# ADR 015: Billing Provider Abstraction

Feature: `015-billing-provider-abstraction`

Status: Proposed

Mode: SHIP

## Context

Feature 014 introduced mock-safe Stripe entitlement billing contracts.

Stripe is useful for testing and for supported merchant countries or regions, but it should not be the only billing assumption for this product.

The core business requirement is entitlement-backed access, not Stripe-specific payment processing.

## Decision

Adopt a provider-agnostic billing architecture.

The project should treat Stripe as one optional provider adapter. Manual license activation, merchant-of-record providers, and local gateway providers should be valid architecture paths.

## Consequences

Positive:

- Keeps entitlement logic independent of payment-provider availability.
- Supports users in regions where Stripe Payments is not directly available for their merchant entity.
- Preserves the Feature 014 work as a Stripe-compatible adapter foundation.
- Enables design partner access without live payment integration.
- Avoids overclaiming production billing readiness.

Negative:

- Adds abstraction complexity.
- Requires clearer provider capability metadata.
- May delay production payment integration until provider strategy is selected.

## Constraints

- No runtime implementation before approval.
- No live provider dependency before approval.
- No live payment operation.
- No unsupported country or region support claim.
- No legal, tax, or accounting advice claim.
- No production billing claim.

## Accepted Direction

Use Feature 015 as a spec gate to reframe the commercial architecture before implementing additional billing runtime code.
