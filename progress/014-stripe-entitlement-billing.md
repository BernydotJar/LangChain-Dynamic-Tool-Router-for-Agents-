# 014 Stripe Entitlement Billing Progress

Feature: `014-stripe-entitlement-billing`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Commercial Readiness

## State

Status: `review`

## Summary

Feature 014 is in review after explicit approval, implementation, and successful release-candidate verification.

Implementation added mock-safe Stripe entitlement billing contracts, documentation, environment placeholders, package exports, and tests.

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

## Implemented

- Registered Feature 014 as `in_progress`.
- Created `src/tool_policy_router/billing.py`.
- Exported billing contracts from `src/tool_policy_router/__init__.py`.
- Created `tests/test_billing.py`.
- Created `docs/stripe-entitlement-billing.md`.
- Created `.env.example` with safe placeholders only.
- Updated README documentation index, developer-preview boundary, roadmap, and billing references.
- Added plan-to-price mapping contract.
- Added Checkout session creation contract.
- Added Customer Portal session creation contract.
- Added mock Stripe gateway.
- Added entitlement state mapping.
- Added premium feature mapping by plan.
- Added license key hashing and machine fingerprint hashing.
- Added in-memory license activation/deactivation store.
- Added webhook event idempotency store.
- Added webhook payload hashing.
- Added tests for Checkout, Portal, entitlement states, grace period, license activation, activation limits, deactivation, and webhook idempotency.

## Billing Flow

```text
public install -> 30-day trial -> Stripe Checkout -> Stripe subscription -> Stripe webhooks -> entitlement DB -> license/API validation -> premium features enabled or disabled
```

## Hard Constraints Preserved

- No real Stripe SDK dependency was added.
- No dependency changes were made.
- No Stripe live secret keys were committed.
- No webhook signing secret was committed.
- No customer data was committed.
- No live payment operation was performed.
- No PyPI publish.
- No git tag.
- No GitHub Release.
- No production-readiness claim.
- No enterprise-readiness claim.
- No compliance certification claim.
- No guaranteed security outcome claim.

## Verification

Automated verification passed after implementation.

Passed:

- `python -m json.tool feature_list.json`
- `PYTHONPATH=src python -m unittest discover -s tests`
- `python examples/basic_agent/run_example.py`
- `python examples/demo_experience/run_demo.py`
- `PYTHONPATH=src python -m unittest discover -s tests/integration`
- `python scripts/verify_release_candidate.py`

Release-candidate verifier evidence:

- basic demo: PASS
- guided demo: PASS
- integration tests: PASS, ran 2 tests, skipped 2
- editable install: PASS
- editable install with dev extra: PASS
- package build: PASS
- release-candidate verification completed

Known non-blocking warning:

- Setuptools emitted license metadata deprecation warnings during package build. These remain a documented follow-up and did not block the build.

## Review Artifact

Created:

```text
progress/review_014-stripe-entitlement-billing.md
```

## Next Valid Lifecycle Action

Human closure approval:

```text
APPROVAL TO CLOSE
FEATURE: 014-stripe-entitlement-billing
MODE: SHIP
STATE CHANGE: review -> done
```

Do not close Feature 014 until explicit human closure approval is received.
