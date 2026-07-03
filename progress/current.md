# Current Progress

## Active Feature

`004-sellable-developer-preview`

## Current State

Feature 001 status: `done`

Feature 002 status: `done`

Feature 003 status: `done`

Feature 004 status: `in_progress`

Feature 005 status: `spec_ready`

Feature 004 remains the active implementation feature. Feature 005 has been specified as the next SHIP landing-page increment but must not move to implementation until Feature 004 verification and review handling are complete.

## Product Direction

The product is now being framed as:

> Runtime Tool Authorization for AI Agents.
>
> Never expose every tool. Expose the right tool.

The intended buyer is a team building multi-tenant LangChain/LangGraph agents that needs runtime tool authorization, tenant-aware policy control, fallback behavior, and audit evidence.

## SHIP Epic

Created:

- `epics/SHIP-001-developer-preview-release.md`

SHIP-001 owns the commercial developer-preview release across GitHub, LinkedIn, and early design partner conversations.

## Feature 004 Implementation Pass

Completed:

- README rewritten for buyer-facing developer-preview positioning.
- Runtime Tool Authorization hero added.
- Futuristic terminal-native architecture diagrams added.
- Mermaid request lifecycle added.
- Quickstart and demo flow added.
- Policy example added.
- Audit example added.
- Security model summary added.
- Verification commands added.
- SHIP roadmap added.
- `docs/product-positioning.md` added.
- `docs/security-model.md` expanded.
- `docs/policy-format.md` added.
- `docs/audit-log-format.md` added.
- `docs/demo-guide.md` added.
- `docs/admin-dashboard.md` added.
- `docs/release-notes.md` added.

## Feature 005 Spec Gate

Created:

- `specs/005-readme-3-landing-page/requirements.md`
- `specs/005-readme-3-landing-page/design.md`
- `specs/005-readme-3-landing-page/tasks.md`
- `adr/005-readme-as-product-landing-page.md`
- `progress/005-readme-3-landing-page.md`

Feature 005 is registered as `spec_ready`.

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

Feature 005 remains at `spec_ready` until Feature 004 review handling is complete.

## Current SHIP-Mode Risks

- Static dashboard remains unauthenticated.
- Local audit files are not tamper-proof.
- Optional LangChain/LangGraph dependencies may be absent during integration verification.
- No hosted API, auth-provider integration, database, billing, or compliance guarantees.
- Feature 004 has not yet been locally verified after the README/docs implementation pass.
