# Tasks: 012 Design Partner Kit

Feature: `012-design-partner-kit`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Design Partner Readiness

## Phase 1: Spec Gate

- [x] Create requirements.
- [x] Create design.
- [x] Create tasks.
- [x] Create ADR.
- [x] Create progress artifact.
- [x] Register Feature 012 as `spec_ready`.
- [x] Update `progress/current.md`.
- [x] Update `progress/history.md`.
- [x] Confirm `docs/design-partner-kit.md` was not created.

## Phase 2: Approval Gate

- [x] Wait for explicit human approval.
- [x] Move Feature 012 from `spec_ready` to approved implementation only after approval.
- [x] Do not implement before approval.

## Phase 3: Implementation Candidates

Implementation scope should be confirmed after approval. Candidate tasks:

- [x] Create `docs/design-partner-kit.md`.
- [x] Define ideal design partner profile.
- [x] Define buyer personas and evaluator roles.
- [x] Define target pain points.
- [x] Define design partner qualification criteria.
- [x] Define discovery questions.
- [x] Define pilot scope template.
- [x] Define safe non-production evaluation scenarios.
- [x] Define demo call script.
- [x] Define success metrics.
- [x] Define feedback checklist.
- [x] Include suggested outbound message.
- [x] Include explicit non-goals and boundaries.
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

- [ ] Design partner kit links resolve.
- [ ] README link, if added, resolves.
- [x] Kit does not claim production readiness.
- [x] Kit does not claim enterprise readiness.
- [x] Kit does not claim compliance certification.
- [x] Kit does not claim guaranteed security outcomes.
- [x] Kit clearly states developer-preview maturity.
- [x] Kit clearly states non-production pilot boundaries.
- [x] No runtime behavior changed unless explicitly approved.
- [x] No dependency changes were introduced.
- [x] No release action was performed.

Verification status:

- [ ] `python -m json.tool feature_list.json`
- [ ] `PYTHONPATH=src python -m unittest discover -s tests`
- [ ] `python examples/basic_agent/run_example.py`
- [ ] `python examples/demo_experience/run_demo.py`
- [ ] `PYTHONPATH=src python -m unittest discover -s tests/integration`
- [ ] `python scripts/verify_release_candidate.py`

## Phase 5: Review

Create:

- [ ] `progress/review_012-design-partner-kit.md`

Move Feature 012 to `review`, not `done`, after verification.
