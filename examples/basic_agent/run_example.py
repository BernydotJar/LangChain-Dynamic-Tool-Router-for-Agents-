from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from tool_policy_router import (  # noqa: E402
    CallableTool,
    FileAuditStore,
    FilePolicyStore,
    LangGraphToolRouterMiddleware,
    Principal,
    RuntimeToolInjector,
    ToolRegistry,
    ToolRequestContext,
)


def search_docs(query: str) -> list[dict[str, str]]:
    return [{"title": "Plan limits", "snippet": f"Search result for {query}"}]


def fetch_customer_record(record_id: str) -> dict[str, str]:
    return {"record_id": record_id, "status": "active"}


def delete_customer_record(record_id: str) -> dict[str, str]:
    return {"record_id": record_id, "deleted": "true"}


def unavailable_tool(**_: object) -> dict[str, str]:
    return {"error": "This tool is not available for this request."}


def build_registry() -> ToolRegistry:
    registry = ToolRegistry()
    registry.register(CallableTool("search_docs", search_docs, "Search tenant documentation."))
    registry.register(CallableTool("fetch_customer_record", fetch_customer_record, "Fetch CRM record."))
    registry.register(CallableTool("delete_customer_record", delete_customer_record, "Delete CRM record."))
    registry.register(CallableTool("not_authorized", unavailable_tool, "Fallback for denied tools."))
    return registry


def main() -> None:
    audit_output_dir = Path(tempfile.gettempdir()) / "tool_policy_router_example"
    audit_log = FileAuditStore(audit_output_dir / "runtime_audit.jsonl", reset=True)
    policy_store = FilePolicyStore(ROOT / "examples" / "policies" / "tool_policies.json")
    router = policy_store.create_router(audit_log=audit_log)
    injector = RuntimeToolInjector(build_registry(), router)

    context = ToolRequestContext(
        principal=Principal(
            user_id="user_123",
            tenant_id="tenant_acme",
            plan="pro",
            roles={"analyst"},
            permissions={"crm:read"},
        ),
        request_id="req_demo_001",
        available_mcp_servers={"crm-mcp"},
    )

    tools = injector.tools_for_context(
        context,
        candidate_tool_names=["search_docs", "fetch_customer_record", "delete_customer_record"],
    )
    print("Injected tools:", ", ".join(tool.name for tool in tools))
    print("search_docs:", tools[0].invoke("retention policy"))

    middleware = LangGraphToolRouterMiddleware(injector)
    state = middleware.before_model(
        {
            "tool_context": context,
            "candidate_tool_names": ["search_docs", "delete_customer_record"],
        }
    )
    print("LangGraph state tools:", ", ".join(tool.name for tool in state["tools"]))
    print("Audit events:")
    print(json.dumps(audit_log.to_dicts(), indent=2))
    export_path = audit_output_dir / "runtime_audit_export.json"
    audit_log.export_json(export_path)
    print("Audit export:", export_path)


if __name__ == "__main__":
    main()
