# 015 Billing Provider Abstraction Progress

Feature: `015-billing-provider-abstraction`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Commercial Readiness

## State

Status: `spec_ready`

## Summary

Feature 015 is opened as a spec gate to make the commercial entitlement layer provider-agnostic.

The goal is to preserve Feature 014 entitlement work while reframing Stripe as one optional adapter rather than the only billing path.

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
- Feature 014: `done`

## Spec Artifacts

Created:

- `specs/015-billing-provider-abstraction/requirements.md`
- `specs/015-billing-provider-abstraction/design.md`
- `specs/015-billing-provider-abstraction/tasks.md`
- `adr/015-billing-provider-abstraction.md`

## Current Scope

Spec only.

No runtime implementation has been approved or added.

## Key Direction

Provider paths to support conceptually:

- Stripe adapter, optional and region-dependent.
- Manual license provider for developer preview and design partners.
- Merchant-of-record provider as future adapter path.
- Local gateway provider as future adapter path.

## Constraints

- Do not implement runtime provider abstraction before approval.
- Do not add new provider dependencies before approval.
- Do not add private provider configuration values.
- Do not claim production billing readiness.
- Do not claim unsupported country or region support.
- Do not provide legal, tax, or accounting advice.
- Do not publish to PyPI.
- Do not create a git tag.
- Do not create a GitHub Release.

## Next Valid Lifecycle Action

Explicit approval:

```text
APPROVAL TO IMPLEMENT
FEATURE: 015-billing-provider-abstraction
MODE: SHIP
STATE CHANGE: spec_ready -> in_progress
```
