# Tasks: 014 Stripe Entitlement Billing

Feature: `014-stripe-entitlement-billing`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Commercial Readiness

## Phase 1: Spec Gate

- [x] Close Feature 013 after approval.
- [x] Register Feature 014 as `spec_ready`.
- [x] Create requirements.
- [x] Create design.
- [x] Create tasks.
- [x] Create ADR.
- [x] Create progress artifact.
- [x] Update `progress/current.md`.
- [x] Update `progress/history.md`.
- [x] Do not implement billing code before approval.

## Phase 2: Approval Gate

- [x] Wait for explicit approval.
- [x] Move Feature 014 from `spec_ready` to approved implementation only after approval.
- [x] Do not implement before approval.

## Phase 3: Implementation Candidates

Candidate implementation scope after approval:

- [x] Create `docs/stripe-entitlement-billing.md`.
- [x] Create `.env.example` billing variables if appropriate.
- [x] Add plan-to-price mapping contract.
- [x] Add entitlement state mapping contract.
- [x] Add license key hashing contract.
- [x] Add license activation/deactivation contract.
- [x] Add webhook event idempotency contract.
- [x] Add mocked Stripe adapter contract.
- [x] Add Checkout session creation contract.
- [x] Add Customer Portal session creation contract.
- [x] Add webhook handler contract.
- [x] Add entitlement API contract.
- [x] Add tests for entitlement state mapping.
- [x] Add tests for license activation limits.
- [x] Add tests for grace-period behavior.
- [x] Add tests for webhook idempotency.
- [x] Add tests for mocked Stripe checkout and portal creation.
- [x] Add tests for subscription status to feature gating.
- [x] Preserve no live-secret rule.
- [x] Preserve no production-readiness claim.

## Phase 4: Verification Candidates

Run after implementation:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
python examples/demo_experience/run_demo.py
PYTHONPATH=src python -m unittest discover -s tests/integration
python scripts/verify_release_candidate.py
```

Manual checks:

- [x] No Stripe live secret keys are committed.
- [x] No webhook signing secret is committed.
- [x] No customer data is committed.
- [x] No production-readiness claim is introduced.
- [x] No enterprise-readiness claim is introduced.
- [x] No compliance certification claim is introduced.
- [x] No guaranteed security outcome claim is introduced.
- [x] No hosted billing service is claimed unless implemented.
- [x] No marketplace-native payment enforcement is claimed.
- [x] No PyPI publish is performed.
- [x] No git tag is created.
- [x] No GitHub Release is created.

Verification status:

- [x] `python -m json.tool feature_list.json`
- [x] `PYTHONPATH=src python -m unittest discover -s tests`
- [x] `python examples/basic_agent/run_example.py`
- [x] `python examples/demo_experience/run_demo.py`
- [x] `PYTHONPATH=src python -m unittest discover -s tests/integration`
- [x] `python scripts/verify_release_candidate.py`

## Phase 5: Review

Created after verification:

- [x] `progress/review_014-stripe-entitlement-billing.md`

Feature 014 moved to `review`, not `done`, after verification.

## Phase 6: Closure

- [x] Receive explicit closure approval.
- [x] Move Feature 014 from `review` to `done`.
- [x] Update `feature_list.json`.
- [x] Update `progress/014-stripe-entitlement-billing.md`.
- [ ] Update `progress/current.md`.
- [ ] Update `progress/history.md`.
- [x] Do not open a next feature during the closure pass.
