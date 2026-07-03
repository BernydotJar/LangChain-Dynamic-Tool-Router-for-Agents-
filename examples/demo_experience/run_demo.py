from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path
from typing import Any

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


POLICY_PATH = ROOT / "examples" / "policies" / "tool_policies.json"
CANDIDATE_TOOLS = ("search_docs", "fetch_customer_record", "delete_customer_record")


def search_docs(query: str) -> list[dict[str, str]]:
    return [{"title": "Retention policy", "snippet": f"Search result for {query}"}]


def fetch_customer_record(record_id: str) -> dict[str, str]:
    return {"record_id": record_id, "status": "active", "tier": "pro"}


def delete_customer_record(record_id: str) -> dict[str, str]:
    return {"record_id": record_id, "deleted": "true"}


def not_authorized(*_: Any, **__: Any) -> dict[str, str]:
    return {"error": "Tool is not authorized for this request."}


def build_registry() -> ToolRegistry:
    registry = ToolRegistry()
    registry.register(CallableTool("search_docs", search_docs, "Search tenant documentation."))
    registry.register(CallableTool("fetch_customer_record", fetch_customer_record, "Fetch CRM record."))
    registry.register(CallableTool("delete_customer_record", delete_customer_record, "Delete CRM record."))
    registry.register(CallableTool("not_authorized", not_authorized, "Fallback for denied tools."))
    return registry


def build_context() -> ToolRequestContext:
    return ToolRequestContext(
        principal=Principal(
            user_id="user_123",
            tenant_id="tenant_acme",
            plan="pro",
            roles={"analyst"},
            permissions={"crm:read"},
            attributes={"region": "us", "demo": True},
        ),
        request_id="req_demo_experience_001",
        conversation_id="conv_demo_experience_001",
        state={"workflow": "customer_research", "risk": "standard"},
        available_mcp_servers={"crm-mcp"},
    )


def tool_names(tools: list[Any]) -> str:
    return ", ".join(tool.name for tool in tools)


def print_section(title: str) -> None:
    print()
    print(f"== {title} ==")


def print_context(context: ToolRequestContext) -> None:
    principal = context.principal
    context_view = {
        "request_id": context.request_id,
        "conversation_id": context.conversation_id,
        "tenant_id": principal.tenant_id,
        "user_id": principal.user_id,
        "plan": principal.plan,
        "roles": sorted(principal.roles),
        "permissions": sorted(principal.permissions),
        "available_mcp_servers": sorted(context.available_mcp_servers),
        "state": dict(context.state),
    }
    print(json.dumps(context_view, indent=2, sort_keys=True))


def print_policy_summary(policy_path: Path) -> None:
    raw_policy = json.loads(policy_path.read_text(encoding="utf-8"))
    print(f"Loaded policy file: {policy_path.relative_to(ROOT)}")
    print(f"Fallback tool: {raw_policy['fallback_tool_name']}")
    for tool_name, policy in raw_policy["policies"].items():
        requirements = {
            key: value
            for key, value in policy.items()
            if key != "reason" and value not in (None, [], {})
        }
        print(f"- {tool_name}: {requirements or {'allowed': 'by policy'}}")


def print_route_decisions(router: Any, context: ToolRequestContext) -> None:
    route_result = router.route(CANDIDATE_TOOLS, context)
    print(f"Candidate tool surface: {', '.join(CANDIDATE_TOOLS)}")
    print(f"Allowed tool surface: {', '.join(route_result.allowed_tool_names)}")
    for decision in route_result.denied:
        print(
            "Denied path: "
            f"{decision.tool_name} -> {decision.reason} -> fallback {decision.fallback_tool_name}"
        )


def main() -> None:
    audit_output_dir = Path(tempfile.gettempdir()) / "tool_policy_router_demo_experience"
    audit_log = FileAuditStore(audit_output_dir / "guided_demo_audit.jsonl", reset=True)
    router = FilePolicyStore(POLICY_PATH).create_router(audit_log=audit_log)
    injector = RuntimeToolInjector(build_registry(), router)
    context = build_context()

    print("Runtime Tool Authorization for AI Agents")
    print("Never expose every tool. Expose the right tool.")
    print("The missing authorization layer between LLMs -> Agents -> Tools -> Your Infrastructure")

    print_section("1. Request Context")
    print_context(context)

    print_section("2. JSON Policy Loading")
    print_policy_summary(POLICY_PATH)

    print_section("3. Runtime Tool Authorization")
    print_route_decisions(router, context)

    print_section("4. LangChain-Style Adapter Boundary")
    agent_kwargs = injector.inject_into_agent_kwargs(
        {"model": "demo-model"},
        context,
        CANDIDATE_TOOLS,
    )
    print(f"Agent receives tools: {tool_names(agent_kwargs['tools'])}")
    print(f"Agent can invoke search_docs: {agent_kwargs['tools'][0].invoke('retention policy')}")

    print_section("5. LangGraph-Style Adapter Boundary")
    middleware = LangGraphToolRouterMiddleware(injector)
    next_state = middleware.before_model(
        {
            "tool_context": context,
            "candidate_tool_names": CANDIDATE_TOOLS,
            "messages": ["Find the customer record, but do not expose destructive tools."],
        }
    )
    print(f"Graph state receives tools: {tool_names(next_state['tools'])}")

    print_section("6. Fallback Behavior")
    fallback_tool = next(tool for tool in next_state["tools"] if tool.name == "not_authorized")
    print(f"Fallback invoke result: {fallback_tool.invoke('delete_customer_record')}")

    print_section("7. Audit Evidence")
    audit_events = audit_log.to_dicts()
    for index, event in enumerate(audit_events, start=1):
        metadata = event.get("metadata") or {}
        fallback = metadata.get("fallback_tool_name")
        fallback_note = f", fallback={fallback}" if fallback else ""
        print(
            f"{index}. action={event['action']}, tool={event['tool_name']}, "
            f"allowed={event['allowed']}, reason={event['reason']}{fallback_note}"
        )

    export_path = audit_output_dir / "guided_demo_audit_export.json"
    audit_log.export_json(export_path)
    print(f"Audit export: {export_path}")


if __name__ == "__main__":
    main()
