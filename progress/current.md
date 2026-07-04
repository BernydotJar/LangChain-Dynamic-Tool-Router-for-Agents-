# Current Progress

## Active Feature

`013-pricing-and-landing-copy`

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

Feature 012 status: `done`

Feature 013 status: `spec_ready`

Feature 013 is opened as a SHIP-mode spec gate for pricing and landing copy placement.

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

Feature 012 is closed as `done` after design partner kit verification and SHIP review artifact creation.

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

## Feature 013 Spec Gate

Created:

- `specs/013-pricing-and-landing-copy/requirements.md`
- `specs/013-pricing-and-landing-copy/design.md`
- `specs/013-pricing-and-landing-copy/tasks.md`
- `adr/013-pricing-and-landing-copy-strategy.md`
- `progress/013-pricing-and-landing-copy.md`

Purpose:

Feature 013 adds commercial pricing and landing-page copy for Runtime Tool Authorization for AI Agents.

Proposed placement:

1. `README.md` - concise conversion section after `Design Partner Signal` and before `Harness SDLC Evidence`.
2. `docs/pricing.md` - canonical pricing page.
3. `docs/design-partner-kit.md` - design partner sales offer.

Proposed pricing:

- 30-day free trial.
- Solo: `$9/month`.
- Team: `$19/user/month`.
- Design Partner: `$49/month` flat for up to 5 users.
- First 20 design partners only.
- Founding price locked for 12 months.
- Enterprise: custom future/custom scope.

No implementation changes were made during the spec gate.

## Next Valid Lifecycle Action

Explicit implementation approval:

```text
APPROVAL TO IMPLEMENT
FEATURE: 013-pricing-and-landing-copy
MODE: SHIP
STATE CHANGE: spec_ready -> in_progress
```

Do not implement pricing copy until approval is received.
