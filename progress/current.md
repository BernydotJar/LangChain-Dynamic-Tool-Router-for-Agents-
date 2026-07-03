# Current Progress

## Active Feature

`008-demo-experience`

## Current State

Feature 001 status: `done`

Feature 002 status: `done`

Feature 003 status: `done`

Feature 004 status: `done`

Feature 005 status: `done`

Feature 006 status: `done`

Feature 007 status: `done`

Feature 008 status: `review`

Feature 009 status: `done`

Feature 008 was approved, implemented, verified, and moved to `review`. It is not closed.

## Product Direction

The product is framed as:

> Runtime Tool Authorization for AI Agents.
>
> Never expose every tool. Expose the right tool.

The intended buyer is a team building multi-tenant LangChain/LangGraph agents that needs runtime tool authorization, tenant-aware policy control, fallback behavior, and audit evidence.

## SHIP Epic

Created:

- `epics/SHIP-001-developer-preview-release.md`

SHIP-001 owns the commercial developer-preview release across GitHub, LinkedIn, and early design partner conversations.

## Recently Closed

Feature 004 is closed as `done` after local verification and SHIP review artifact creation.

Feature 005 is closed as `done` after README 3.0 verification and SHIP review artifact creation.

Feature 006 is closed as `done` after trust signal verification and SHIP review artifact creation.

Feature 009 is closed as `done` after release-candidate verification and SHIP review artifact creation.

Feature 007 is closed as `done` after architecture documentation verification and SHIP review artifact creation.

Review artifacts:

- `progress/review_004-sellable-developer-preview.md`
- `progress/review_005-readme-3-landing-page.md`
- `progress/review_006-github-trust-signals.md`
- `progress/review_009-packaging-and-release.md`
- `progress/review_007-architecture-mermaid-diagrams.md`
- `progress/review_008-demo-experience.md`

## Feature 008 Review Evidence

Human approval received:

```text
FEATURE: 008-demo-experience
MODE: SHIP
STATE CHANGE: spec_ready -> approved
```

Implemented:

- `examples/demo_experience/run_demo.py`
- guided demo documentation in `docs/demo-guide.md`
- lifecycle/progress/review artifact updates

Verification:

- `python -m json.tool feature_list.json` passed.
- `PYTHONPATH=src python -m unittest discover -s tests` passed: Ran 23 tests; OK; skipped 2 optional integration-gated tests.
- `python examples/basic_agent/run_example.py` passed.
- `python examples/demo_experience/run_demo.py` passed.
- `PYTHONPATH=src python -m unittest discover -s tests/integration` passed: Ran 2 tests; OK; skipped 2 optional dependency-gated tests.

Accepted implementation boundaries:

- No runtime code changes.
- No external service dependencies.
- No mandatory LangChain/LangGraph dependency.
- No PyPI publish.
- No git tag.
- No GitHub Release.
- No production-readiness claim.

## Next Valid Lifecycle Action

Human closure approval:

```text
APPROVAL
FEATURE: 008-demo-experience
MODE: SHIP
STATE CHANGE: review -> done
```

Do not open the next feature until Feature 008 closure is explicitly approved.
