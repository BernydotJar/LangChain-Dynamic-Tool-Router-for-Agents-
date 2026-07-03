# Current Progress

## Active Feature

`006-github-trust-signals`

## Current State

Feature 001 status: `done`

Feature 002 status: `done`

Feature 003 status: `done`

Feature 004 status: `done`

Feature 005 status: `done`

Feature 006 status: `in_progress`

Feature 005 was approved for closure. Feature 006 is now the active SHIP implementation feature.

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

Review artifacts:

- `progress/review_004-sellable-developer-preview.md`
- `progress/review_005-readme-3-landing-page.md`

## Feature 006 Implementation Pass

Completed:

- Feature 006 registered as `in_progress`.
- `SECURITY.md` added.
- `CONTRIBUTING.md` added.
- `CHANGELOG.md` added.
- `CODE_OF_CONDUCT.md` added.
- `LICENSE` added.
- README Trust & Project Governance section added.
- `progress/006-github-trust-signals.md` updated.

## Feature 006 Required Local Verification

Run:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
PYTHONPATH=src python -m unittest discover -s tests/integration
```

Manual checks:

- README links to trust files.
- Security policy does not claim production security certification.
- CONTRIBUTING references harness workflow.
- CHANGELOG accurately reflects developer-preview milestones.
- LICENSE exists and is visible.

## Next Valid Lifecycle Action

After local verification passes:

```text
FEATURE: 006-github-trust-signals
MODE: SHIP
STATE CHANGE: in_progress -> review
```

Then create:

```text
progress/review_006-github-trust-signals.md
```
