# Current Progress

## Active Feature

`009-packaging-and-release`

## Current State

Feature 001 status: `done`

Feature 002 status: `done`

Feature 003 status: `done`

Feature 004 status: `done`

Feature 005 status: `done`

Feature 006 status: `done`

Feature 009 status: `in_progress`

Feature 006 was approved for closure. Feature 009 is now the active SHIP implementation feature.

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

Review artifacts:

- `progress/review_004-sellable-developer-preview.md`
- `progress/review_005-readme-3-landing-page.md`
- `progress/review_006-github-trust-signals.md`

## Feature 009 Implementation Pass

Completed:

- Feature 009 registered as `in_progress`.
- `pyproject.toml` updated for developer-preview packaging.
- Package version set to `0.1.0.dev0`.
- Optional `integrations` and `dev` extras added.
- `docs/release-checklist.md` added.
- `docs/v0.1.0-dev-release-notes.md` added.
- README Packaging & Release section added.
- CHANGELOG updated.
- `progress/009-packaging-and-release.md` added.

## Feature 009 Required Local Verification

Run:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
PYTHONPATH=src python -m unittest discover -s tests/integration
python -m pip install -e .
python -m pip install -e .[dev]
python -m build
```

Manual checks:

- Package metadata is accurate.
- README release section does not claim PyPI publication.
- Release checklist does not create tags without maintainer approval.
- `v0.1.0-dev` notes clearly state developer-preview limitations.

## Next Valid Lifecycle Action

After local verification passes:

```text
FEATURE: 009-packaging-and-release
MODE: SHIP
STATE CHANGE: in_progress -> review
```

Then create:

```text
progress/review_009-packaging-and-release.md
```
