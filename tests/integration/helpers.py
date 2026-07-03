from __future__ import annotations

import json
import tempfile
from pathlib import Path

from tool_policy_router import (
    CallableTool,
    FileAuditStore,
    FilePolicyStore,
    Principal,
    RuntimeToolInjector,
    ToolRegistry,
    ToolRequestContext,
    fallback_tool,
)


def write_policy_file(directory: str | Path) -> Path:
    path = Path(directory) / "tool_policies.json"
    path.write_text(
        json.dumps(
            {
                "version": 1,
                "default_allow": False,
                "fallback_tool_name": "not_authorized",
                "policies": {
                    "search_docs": {
                        "allowed_plans": ["pro", "enterprise"],
                        "required_permissions": ["docs:search"],
                    },
                    "admin_delete": {
                        "allowed_plans": ["enterprise"],
                        "required_roles": ["admin"],
                    },
                    "not_authorized": {
                        "allowed_plans": ["free", "pro", "enterprise"],
                    },
                },
            }
        ),
        encoding="utf-8",
    )
    return path


def build_context() -> ToolRequestContext:
    return ToolRequestContext(
        principal=Principal(
            user_id="user_1",
            tenant_id="tenant_1",
            plan="pro",
            roles={"member"},
            permissions={"docs:search"},
        ),
        request_id="req_integration_1",
    )


def build_registry(search_tool: object) -> ToolRegistry:
    return ToolRegistry(
        [
            search_tool,
            CallableTool("admin_delete", lambda record_id: {"deleted": record_id}),
            fallback_tool(),
        ]
    )


def build_integration_system(search_tool: object):
    workspace = tempfile.TemporaryDirectory()
    policy_path = write_policy_file(workspace.name)
    audit_store = FileAuditStore(Path(workspace.name) / "audit.jsonl")
    router = FilePolicyStore(policy_path).create_router(audit_log=audit_store)
    injector = RuntimeToolInjector(build_registry(search_tool), router)
    return workspace, audit_store, injector, build_context()
