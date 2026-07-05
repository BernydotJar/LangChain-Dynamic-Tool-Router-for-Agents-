# Tasks: 015 Billing Provider Abstraction

Feature: `015-billing-provider-abstraction`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Commercial Readiness

## Phase 1: Spec Gate

- [x] Close Feature 014 after approval.
- [x] Register Feature 015 as `spec_ready`.
- [x] Create requirements.
- [x] Create design.
- [x] Create tasks.
- [x] Create ADR.
- [x] Create progress artifact.
- [x] Update README roadmap and billing language.
- [x] Update `progress/current.md`.
- [x] Update `progress/history.md`.
- [x] Do not implement runtime provider abstraction before approval.

## Phase 2: Approval Gate

- [ ] Wait for explicit approval.
- [ ] Move Feature 015 from `spec_ready` to implementation only after approval.
- [ ] Do not implement before approval.

## Phase 3: Implementation Candidates

Candidate implementation scope after approval:

- [ ] Create provider capability model.
- [ ] Create provider-neutral billing interface.
- [ ] Refactor Stripe-specific naming into an optional adapter boundary.
- [ ] Add manual license provider path.
- [ ] Add unsupported provider fallback behavior.
- [ ] Add provider registry or selector.
- [ ] Add provider-neutral entitlement mapping.
- [ ] Add tests for provider capabilities.
- [ ] Add tests for manual license provider behavior.
- [ ] Add tests for unsupported provider behavior.
- [ ] Add tests proving Stripe remains mock-safe.
- [ ] Update docs to distinguish entitlement core from billing provider adapters.
- [ ] Preserve no live charge operation.
- [ ] Preserve no production billing claim.

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

- [ ] No private billing configuration is committed.
- [ ] No customer data is committed.
- [ ] No production-readiness claim is introduced.
- [ ] No enterprise-readiness claim is introduced.
- [ ] No compliance certification claim is introduced.
- [ ] No tax or legal advice claim is introduced.
- [ ] No unsupported country or region support claim is introduced.
- [ ] No PyPI publish is performed.
- [ ] No git tag is created.
- [ ] No GitHub Release is created.

## Phase 5: Review

Create after verification:

- [ ] `progress/review_015-billing-provider-abstraction.md`
