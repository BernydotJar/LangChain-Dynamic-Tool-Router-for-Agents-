# 013 Pricing And Landing Copy Progress

Feature: `013-pricing-and-landing-copy`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Commercial Readiness

## State

Status: `done`

## Summary

Feature 013 is closed as `done` after explicit approval, implementation, successful release-candidate verification, review artifact creation, and closure approval.

Implementation added pricing, trial, design partner offer, and monetization architecture documentation.

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

## Spec Artifacts

Created:

- `specs/013-pricing-and-landing-copy/requirements.md`
- `specs/013-pricing-and-landing-copy/design.md`
- `specs/013-pricing-and-landing-copy/tasks.md`
- `adr/013-pricing-and-landing-copy-strategy.md`

## Implemented

- Registered Feature 013 as `in_progress` before implementation.
- Created `docs/pricing.md`.
- Added README pricing section after `Design Partner Signal` and before `Harness SDLC Evidence`.
- Added README link to `docs/pricing.md`.
- Updated README roadmap to show Feature 013 as `in progress` during implementation.
- Updated `docs/design-partner-kit.md` with the first-20 design partner offer.
- Added the `$49/month` flat design partner offer for up to 5 users.
- Added 12-month founding price lock language.
- Added 30-day free trial, `$9/month` Solo, and `$19/user/month` Team pricing.
- Added monetization architecture: public install, Stripe billing, entitlement backend, license validation, and grace-period behavior.

## Monetization Decision

Do not rely on marketplace install gating for payment enforcement.

Use this model:

```text
public install -> 30-day trial -> Stripe billing -> entitlement backend -> license/API validation -> premium features enabled or disabled
```

Developer-preview local examples can remain free. Commercial or team capabilities should require an active entitlement.

## Hard Constraints Preserved

- No runtime code changes.
- No dependency changes.
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

- unit tests: PASS, ran 23 tests, skipped 2
- basic demo: PASS
- guided demo: PASS
- integration tests: PASS, ran 2 tests, skipped 2
- editable install: PASS
- editable install with dev extra: PASS
- package build: PASS

Known non-blocking warning:

- Setuptools emitted license metadata deprecation warnings during package build. These remain a documented follow-up and did not block the build.

## Review Artifact

Created:

```text
progress/review_013-pricing-and-landing-copy.md
```

## Closure

Closure approval received.

Feature 013 moved from `review` to `done`.

Accepted limitations:

- No runtime code changes.
- No dependency changes.
- No PyPI publish.
- No git tag.
- No GitHub Release.
- No production-readiness claim.
- No enterprise-readiness claim.
- No compliance certification claim.
- No guaranteed security outcome claim.
- Setuptools license metadata warnings remain a documented follow-up.

## Next Feature

Feature 014 opened as a spec gate:

```text
014-stripe-entitlement-billing
```
