# Current Progress

## Active Feature

`003-langchain-langgraph-real-integration-tests`

## Current State

Feature 003 status: `review`

Feature 004 status: `spec_ready`

`001-dynamic-tool-router` is closed as an MVP.

`002-persistent-policy-and-audit-store` is closed as an MVP.

`003-langchain-langgraph-real-integration-tests` is implemented, verified, and ready for review/closure approval.

`004-sellable-developer-preview` has been created as the first SHIP-mode productization feature. It is a spec gate only and must not be implemented until explicit approval.

## Product Direction

The product is now being reframed from MVP validation toward a sellable developer-preview package:

> Auth0-style authorization for AI agent tools.

The intended buyer is a team building multi-tenant LangChain/LangGraph agents that needs runtime tool authorization, tenant-aware policy control, fallback behavior, and audit evidence.

## Feature 003 Verification

Passed:

```sh
PYTHONPATH=src python -m unittest discover -s tests
# Ran 23 tests in 0.006s
# OK (skipped=2)

python examples/basic_agent/run_example.py
# Injected tools: search_docs, fetch_customer_record, not_authorized
# LangGraph state tools: search_docs, not_authorized
# Audit export: /var/folders/vv/v8kws2hj0gbc976b69bbccrc0000gn/T/tool_policy_router_example/runtime_audit_export.json

python -m json.tool feature_list.json
# valid JSON

PYTHONPATH=src python -m unittest discover -s tests/integration
# Ran 2 tests in 0.000s
# OK (skipped=2)
```

Review artifact:

- `progress/review_003-langchain-langgraph-real-integration-tests.md`

Next valid lifecycle action for Feature 003:

```text
FEATURE: 003-langchain-langgraph-real-integration-tests
MODE: MVP
STATE CHANGE: review -> done
```

## Feature 004 Spec Gate

Created:

- `specs/004-sellable-developer-preview/requirements.md`
- `specs/004-sellable-developer-preview/design.md`
- `specs/004-sellable-developer-preview/tasks.md`
- `adr/004-ship-mode-sellable-developer-preview.md`
- `progress/004-sellable-developer-preview.md`

Feature 004 applies SHIP-mode developer-tool principles:

- one-screen clarity,
- copy-paste quickstart,
- immediate demo path,
- futuristic text diagrams,
- realistic multi-tenant examples,
- policy/audit documentation,
- security honesty,
- visible verification evidence,
- integration proof or explicit dependency gates,
- release notes.

Recommended lifecycle handling:

1. Close Feature 003 as `done` if its review evidence is accepted.
2. Approve Feature 004: `spec_ready -> approved`.
3. Implement Feature 004 in SHIP mode.

## Feature 004 Required Verification During Implementation

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
PYTHONPATH=src python -m unittest discover -s tests/integration
```

## Current SHIP-Mode Risks

- README still reads like an MVP rather than a sellable developer-preview product.
- Static dashboard remains unauthenticated.
- Local audit files are not tamper-proof.
- Optional LangChain/LangGraph dependencies were not installed during Feature 003 verification.
- No hosted API, auth-provider integration, database, billing, or compliance guarantees.
