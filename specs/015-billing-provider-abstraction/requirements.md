# Requirements: 015 Billing Provider Abstraction

Feature: `015-billing-provider-abstraction`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Commercial Readiness

## Context

Feature 014 added mock-safe Stripe entitlement billing contracts.

After review, the commercial architecture needs to avoid treating Stripe as the only payment path because Stripe Payments availability depends on the legal country or region of the merchant account.

Stripe should remain one optional adapter, not the core billing assumption.

## Problem

The current wording and implementation shape can be interpreted as Stripe-first billing.

That is too narrow for founders, design partners, and technical users in unsupported Stripe merchant countries or regions.

The project needs a provider-agnostic entitlement layer that can support:

- Stripe where legally and commercially available,
- merchant-of-record providers,
- local payment gateways,
- manual invoice or bank-transfer license activation,
- future provider adapters without changing the authorization core.

## Goals

- Define a provider-neutral billing abstraction.
- Preserve the existing entitlement and license concepts from Feature 014.
- Reframe Stripe as an optional adapter.
- Support manual license activation as a first-class developer-preview path.
- Support merchant-of-record and local gateway paths as future adapters.
- Avoid committing to any single payment processor as production-ready.
- Avoid adding live payment dependencies before approval.
- Avoid adding real payment credentials, webhook secrets, or customer data.

## Non-Goals

- Do not process live payments.
- Do not add real Stripe SDK integration.
- Do not add merchant-of-record SDK integration.
- Do not add PayU, Wompi, or other local gateway SDK integration.
- Do not add tax, accounting, invoicing, or legal advice.
- Do not claim Colombia, Guatemala, or any other unsupported merchant region can use Stripe Payments directly.
- Do not publish to PyPI.
- Do not create a git tag.
- Do not create a GitHub Release.

## Functional Requirements

### FR-1 Provider Interface

Define a provider-neutral billing boundary that can represent:

- checkout/session creation,
- customer portal or customer management URL creation,
- webhook/event ingestion,
- subscription or license status mapping,
- entitlement resolution,
- provider capability metadata.

### FR-2 Provider Capability Model

Each provider path should be able to describe capabilities such as:

- supports subscriptions,
- supports one-time payments,
- supports trials,
- supports customer portal,
- supports webhooks,
- supports merchant-of-record behavior,
- supports local payment methods,
- requires supported merchant country or region,
- supports manual activation.

### FR-3 Stripe Adapter Reframe

Stripe must be documented and modeled as:

- optional,
- region-dependent,
- mock-safe in developer preview,
- not a guaranteed global merchant path.

### FR-4 Manual License Provider

Manual license activation must be treated as a real provider path for developer preview and design partners.

It should support:

- manually issued license keys,
- plan selection,
- activation limits,
- expiration or renewal date metadata,
- entitlement mapping,
- audit-friendly state.

### FR-5 Merchant-of-Record Provider Placeholder

The architecture should support a future merchant-of-record provider without naming it as implemented.

The provider path should be able to support:

- external checkout,
- entitlement webhook mapping,
- provider-managed tax/payment handling,
- customer portal or management links if available.

### FR-6 Local Gateway Provider Placeholder

The architecture should support a future local gateway provider without naming it as implemented.

The provider path should be able to support:

- local checkout URLs,
- local payment reference metadata,
- asynchronous payment confirmation,
- manual reconciliation fallback.

### FR-7 Documentation Update

Update README and docs language so the project says:

- entitlement-backed billing layer,
- provider-agnostic billing boundary,
- Stripe adapter is optional,
- manual license path is valid during developer preview,
- no production billing claim.

### FR-8 Test Strategy

If implementation is approved, add tests for:

- provider capability metadata,
- provider registry selection,
- manual license provider behavior,
- unsupported provider behavior,
- entitlement mapping independent of provider,
- Stripe adapter remaining mock-safe.

## Acceptance Criteria

- Feature 015 registered as `spec_ready`.
- Requirements, design, tasks, ADR, and progress artifacts created.
- README reflects Feature 014 as closed and Feature 015 as spec-ready.
- No runtime implementation added before approval.
- No new dependency added before approval.
- No live payment provider is presented as production-ready.
- No country-specific payment support is claimed beyond source-backed availability statements.
