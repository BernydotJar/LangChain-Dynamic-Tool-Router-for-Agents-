# Design: 014 Stripe Entitlement Billing

Feature: `014-stripe-entitlement-billing`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Commercial Readiness

## Design Principle

The product should be easy to try, but paid capabilities must be controlled by a billing-backed entitlement layer.

Distribution should be public. Payment enforcement should not depend on PyPI, GitHub, VS Code Marketplace, or another install channel.

## System Shape

```text
User
  |
  v
Website / Landing Page
  |
  v
Stripe Checkout
  |
  v
Stripe Subscription
  |
  v
Stripe Webhooks
  |
  v
Billing Backend
  |
  v
Entitlement Store
  |
  v
License / Session Validation API
  |
  v
Extension / Package / Demo Premium Features
```

## Stripe Configuration

### Products

Create three products in Stripe:

```text
Runtime Tool Authorization - Solo
Runtime Tool Authorization - Team
Runtime Tool Authorization - Design Partner
```

### Prices

Create recurring monthly prices:

```text
Solo: $9/month
Team: $19/user/month
Design Partner: $49/month flat
```

### Trial

Use a 30-day subscription trial for public launch.

Design partner subscription may also use a 30-day trial unless manually arranged.

### Customer Portal

Use Stripe Customer Portal for:

- card updates,
- invoice access,
- cancellation,
- plan management,
- billing details.

Do not build a custom billing portal in the first paid version.

## Checkout Flow

```text
POST /v1/billing/checkout
```

Request:

```json
{
  "plan": "solo",
  "email": "buyer@example.com",
  "success_url": "https://example.com/billing/success",
  "cancel_url": "https://example.com/billing/cancel"
}
```

Behavior:

1. Validate requested plan.
2. Map plan to Stripe price ID from environment configuration.
3. Create Stripe Checkout Session in subscription mode.
4. Apply 30-day trial.
5. Return Checkout URL.

Response:

```json
{
  "checkout_url": "https://checkout.stripe.com/..."
}
```

## Portal Flow

```text
POST /v1/billing/portal
```

Request:

```json
{
  "customer_id": "cus_...",
  "return_url": "https://example.com/account/billing"
}
```

Behavior:

1. Resolve authenticated user to Stripe customer.
2. Create Customer Portal session.
3. Return portal URL.

## Webhook Flow

```text
POST /v1/billing/webhooks/stripe
```

Rules:

- Verify Stripe webhook signature.
- Reject events with invalid signatures.
- Process events idempotently.
- Store event IDs to prevent duplicate handling.
- Never trust client-submitted subscription status.

Required events:

- `checkout.session.completed`
- `customer.subscription.created`
- `customer.subscription.updated`
- `customer.subscription.deleted`
- `customer.subscription.trial_will_end`
- `invoice.paid`
- `invoice.payment_failed`

## Entitlement Model

Suggested tables:

```text
customers
- id
- email
- stripe_customer_id
- created_at
- updated_at

subscriptions
- id
- customer_id
- stripe_subscription_id
- stripe_price_id
- plan
- status
- trial_ends_at
- current_period_ends_at
- seat_limit
- created_at
- updated_at

licenses
- id
- customer_id
- license_key_hash
- status
- plan
- seat_limit
- expires_at
- created_at
- updated_at

license_activations
- id
- license_id
- machine_fingerprint_hash
- user_label
- activated_at
- last_seen_at

gateway_events
- id
- provider
- provider_event_id
- event_type
- processed_at
- payload_hash

entitlement_audit_events
- id
- customer_id
- subscription_id
- license_id
- action
- reason
- metadata_json
- created_at
```

## Entitlement API

```text
GET /v1/entitlements/me
```

Request authentication options:

- license key,
- signed session token,
- future account login.

Response:

```json
{
  "status": "active",
  "plan": "team",
  "seat_limit": 5,
  "features": [
    "policy_profiles",
    "team_config",
    "audit_export"
  ],
  "trial_ends_at": null,
  "current_period_ends_at": "2026-08-05T00:00:00Z",
  "grace_until": null
}
```

## License Activation

```text
POST /v1/licenses/activate
```

Request:

```json
{
  "license_key": "rtai_live_...",
  "machine_fingerprint": "hashed-device-or-install-id",
  "user_label": "Eduardo MacBook Pro"
}
```

Rules:

- Store only license key hashes.
- Store only hashed machine fingerprints.
- Enforce seat or activation limits.
- Return entitlement summary.
- Allow revocation or deactivation.

## Access Mapping

```text
trialing -> premium enabled
active -> premium enabled
past_due -> premium enabled during grace period, then downgrade
canceled -> premium disabled
unpaid -> premium disabled
missing -> premium disabled
```

## Offline Grace Period

Allow a short offline grace period to avoid breaking demos.

Recommended behavior:

```text
Online active entitlement -> premium enabled
Offline with recently validated entitlement -> premium enabled for 72 hours
Expired/canceled/missing entitlement -> premium disabled
```

## Secret Handling

Do not commit:

- Stripe secret keys,
- webhook signing secrets,
- live price IDs if the repo is public and environment separation is needed,
- license signing secrets,
- customer data.

Use environment variables:

```text
STRIPE_SECRET_KEY
STRIPE_WEBHOOK_SECRET
STRIPE_PRICE_SOLO_MONTHLY
STRIPE_PRICE_TEAM_MONTHLY
STRIPE_PRICE_DESIGN_PARTNER_MONTHLY
BILLING_SUCCESS_URL
BILLING_CANCEL_URL
LICENSE_KEY_PEPPER
```

## Feature Flags

Premium gates should map entitlements to features:

```text
policy_profiles
team_config
team_seats
design_partner_support
hosted_policy_api_future
hosted_audit_export_future
```

Future enterprise-only capabilities must remain disabled unless explicitly implemented later.

## Testing Strategy

Unit tests:

- plan to price mapping,
- entitlement state mapping,
- license key hashing,
- activation limit enforcement,
- grace-period calculation,
- webhook idempotency.

Integration or contract tests:

- Checkout session creation with mocked Stripe client,
- Customer Portal session creation with mocked Stripe client,
- webhook signature verification path,
- subscription update changes entitlement,
- failed invoice changes entitlement state,
- canceled subscription disables entitlement.

Manual checks:

- no live secrets committed,
- no production readiness claim,
- no dependency changes before approval,
- no payment enforcement by marketplace install.

## Implementation Phasing

Recommended implementation after approval:

1. Add billing docs and environment template.
2. Add entitlement contracts and pure mapping logic.
3. Add mocked Stripe adapter layer.
4. Add webhook handler contract.
5. Add license validation logic.
6. Add tests.
7. Only then wire into a real web backend or extension surface.

## Constraints

Spec gate only. Do not implement billing runtime code until explicit approval.
