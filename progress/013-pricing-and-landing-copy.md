# 013 Pricing And Landing Copy Progress

Feature: `013-pricing-and-landing-copy`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Commercial Readiness

## State

Status: `spec_ready`

## Summary

Feature 013 is opened as a spec gate for commercial pricing and landing-page placement.

No implementation changes have been made.

## Preconditions

- Feature 001: `done`
- Feature 002: `done`
- Feature 003: `done`
- Feature 004: `done`
- Feature 005: `done`
- Feature 006: `done`
- Feature 007: `done`
- Feature 008: `done`
- Feature 009: `done`
- Feature 010: `done`
- Feature 011: `done`
- Feature 012: `done`

## Spec Artifacts

Created:

- `specs/013-pricing-and-landing-copy/requirements.md`
- `specs/013-pricing-and-landing-copy/design.md`
- `specs/013-pricing-and-landing-copy/tasks.md`
- `adr/013-pricing-and-landing-copy-strategy.md`

## Proposed Placement

Pricing should be added in three layers after approval:

1. `README.md` - concise conversion section after `Design Partner Signal` and before `Harness SDLC Evidence`.
2. `docs/pricing.md` - canonical pricing page.
3. `docs/design-partner-kit.md` - design partner sales offer.

## Proposed Pricing

Public launch:

- 30-day free trial.
- Solo: `$9/month`.
- Team: `$19/user/month`.

Design partner offer:

- First 20 design partners.
- `$49/month` flat for up to 5 users.
- Founding price locked for 12 months.

Enterprise:

- Custom future/custom scope.

## Hard Constraints

- No runtime code changes.
- No dependency changes.
- No PyPI publish.
- No git tag.
- No GitHub Release.
- No production-readiness claim.
- No enterprise-readiness claim.
- No compliance certification claim.
- No guaranteed security outcome claim.

## Next Valid Lifecycle Action

Explicit implementation approval:

```text
APPROVAL TO IMPLEMENT
FEATURE: 013-pricing-and-landing-copy
MODE: SHIP
STATE CHANGE: spec_ready -> in_progress
```

Do not implement pricing copy until approval is received.
