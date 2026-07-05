# Requirements: 014 Stripe Entitlement Billing

Feature: `014-stripe-entitlement-billing`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Commercial Readiness

## Objective

Define the implementation contract for paid access to Runtime Tool Authorization for AI Agents using Stripe subscriptions, 30-day free trials, billing webhooks, entitlement storage, license validation, and premium feature gating.

This feature should turn the pricing architecture from Feature 013 into an implementation-ready billing system design.

## Scope

Feature 014 should prepare the repo for billing infrastructure implementation.

Required scope:

- Stripe product and price mapping.
- 30-day free trial flow.
- Stripe Checkout flow.
- Stripe Customer Portal flow.
- Stripe webhook event handling contract.
- Entitlement data model.
- License key validation contract.
- Premium feature gating behavior.
- Offline grace-period behavior.
- Local developer-preview fallback behavior.
- Security and secret-handling rules.
- Test strategy.
- Operational checklist.

## Required Plans

Public launch:

- Solo: `$9/month`.
- Team: `$19/user/month`.

Design partner:

- `$49/month` flat for up to 5 users.
- First 20 design partners only.
- Founding price locked for 12 months.

Enterprise:

- Custom future/custom scope only.

## Required Billing Flow

```text
public install -> 30-day trial -> Stripe Checkout -> Stripe subscription -> webhook receiver -> entitlement DB -> license/API validation -> premium features enabled or disabled
```

## Required Stripe Events

At minimum, implementation should handle:

- `checkout.session.completed`
- `customer.subscription.created`
- `customer.subscription.updated`
- `customer.subscription.deleted`
- `customer.subscription.trial_will_end`
- `invoice.paid`
- `invoice.payment_failed`

## Required Entitlement States

The entitlement layer should map Stripe state to product access:

- `trialing` -> premium enabled.
- `active` -> premium enabled.
- `past_due` -> premium enabled during grace period, then warning or downgrade.
- `canceled` -> premium disabled.
- `unpaid` -> premium disabled.
- missing entitlement -> premium disabled.

## Required API Contracts

Create contracts for:

```text
POST /v1/billing/checkout
POST /v1/billing/portal
POST /v1/billing/webhooks/stripe
GET /v1/entitlements/me
POST /v1/licenses/activate
POST /v1/licenses/deactivate
```

No production API implementation should happen before explicit approval.

## Required Data Model

Define a minimal data model for:

- customers,
- subscriptions,
- licenses,
- license activations,
- entitlement audit events.

## Required Feature Gating

Free or local developer-preview usage may include:

- local demo,
- JSON policy examples,
- request-time authorization demo,
- fallback behavior,
- local audit evidence export.

Premium usage should gate:

- multiple saved policy profiles,
- team configuration,
- team seat management,
- design partner support workflow,
- future hosted policy API access,
- future hosted audit export.

## Non-Goals

Do not implement or claim:

- production-ready billing system,
- enterprise SSO,
- hosted policy API availability,
- compliance workflows,
- audit retention service,
- tax/legal accounting completeness,
- marketplace-native payment enforcement,
- production IAM replacement.

## Acceptance Criteria

- Feature 014 is registered as `spec_ready`.
- Requirements, design, tasks, ADR, and progress artifacts exist.
- Stripe implementation contract is clear enough for coding.
- Entitlement states and API contracts are explicit.
- Secret handling rules are documented.
- No runtime billing code is implemented before approval.
- No dependencies are added before approval.
- No Stripe secrets or live keys are committed.
- Feature 013 remains `done`.
