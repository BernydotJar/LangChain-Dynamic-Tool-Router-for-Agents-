# Current Progress

## Active Feature

`015-billing-provider-abstraction`

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

Feature 013 status: `done`

Feature 014 status: `done`

Feature 015 status: `spec_ready`

Feature 015 is open as a spec gate. Do not implement billing provider abstraction until explicit approval is received.

## Product Direction

The product is framed as:

> Runtime Tool Authorization for AI Agents.
>
> Never expose every tool. Expose the right tool.

The intended buyer is a team building multi-tenant LangChain/LangGraph agents that needs runtime tool authorization, tenant-aware policy control, fallback behavior, audit evidence, and entitlement-backed premium access.

## Commercial Architecture Direction

Feature 014 added mock-safe Stripe entitlement billing contracts.

Feature 015 reframes the commercial layer as provider-agnostic:

- entitlement is core,
- Stripe is an optional adapter,
- manual license activation is a valid developer-preview path,
- merchant-of-record and local gateway paths remain future adapters,
- no production billing claim is made.

## SHIP Epic

Created:

- `epics/SHIP-001-developer-preview-release.md`

SHIP-001 owns the commercial developer-preview release across GitHub, LinkedIn, and early design partner conversations.

## Recently Closed

Feature 013 is closed as `done` after pricing, monetization architecture, release-candidate verification, and SHIP review artifact creation.

Feature 014 is closed as `done` after Stripe entitlement billing implementation, release-candidate verification, SHIP review artifact creation, and closure approval.

Review artifacts:

- `progress/review_013-pricing-and-landing-copy.md`
- `progress/review_014-stripe-entitlement-billing.md`

## Feature 015 Spec Gate

Created and updated:

- `specs/015-billing-provider-abstraction/requirements.md`
- `specs/015-billing-provider-abstraction/design.md`
- `specs/015-billing-provider-abstraction/tasks.md`
- `adr/015-billing-provider-abstraction.md`
- `progress/015-billing-provider-abstraction.md`
- `README.md`
- `feature_list.json`

Spec direction:

- define a provider-neutral billing boundary,
- preserve entitlement and license concepts from Feature 014,
- reframe Stripe as optional and region-dependent,
- support manual license activation as a developer-preview path,
- leave merchant-of-record and local gateway providers as future adapters,
- avoid production billing, legal, tax, and unsupported-region claims.

## Next Valid Lifecycle Action

Explicit approval:

```text
APPROVAL TO IMPLEMENT
FEATURE: 015-billing-provider-abstraction
MODE: SHIP
STATE CHANGE: spec_ready -> in_progress
```
