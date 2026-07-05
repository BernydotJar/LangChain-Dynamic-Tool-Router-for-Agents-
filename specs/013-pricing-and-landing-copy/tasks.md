# Tasks: 013 Pricing And Landing Copy

Feature: `013-pricing-and-landing-copy`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Commercial Readiness

## Phase 1: Spec Gate

- [x] Create requirements.
- [x] Create design.
- [x] Create tasks.
- [x] Create ADR.
- [x] Create progress artifact.
- [x] Register Feature 013 as `spec_ready`.
- [x] Update `progress/current.md`.
- [x] Update `progress/history.md`.
- [x] Do not implement pricing copy before approval.

## Phase 2: Approval Gate

- [x] Wait for explicit human approval.
- [x] Move Feature 013 from `spec_ready` to approved implementation only after approval.
- [x] Do not implement before approval.

## Phase 3: Implementation Candidates

Implementation scope after approval:

- [x] Create `docs/pricing.md`.
- [x] Add concise README pricing section after `Design Partner Signal` and before `Harness SDLC Evidence`.
- [x] Add README link to `docs/pricing.md`.
- [x] Update README roadmap if needed.
- [x] Update `docs/design-partner-kit.md` with the first-20 design partner offer.
- [x] Include 30-day free trial.
- [x] Include Solo `$9/month`.
- [x] Include Team `$19/user/month`.
- [x] Include Design Partner `$49/month` flat for up to 5 users.
- [x] Include 12-month founding price lock.
- [x] Include Custom Enterprise future/custom scope.
- [x] Include the category contrast copy.
- [x] Include the hero copy.
- [x] Include the pricing CTA.
- [x] Include the design partner CTA.
- [x] Include the premium AI developer-tool seat value anchor.
- [x] Add monetization architecture for trial, billing, entitlement, license/API validation, and grace-period behavior.
- [x] Avoid unsupported production, enterprise, compliance, and security claims.

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

- [ ] README link to `docs/pricing.md` resolves.
- [ ] `docs/pricing.md` exists.
- [ ] `docs/design-partner-kit.md` includes the design partner offer.
- [ ] Pricing preserves developer-preview maturity.
- [ ] Enterprise section is explicitly future/custom scope.
- [ ] No production-readiness claim is introduced.
- [ ] No enterprise-readiness claim is introduced.
- [ ] No compliance certification claim is introduced.
- [ ] No guaranteed security outcome claim is introduced.
- [ ] No runtime behavior changed unless explicitly approved.
- [ ] No dependency changes were introduced.
- [ ] No release action was performed.

Verification status:

- [ ] `python -m json.tool feature_list.json`
- [ ] `PYTHONPATH=src python -m unittest discover -s tests`
- [ ] `python examples/basic_agent/run_example.py`
- [ ] `python examples/demo_experience/run_demo.py`
- [ ] `PYTHONPATH=src python -m unittest discover -s tests/integration`
- [ ] `python scripts/verify_release_candidate.py`

## Phase 5: Review

Create after verification:

- [ ] `progress/review_013-pricing-and-landing-copy.md`

Move Feature 013 to `review`, not `done`, after verification.
