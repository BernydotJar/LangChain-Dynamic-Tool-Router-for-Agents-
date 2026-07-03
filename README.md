# LangChain Dynamic Tool Router for Agents

Policy-driven runtime tool routing for LangChain and LangGraph agents.

This MVP is a lightweight "RBAC layer for AI tools": it selects and injects tools dynamically at request time based on user, tenant, plan, roles, permissions, context, and available MCP servers.

## What It Provides

- `ToolPolicyRouter` for policy evaluation.
- Runtime tool injection for agent request contexts.
- Per-user and per-tenant authorization rules.
- Tool audit log with allow, deny, invoke, and fallback events.
- Fallback behavior when a tool is not authorized.
- Framework-agnostic adapters for LangChain-style and LangGraph-style flows.
- Static admin dashboard example for reviewing policy decisions and audit events.

## Install For Local Development

```sh
python -m pip install -e .
```

No runtime dependencies are required for the MVP.

## Quick Example

```python
from tool_policy_router import (
    CallableTool,
    InMemoryAuditLog,
    Principal,
    RuntimeToolInjector,
    ToolPolicy,
    ToolPolicyRouter,
    ToolRegistry,
    ToolRequestContext,
)

registry = ToolRegistry()
registry.register(CallableTool("basic_search", lambda query: f"result: {query}"))
registry.register(CallableTool("admin_delete", lambda record_id: f"deleted {record_id}"))
registry.register(CallableTool("not_authorized", lambda **_: "Tool is not available for this request."))

router = ToolPolicyRouter(
    policies={
        "basic_search": ToolPolicy(allowed_plans={"free", "pro", "enterprise"}),
        "admin_delete": ToolPolicy(required_permissions={"records:delete"}, allowed_plans={"enterprise"}),
    },
    fallback_tool_name="not_authorized",
    audit_log=InMemoryAuditLog(),
)

context = ToolRequestContext(
    principal=Principal(
        user_id="user_123",
        tenant_id="tenant_acme",
        plan="pro",
        permissions={"records:read"},
    )
)

injector = RuntimeToolInjector(registry, router)
tools = injector.tools_for_context(context)

assert [tool.name for tool in tools] == ["basic_search", "not_authorized"]
```

## LangChain And LangGraph Compatibility

The package does not require LangChain or LangGraph at runtime. It works with:

- objects with a `name` attribute and `invoke()` method,
- plain callables wrapped in `CallableTool`,
- LangChain-like agent config dictionaries using `RuntimeToolInjector.inject_into_agent_kwargs()`,
- LangGraph-like state dictionaries using `LangGraphToolRouterMiddleware.before_model()`.

## SDLC Artifacts

This repository follows a harness-style artifact layout:

```text
feature_list.json
specs/001-dynamic-tool-router/
progress/
adr/
docs/
```

The first feature is implemented in MVP mode. SHIP-mode gaps are documented in the spec and progress files.
