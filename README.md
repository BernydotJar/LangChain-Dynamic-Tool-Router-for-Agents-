# Runtime Tool Authorization for AI Agents

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Runtime Tool Authorization
for AI Agents
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Never expose every tool.
Expose the right tool.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Dynamic Tool Router is a request-time authorization layer for LangChain and LangGraph agents. It decides which tools an agent may see, inject, invoke, deny, and audit per user, tenant, plan, role, permission, request context, and available MCP-style tool surface.

> Developer preview: local policy files, local audit evidence, framework adapter shapes, and dependency-gated LangChain/LangGraph integration tests. Not a hosted IAM product yet.

## Why This Exists

Everyone is building AI agents. Fewer teams are building the infrastructure that controls which tools those agents are allowed to use.

Most agent frameworks make tool access feel static: define tools, create the agent, run the agent. That works for demos. It breaks down in multi-tenant products where users, tenants, plans, roles, and available MCP servers change per request.

```text
The old question:
Which tools are relevant?

The product question:
Which tools is this user, tenant, plan, role, and request allowed to use right now?
```

## The Missing Layer

```text
LLMs
  ↓
Agents
  ↓
Runtime Tool Authorization   ← this project
  ↓
Tools
  ↓
Your Infrastructure
```

## What It Gives You

| Capability | Developer-preview behavior |
|---|---|
| Runtime authorization | Evaluates tool policy per request context. |
| Tool injection | Exposes only the authorized tool surface. |
| Fallback routing | Maps unavailable tools to a safe fallback tool. |
| Multi-tenant policy | Supports user, tenant, plan, role, permission, context, and MCP-server dimensions. |
| Policy persistence | Loads JSON policy configuration from disk. |
| Audit evidence | Persists JSONL audit events and exports JSON. |
| LangChain/LangGraph compatibility | Provides adapter shapes and dependency-gated real-framework tests. |
| Dashboard visibility | Includes static dashboard documentation and sample-data direction. |

## Killer Contrast

```text
WITHOUT

Agent
 ├── SQL
 ├── CRM
 ├── GitHub
 ├── Stripe
 ├── AWS
 ├── Slack
 ├── Jira
 └── ...

Every tool is potentially visible unless the app manually filters it.
```

```text
WITH

Tenant A
Agent
 ├── SQL     ✓
 └── CRM     ✓

Tenant B
Agent
 ├── GitHub  ✓
 └── Slack   ✓

Tenant C
Agent
 └── AWS     ✓

Each request receives only the tool surface it is allowed to use.
```

## Architecture

```text
                AI Product
                     │
                     ▼
         Authentication Layer
                     │
                     ▼
        Principal Resolution
                     │
                     ▼
 user • tenant • plan • roles • permissions • MCP servers
                     │
                     ▼
╔══════════════════════════════════════════════════════════════════════╗
║                    Runtime Tool Authorization                       ║
║──────────────────────────────────────────────────────────────────────║
║  ✓ Policy evaluation                                                ║
║  ✓ Runtime tool injection                                           ║
║  ✓ RBAC-style gating                                                ║
║  ✓ MCP tool surface filtering                                       ║
║  ✓ Fallback routing                                                 ║
║  ✓ Audit persistence                                                ║
╚══════════════════════════════════════════════════════════════════════╝
                     │
                     ▼
            Authorized Tool Surface
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
  Search Tool    CRM Tool      SQL Tool
```

## Request Lifecycle

```mermaid
sequenceDiagram
    participant User
    participant App
    participant Router as ToolPolicyRouter
    participant Registry as ToolRegistry
    participant Agent
    participant Audit as Audit Store

    User->>App: Send request
    App->>App: Resolve Principal(user, tenant, plan, permissions)
    App->>Router: Evaluate request context
    Router->>Registry: Select candidate tools
    Router->>Router: Apply policy
    Router->>Audit: Record allow/deny/fallback events
    Router-->>App: Authorized tool surface
    App->>Agent: Run agent with routed tools
    Agent->>Audit: Record audited tool invocations
```

## Install

```sh
python -m pip install -e .
```

The core package has no required LangChain or LangGraph runtime dependency. Integration tests are dependency-gated so the router can stay lightweight.

## Run The Demo

```sh
python examples/basic_agent/run_example.py
```

Expected output shape:

```text
Injected tools: search_docs, fetch_customer_record, not_authorized
search_docs: [{'title': 'Plan limits', 'snippet': 'Search result for retention policy'}]
LangGraph state tools: search_docs, not_authorized
Audit export: /tmp/.../runtime_audit_export.json
```

The demo proves:

- JSON policy loading,
- runtime tool injection,
- authorized tool exposure,
- unavailable tool fallback,
- LangGraph-style state middleware,
- JSONL audit persistence,
- JSON audit export.

