# 014 Stripe Entitlement Billing Progress

Feature: `014-stripe-entitlement-billing`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Commercial Readiness

## State

Status: `spec_ready`

## Summary

Feature 014 is opened as a spec gate for Stripe Checkout, subscription webhooks, entitlement storage, license validation, and premium feature gating.

No billing runtime code has been implemented.

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
- Feature 013: `done`

## Spec Artifacts

Created:

- `specs/014-stripe-entitlement-billing/requirements.md`
- `specs/014-stripe-entitlement-billing/design.md`
- `specs/014-stripe-entitlement-billing/tasks.md`
- `adr/014-stripe-entitlement-billing.md`

## Proposed Billing Flow

```text
public install -> 30-day trial -> Stripe Checkout -> Stripe subscription -> Stripe webhooks -> entitlement DB -> license/API validation -> premium features enabled or disabled
```

## Proposed Stripe Plans

- Solo: `$9/month`
- Team: `$19/user/month`
- Design Partner: `$49/month` flat for up to 5 users

## Proposed API Contracts

```text
POST /v1/billing/checkout
POST /v1/billing/portal
POST /v1/billing/webhooks/stripe
GET /v1/entitlements/me
POST /v1/licenses/activate
POST /v1/licenses/deactivate
```

## Hard Constraints

- No billing runtime code before approval.
- No dependency changes before approval.
- No Stripe secrets committed.
- No webhook signing secrets committed.
- No customer data committed.
- No live payment operation performed.
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
FEATURE: 014-stripe-entitlement-billing
MODE: SHIP
STATE CHANGE: spec_ready -> in_progress
```

Do not implement billing code until approval is received.
