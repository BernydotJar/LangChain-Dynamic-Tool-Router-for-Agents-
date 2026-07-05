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

- [ ] Wait for explicit approval.
- [ ] Move Feature 014 from `spec_ready` to approved implementation only after approval.
- [ ] Do not implement before approval.

## Phase 3: Implementation Candidates

Candidate implementation scope after approval:

- [ ] Create `docs/stripe-entitlement-billing.md`.
- [ ] Create `.env.example` billing variables if appropriate.
- [ ] Add plan-to-price mapping contract.
- [ ] Add entitlement state mapping contract.
- [ ] Add license key hashing contract.
- [ ] Add license activation/deactivation contract.
- [ ] Add webhook event idempotency contract.
- [ ] Add mocked Stripe adapter contract.
- [ ] Add Checkout session creation contract.
- [ ] Add Customer Portal session creation contract.
- [ ] Add webhook handler contract.
- [ ] Add entitlement API contract.
- [ ] Add tests for entitlement state mapping.
- [ ] Add tests for license activation limits.
- [ ] Add tests for grace-period behavior.
- [ ] Add tests for webhook idempotency.
- [ ] Add tests for mocked Stripe checkout and portal creation.
- [ ] Add tests for subscription status to feature gating.
- [ ] Preserve no live-secret rule.
- [ ] Preserve no production-readiness claim.

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

- [ ] No Stripe live secret keys are committed.
- [ ] No webhook signing secret is committed.
- [ ] No customer data is committed.
- [ ] No production-readiness claim is introduced.
- [ ] No enterprise-readiness claim is introduced.
- [ ] No compliance certification claim is introduced.
- [ ] No guaranteed security outcome claim is introduced.
- [ ] No hosted billing service is claimed unless implemented.
- [ ] No marketplace-native payment enforcement is claimed.
- [ ] No PyPI publish is performed.
- [ ] No git tag is created.
- [ ] No GitHub Release is created.

Verification status:

- [ ] `python -m json.tool feature_list.json`
- [ ] `PYTHONPATH=src python -m unittest discover -s tests`
- [ ] `python examples/basic_agent/run_example.py`
- [ ] `python examples/demo_experience/run_demo.py`
- [ ] `PYTHONPATH=src python -m unittest discover -s tests/integration`
- [ ] `python scripts/verify_release_candidate.py`

## Phase 5: Review

Create after verification:

- [ ] `progress/review_014-stripe-entitlement-billing.md`

Move Feature 014 to `review`, not `done`, after verification.
