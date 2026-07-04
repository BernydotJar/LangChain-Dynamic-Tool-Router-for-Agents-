# Current Progress

## Active Feature

`012-design-partner-kit`

## Current State

Feature 001 status: `done`

Feature 002 status: `done`

Feature 003 status: `done`

Feature 004 status: `done`

Feature 005 status: `done`

Feature 006 status: `done`

Feature 007 status: `done`

Feature 008 status: `done`

Feature 009 status: `done`

Feature 010 status: `done`

Feature 011 status: `done`

Feature 012 status: `review`

Feature 012 is in review after design partner kit implementation and required release-candidate verification completed successfully.

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

Feature 008 is closed as `done` after guided demo verification and SHIP review artifact creation.

Feature 010 is closed as `done` after release-candidate polish verification and SHIP review artifact creation.

Feature 011 is closed as `done` after security whitepaper verification and SHIP review artifact creation.

Review artifacts:

- `progress/review_004-sellable-developer-preview.md`
- `progress/review_005-readme-3-landing-page.md`
- `progress/review_006-github-trust-signals.md`
- `progress/review_009-packaging-and-release.md`
- `progress/review_007-architecture-mermaid-diagrams.md`
- `progress/review_008-demo-experience.md`
- `progress/review_010-release-candidate-polish.md`
- `progress/review_011-security-whitepaper.md`
- `progress/review_012-design-partner-kit.md`

## Feature 012 Spec Gate

Created:

- `specs/012-design-partner-kit/requirements.md`
- `specs/012-design-partner-kit/design.md`
- `specs/012-design-partner-kit/tasks.md`
- `adr/012-design-partner-kit-strategy.md`
- `progress/012-design-partner-kit.md`

Purpose:

Feature 012 prepares a design partner kit for Runtime Tool Authorization for AI Agents. It is tied to SHIP-001 Wave 3: design partner readiness.

No implementation changes were made during the spec gate.

## Feature 012 Review

Human approval received to continue Feature 012 from `spec_ready` into implementation.

Implemented:

- `docs/design-partner-kit.md`
- README discoverability for `docs/design-partner-kit.md`
- README roadmap update showing 012 as `in progress`
- progress and task bookkeeping
- review artifact at `progress/review_012-design-partner-kit.md`

The design partner kit covers:

- ideal design partner profile,
- buyer personas and evaluator roles,
- target pain points,
- qualification criteria,
- discovery questions,
- pilot scope template,
- safe non-production evaluation scenarios,
- 20-30 minute demo call script,
- success metrics,
- feedback checklist,
- suggested outbound message,
- security discussion guide,
- explicit non-goals and boundaries.

Verification passed:

- `python -m json.tool feature_list.json`
- `PYTHONPATH=src python -m unittest discover -s tests`
- `python examples/basic_agent/run_example.py`
- `python examples/demo_experience/run_demo.py`
- `PYTHONPATH=src python -m unittest discover -s tests/integration`
- `python scripts/verify_release_candidate.py`

Preserved constraints:

- No runtime behavior changed.
- No dependencies changed.
- No package was published.
- No git tag was created.
- No GitHub Release was created.
- No production-readiness claim was introduced.
- No enterprise-readiness claim was introduced.
- No compliance certification claim was introduced.
- No guaranteed security outcome claim was introduced.

## Next Valid Lifecycle Action

Human closure approval:

```text
APPROVAL TO CLOSE
FEATURE: 012-design-partner-kit
MODE: SHIP
STATE CHANGE: review -> done
```

Do not close Feature 012 until explicit closure approval is received.
