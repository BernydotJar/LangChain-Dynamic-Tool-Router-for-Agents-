# ADR 014: Stripe Entitlement Billing

Feature: `014-stripe-entitlement-billing`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Status: Proposed

## Context

Feature 013 established the public pricing model:

- 30-day free trial.
- Solo: `$9/month`.
- Team: `$19/user/month`.
- Design Partner: `$49/month` flat for up to 5 users.
- Enterprise: custom future/custom scope.

The next gap is implementation strategy for letting people install and evaluate the product first, then charging after trial or subscription activation.

Marketplace install gating is the wrong enforcement layer because the product may be distributed through multiple channels, including GitHub, PyPI, VS Code, local demos, and future hosted surfaces.

## Decision

Use Stripe for billing and a product-owned entitlement layer for access control.

The paid access model is:

```text
public install -> 30-day trial -> Stripe Checkout -> Stripe subscription -> Stripe webhooks -> entitlement DB -> license/API validation -> premium features enabled or disabled
```

Distribution remains public. Premium feature access is controlled by entitlement.

## Stripe Responsibilities

Stripe owns:

- Checkout,
- recurring subscription billing,
- trial period tracking,
- invoice payment status,
- customer billing portal,
- subscription lifecycle events.

## Product Backend Responsibilities

The product backend owns:

- plan-to-price mapping,
- webhook verification,
- webhook idempotency,
- entitlement records,
- license key hashing,
- activation limits,
- entitlement API responses,
- premium feature gating,
- grace-period behavior.

## Entitlement Rules

```text
trialing -> premium enabled
active -> premium enabled
past_due -> premium enabled during grace period, then downgrade
canceled -> premium disabled
unpaid -> premium disabled
missing -> premium disabled
```

## Security Rules

Do not commit:

- Stripe secret keys,
- webhook signing secrets,
- live customer data,
- license key signing secrets,
- raw license keys,
- raw machine fingerprints.

Store hashes for license keys and machine fingerprints.

## Rationale

This keeps the install experience low-friction while allowing paid access to be enforced consistently across distribution channels.

Stripe is used for money movement and subscription lifecycle. The product owns entitlements because only the product understands which capabilities map to plans.

A 72-hour offline grace period preserves a good developer experience for demos and travel without making local state the source of truth.

## Consequences

Positive:

- Users can try before paying.
- Billing is handled by Stripe instead of custom payment code.
- Premium access can be enforced outside marketplaces.
- Future hosted features can reuse the same entitlement layer.

Tradeoffs:

- Requires a backend service.
- Requires webhook security and idempotency.
- Requires entitlement persistence.
- Requires careful messaging around developer-preview maturity.

## Status

Spec gate only. No billing runtime code should be implemented until explicit approval.
