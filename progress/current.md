# Current Progress

## Active Feature

`005-readme-3-landing-page`

## Current State

Feature 001 status: `done`

Feature 002 status: `done`

Feature 003 status: `done`

Feature 004 status: `done`

Feature 005 status: `in_progress`

Feature 004 was approved for closure. Feature 005 is now the active SHIP implementation feature.

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

## Feature 004 Closure

Feature 004 is closed as `done` after local verification and SHIP review artifact creation.

Review artifact:

- `progress/review_004-sellable-developer-preview.md`

## Feature 005 Implementation Pass

Completed:

- Feature 005 moved from `spec_ready` to `in_progress`.
- README hero retained the Runtime Tool Authorization identity.
- README sharpened the Why This Exists section.
- README added a capability grid.
- README tightened install and demo sections.
- README updated the audit example to match observed local output shape.
- README added a Who This Is For section.
- README linked admin dashboard documentation.
- README added a design partner signal section.
- README roadmap now reflects Feature 004 done and Feature 005 in progress.

## Feature 005 Required Local Verification

Run:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
PYTHONPATH=src python -m unittest discover -s tests/integration
```

Manual checks:

- README renders cleanly on GitHub.
- Mermaid renders cleanly.
- Quickstart is accurate.
- Product claims match implementation.
- No unsupported benchmark, security, customer, or revenue claims.

## Next Valid Lifecycle Action

After local verification passes:

```text
FEATURE: 005-readme-3-landing-page
MODE: SHIP
STATE CHANGE: in_progress -> review
```

Then create:

```text
progress/review_005-readme-3-landing-page.md
```
