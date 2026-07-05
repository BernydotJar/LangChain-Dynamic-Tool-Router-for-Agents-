# Design: 015 Billing Provider Abstraction

Feature: `015-billing-provider-abstraction`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Commercial Readiness

## Decision

Move the commercial architecture from Stripe-first wording to a provider-agnostic billing boundary.

Stripe remains an adapter option, but the core product should expose entitlement concepts that can be backed by multiple provider paths.

## Design Principles

- Entitlement is core.
- Payment provider is replaceable.
- Stripe is optional.
- Manual licenses are first-class for developer preview.
- Provider limitations must be explicit.
- No production billing claim without production-grade provider integration.
- No country or region support claim without source-backed validation.

## Conceptual Architecture

```text
AI Product / CLI / SaaS
        |
        v
Billing Provider Boundary
        |
        +-- Stripe adapter, optional and region-dependent
        +-- Merchant-of-record adapter, future
        +-- Local gateway adapter, future
        +-- Manual license adapter, developer-preview path
        |
        v
Entitlement Resolver
        |
        v
Runtime Tool Authorization
        |
        v
Premium tool policy / plan gates
```

## Proposed Provider Contract

A future implementation should define a protocol-like boundary similar to:

```python
class BillingProvider:
    name: str
    capabilities: BillingProviderCapabilities

    def create_checkout_session(self, request): ...
    def create_customer_management_session(self, request): ...
    def parse_event(self, payload, headers): ...
    def resolve_entitlement(self, provider_record): ...
```

The exact names can change during implementation, but the boundary should keep provider behavior separate from entitlement behavior.

## Provider Capabilities

A provider capability model should describe:

```text
supports_subscriptions
supports_one_time_payments
supports_trials
supports_customer_portal
supports_webhooks
supports_merchant_of_record
supports_local_payment_methods
requires_supported_merchant_country
supports_manual_activation
```

This keeps README and docs honest when a provider cannot be used directly from the seller's legal country or region.

## Provider Paths

### Stripe Provider

Purpose:

- optional adapter path,
- useful when the merchant has a supported legal country or region,
- useful for local testing through CLI and webhook mocks,
- not assumed as globally available.

Developer-preview status:

- mock-safe only,
- no live SDK dependency unless separately approved,
- no live credential material,
- no live payment operations.

### Manual License Provider

Purpose:

- developer preview,
- design partners,
- bank transfer or invoice-based activation,
- testing entitlement flows without a payment processor.

Required behaviors:

- issue license records,
- enforce activation limits,
- map license status to entitlement,
- carry expiration or renewal metadata,
- preserve auditability.

### Merchant-of-Record Provider

Purpose:

- future path for cross-border SaaS payments where the provider handles merchant-of-record responsibilities.

Developer-preview status:

- documentation placeholder only unless approved.

### Local Gateway Provider

Purpose:

- future path for local payment processors in specific markets.

Developer-preview status:

- documentation placeholder only unless approved.

## Entitlement State Model

Keep the Feature 014 entitlement model, but ensure it is not Stripe-shaped.

Provider states should normalize into internal states such as:

```text
trialing
active
past_due
canceled
unpaid
missing
manual_active
manual_expired
```

The final state names can be refined during implementation.

## Documentation Impact

README should be updated to say:

- Feature 014 is done,
- Feature 015 is a spec gate,
- Stripe billing is optional and region-dependent,
- entitlement-backed access is provider-agnostic,
- manual license activation is the practical developer-preview fallback.

Existing `docs/stripe-entitlement-billing.md` should eventually be reframed as a Stripe adapter document or cross-linked from a provider abstraction document.

## Verification Strategy

Spec gate verification:

```sh
python -m json.tool feature_list.json
```

Implementation verification after approval should include:

```sh
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
python examples/demo_experience/run_demo.py
PYTHONPATH=src python -m unittest discover -s tests/integration
python scripts/verify_release_candidate.py
```

## Risk Controls

- No implementation before approval.
- No live payment provider dependencies before approval.
- No live credential material.
- No unsupported country or region payment claim.
- No production billing claim.
- No tax or legal advice claim.
