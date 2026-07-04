# Tasks: 012 Design Partner Kit

Feature: `012-design-partner-kit`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Design Partner Readiness

## Phase 1: Spec Gate

- [x] Create requirements.
- [x] Create design.
- [x] Create tasks.
- [ ] Create ADR.
- [ ] Create progress artifact.
- [ ] Register Feature 012 as `spec_ready`.
- [ ] Update `progress/current.md`.
- [ ] Update `progress/history.md`.
- [ ] Confirm `docs/design-partner-kit.md` was not created.

## Phase 2: Approval Gate

- [ ] Wait for explicit human approval.
- [ ] Move Feature 012 from `spec_ready` to `approved` only after approval.
- [ ] Do not implement before approval.

## Phase 3: Implementation Candidates

Implementation scope should be confirmed after approval. Candidate tasks:

- [ ] Create `docs/design-partner-kit.md`.
- [ ] Define ideal design partner profile.
- [ ] Define buyer personas and evaluator roles.
- [ ] Define target pain points.
- [ ] Define design partner qualification criteria.
- [ ] Define discovery questions.
- [ ] Define pilot scope template.
- [ ] Define safe non-production evaluation scenarios.
- [ ] Define demo call script.
- [ ] Define success metrics.
- [ ] Define feedback checklist.
- [ ] Include suggested outbound message.
- [ ] Include explicit non-goals and boundaries.
- [ ] Avoid unsupported production, enterprise, compliance, and security claims.

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

- [ ] Design partner kit links resolve.
- [ ] README link, if added, resolves.
- [ ] Kit does not claim production readiness.
- [ ] Kit does not claim enterprise readiness.
- [ ] Kit does not claim compliance certification.
- [ ] Kit does not claim guaranteed security outcomes.
- [ ] Kit clearly states developer-preview maturity.
- [ ] Kit clearly states non-production pilot boundaries.
- [ ] No runtime behavior changed unless explicitly approved.
- [ ] No dependency changes were introduced.
- [ ] No release action was performed.

## Phase 5: Review

Create:

- [ ] `progress/review_012-design-partner-kit.md`

Move Feature 012 to `review`, not `done`, after verification.