## Policy Example

```json
{
  "version": 1,
  "fallback_tool_name": "not_authorized",
  "policies": {
    "search_docs": {
      "allowed_plans": ["free", "pro", "enterprise"]
    },
    "fetch_customer_record": {
      "allowed_plans": ["pro", "enterprise"],
      "required_permissions": ["records:read"]
    },
    "delete_customer_record": {
      "allowed_plans": ["enterprise"],
      "required_permissions": ["records:delete"]
    }
  }
}
```

See `docs/policy-format.md` for the full developer-preview policy format.

## Audit Example

```json
{
  "action": "authorize",
  "allowed": false,
  "tool_name": "delete_customer_record",
  "user_id": "user_123",
  "tenant_id": "tenant_acme",
  "reason": "plan is not allowed",
  "metadata": {
    "fallback_tool_name": "not_authorized"
  }
}
```

Audit events are persisted locally as JSON Lines and can be exported to JSON. See `docs/audit-log-format.md`.

## LangChain And LangGraph Compatibility

The core package works with:

- objects with a `name` attribute and `invoke()` method,
- plain callables wrapped in `CallableTool`,
- LangChain-like agent config dictionaries using `RuntimeToolInjector.inject_into_agent_kwargs()`,
- LangGraph-like state dictionaries using `LangGraphToolRouterMiddleware.before_model()`.

Optional real-framework integration tests exist under `tests/integration`. If LangChain/LangGraph packages are not installed, the tests skip with explicit dependency messages.

```sh
PYTHONPATH=src python -m unittest discover -s tests/integration
```

See `docs/langchain-langgraph-integration.md`.

## Who This Is For

| Reader | Why they care |
|---|---|
| CTO | Shows disciplined AI infrastructure, product judgment, and security restraint. |
| AI platform engineer | Provides a reusable policy layer for agent tool surfaces. |
| SaaS product team | Enables plan, tenant, role, and permission-aware agent behavior. |
| Security reviewer | Produces explicit allow, deny, fallback, and invoke evidence. |
| Design partner | Offers a concrete starting point for agent-tool governance pilots. |

## Documentation

- `docs/product-positioning.md` — buyer narrative and wedge use cases.
- `docs/demo-guide.md` — local evaluation flow.
- `docs/policy-format.md` — JSON policy format.
- `docs/audit-log-format.md` — persisted audit event format.
- `docs/security-model.md` — security boundaries and non-goals.
- `docs/admin-dashboard.md` — dashboard purpose and limitations.
- `docs/persistent-policy-and-audit-store.md` — file-backed store notes.
- `docs/langchain-langgraph-integration.md` — optional framework integration behavior.
- `docs/release-notes.md` — developer-preview release notes.

## Security Boundary

Dynamic Tool Router is an authorization and routing layer for tool visibility. It is not a sandbox, secret manager, IAM provider, compliance product, or tamper-proof audit system.

Developer-preview limitations:

- local audit files can be modified by anyone with filesystem access,
- JSON policy validation catches common configuration errors but is not formal verification,
- static admin dashboard is unauthenticated,
- fallback behavior reduces unsafe exposure but does not secure the tool implementation itself,
- no hosted policy API or production auth-provider integration is included.

See `docs/security-model.md`.

## Verification

Core verification:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
```

Optional integration verification:

```sh
PYTHONPATH=src python -m unittest discover -s tests/integration
```

If optional framework dependencies are absent, integration tests should skip explicitly rather than failing core verification.

## Roadmap

```text
SHIP-001  Developer Preview Release                  active

001       Dynamic Tool Router MVP                    done
002       Persistent policy and audit store          done
003       Real LangChain/LangGraph integration       done
004       Sellable developer preview                 done
005       README 3.0 landing page                    in progress
006       Architecture & Mermaid diagrams            candidate
007       Demo experience                            candidate
008       GitHub trust signals                       candidate
009       Packaging & release                        candidate
010       Security whitepaper                        candidate
```

## Design Partner Signal

This project is ready for design-partner conversations around:

- agent tool authorization,
- multi-tenant agent governance,
- LangChain/LangGraph tool routing,
- MCP-style tool surface filtering,
- audit evidence for agent actions,
- productizing internal agent infrastructure.

## Harness SDLC Evidence

This repository follows a harness-style SDLC:

```text
[SPEC] -> [APPROVAL] -> [IMPLEMENT] -> [VERIFY] -> [REVIEW] -> [CLOSE]
```

Feature artifacts live under:

```text
feature_list.json
specs/
adr/
docs/
progress/
epics/
tests/
examples/
```

Developer preview status: SHIP-mode hardening is underway. Do not treat the package as production IAM or compliance infrastructure yet.
