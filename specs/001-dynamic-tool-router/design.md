# 001-dynamic-tool-router Design

## Approach

Implement a dependency-free Python package with:

- dataclass contracts for principals, contexts, policies, decisions, and route results
- mutable `ToolRegistry`
- `ToolPolicyRouter` for authorization
- `InMemoryAuditLog` for MVP audit evidence
- `RuntimeToolInjector` for LangChain-style tool injection
- `LangGraphToolRouterMiddleware` for state-based injection
- static admin dashboard example

The router is framework-agnostic and returns wrapped tools that record invocation audit events.

## Files You May Read

- `feature_list.json`
- `specs/001-dynamic-tool-router/**`
- `src/tool_policy_router/**`
- `tests/**`
- `examples/**`
- `docs/**`
- `progress/**`

## Files You May Touch

- `README.md`
- `AGENTS.md`
- `RTK.md`
- `CLAUDE.md`
- `feature_list.json`
- `pyproject.toml`
- `src/tool_policy_router/**`
- `tests/**`
- `examples/**`
- `docs/**`
- `adr/**`
- `progress/**`
- `specs/001-dynamic-tool-router/**`

## Files You Must Not Touch

- secrets
- deployment credentials
- unrelated local repositories

## Data Contracts

`Principal`:

- `user_id`
- `tenant_id`
- `plan`
- `roles`
- `permissions`
- `attributes`

`ToolRequestContext`:

- `principal`
- `request_id`
- `conversation_id`
- `state`
- `available_mcp_servers`

`ToolPolicy`:

- `allowed_users`
- `allowed_tenants`
- `allowed_plans`
- `required_roles`
- `required_permissions`
- `required_mcp_servers`
- `condition`
- `reason`

## Dependencies

No external dependencies are required for the MVP.

## Context7 Checkpoints

None required. The implementation avoids direct LangChain/LangGraph APIs for MVP compatibility.

## Risks

- Risk: applications bypass the router and expose raw tools.
  - Mitigation: document trust boundary and use injection adapters.
- Risk: fallback tool leaks policy details.
  - Mitigation: fallback message is generic by default.
- Risk: in-memory audit log is not production durable.
  - Mitigation: document as SHIP-mode gap.

## Verification Plan

Run:

```sh
python -m unittest discover -s tests
python examples/basic_agent/run_example.py
```
