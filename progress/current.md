# Current Progress

## Active Feature

`004-sellable-developer-preview`

## Current State

Feature 001 status: `done`

Feature 002 status: `done`

Feature 003 status: `done`

Feature 004 status: `in_progress`

Feature 003 was closed after human approval. Feature 004 was approved and implementation has started in SHIP mode.

## Product Direction

The product is now being reframed from MVP validation toward a sellable developer-preview package:

> Auth0-style authorization for AI agent tools.

The intended buyer is a team building multi-tenant LangChain/LangGraph agents that needs runtime tool authorization, tenant-aware policy control, fallback behavior, and audit evidence.

## Feature 004 Implementation Pass

Completed:

- README rewritten for buyer-facing developer-preview positioning.
- Futuristic terminal-native architecture diagrams added.
- Quickstart and demo flow added.
- Policy example added.
- Audit example added.
- Security model summary added.
- Verification commands added.
- Roadmap added.
- `docs/product-positioning.md` added.
- `docs/security-model.md` expanded.
- `docs/policy-format.md` added.
- `docs/audit-log-format.md` added.
- `docs/demo-guide.md` added.
- `docs/admin-dashboard.md` added.
- `docs/release-notes.md` added.

## Feature 004 Required Local Verification

Run:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
PYTHONPATH=src python -m unittest discover -s tests/integration
```

Feature 004 remains `in_progress` until local verification evidence is reported.

## Next Valid Lifecycle Action

After local verification passes:

```text
FEATURE: 004-sellable-developer-preview
MODE: SHIP
STATE CHANGE: in_progress -> review
```

Then create:

```text
progress/review_004-sellable-developer-preview.md
```

## Current SHIP-Mode Risks

- Static dashboard remains unauthenticated.
- Local audit files are not tamper-proof.
- Optional LangChain/LangGraph dependencies may be absent during integration verification.
- No hosted API, auth-provider integration, database, billing, or compliance guarantees.
- Feature 004 has not yet been locally verified after the README/docs implementation pass.
