# Stripe Entitlement Billing

Runtime Tool Authorization should be easy to install and evaluate, but paid capabilities should be controlled by a billing-backed entitlement layer.

This guide describes the developer-preview implementation contract. It does not claim production billing readiness.

## Billing Flow

```text
public install -> 30-day trial -> Stripe Checkout -> Stripe subscription -> Stripe webhooks -> entitlement DB -> license/API validation -> premium features enabled or disabled
```

## Plans

| Plan | Price | Seat Limit | Trial | Premium Use |
|---|---:|---:|---:|---|
| Solo | `$9/month` | 1 | 30 days | Individual evaluation and local policy profiles. |
| Team | `$19/user/month` | 1 per paid user | 30 days | Team configuration, team seats, and shared evaluation. |
| Design Partner | `$49/month` flat | 5 | 30 days unless manually arranged | First 20 qualified design partners. |
| Enterprise | Custom | Custom | Custom | Future/custom scope only. |

## Stripe Dashboard Setup

Create three recurring monthly prices in Stripe:

```text
Runtime Tool Authorization - Solo
Runtime Tool Authorization - Team
Runtime Tool Authorization - Design Partner
```

Store price IDs in environment variables:

```text
STRIPE_PRICE_SOLO_MONTHLY
STRIPE_PRICE_TEAM_MONTHLY
STRIPE_PRICE_DESIGN_PARTNER_MONTHLY
```

Do not commit live keys, webhook signing secrets, customer data, or raw license keys.

## Required API Contracts

```text
POST /v1/billing/checkout
POST /v1/billing/portal
POST /v1/billing/webhooks/stripe
GET /v1/entitlements/me
POST /v1/licenses/activate
POST /v1/licenses/deactivate
```

## Checkout Contract

Input:

```json
{
  "plan": "solo",
  "email": "buyer@example.com",
  "success_url": "https://example.com/billing/success",
  "cancel_url": "https://example.com/billing/cancel"
}
```

Output:

```json
{
  "checkout_url": "https://checkout.stripe.com/..."
}
```

The developer-preview package includes a mockable contract for Checkout session creation. It intentionally does not include the Stripe SDK as a required dependency.

## Portal Contract

Input:

```json
{
  "stripe_customer_id": "cus_...",
  "return_url": "https://example.com/account/billing"
}
```

Output:

```json
{
  "portal_url": "https://billing.stripe.com/..."
}
```

## Webhook Contract

Required events:

- `checkout.session.completed`
- `customer.subscription.created`
- `customer.subscription.updated`
- `customer.subscription.deleted`
- `customer.subscription.trial_will_end`
- `invoice.paid`
- `invoice.payment_failed`

Rules:

- Verify Stripe webhook signatures in the real backend.
- Process events idempotently.
- Store provider event IDs.
- Never trust client-submitted subscription status.
- Never store raw webhook secrets in source control.

## Entitlement Mapping

```text
trialing -> premium enabled
active -> premium enabled
past_due -> premium enabled during grace period, then downgrade
canceled -> premium disabled
unpaid -> premium disabled
missing -> premium disabled
```

The developer-preview contract uses a 72-hour grace period for `past_due` states.

## License Activation

License keys and machine fingerprints should be hashed before storage.

Rules:

- Store only license key hashes.
- Store only machine fingerprint hashes.
- Enforce activation limits by plan.
- Refresh an existing activation when the same machine checks in again.
- Allow activation deactivation.

## Premium Feature Gates

Premium features are represented as entitlement feature flags:

```text
policy_profiles
team_config
team_seats
design_partner_support
hosted_policy_api_future
hosted_audit_export_future
```

Future hosted or enterprise-only features remain flags only until explicitly implemented.

## Developer-Preview Boundary

This feature adds mock-safe billing and entitlement contracts. It does not provide:

- production billing service,
- hosted account system,
- Stripe SDK integration,
- real webhook signature verification,
- tax or accounting completeness,
- production IAM,
- compliance certification.

## Verification

Run:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
python examples/demo_experience/run_demo.py
PYTHONPATH=src python -m unittest discover -s tests/integration
python scripts/verify_release_candidate.py
```
