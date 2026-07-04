# Tasks: 011 Security Whitepaper

Feature: `011-security-whitepaper`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 2 - Make CTOs Trust It

## Phase 1: Spec Gate

- [x] Create requirements.
- [x] Create design.
- [x] Create tasks.
- [x] Create ADR.
- [x] Create progress artifact.
- [x] Register Feature 011 as `spec_ready`.
- [x] Update `progress/current.md`.
- [x] Update `progress/history.md`.
- [x] Confirm `docs/security-whitepaper.md` was not created.

## Phase 2: Approval Gate

- [x] Wait for explicit human approval.
- [x] Move Feature 011 from `spec_ready` to `approved` only after approval.
- [x] Do not implement before approval.

## Phase 3: Implementation Candidates

Implementation scope should be confirmed after approval. Candidate tasks:

- [x] Create `docs/security-whitepaper.md`.
- [x] Explain security posture for Runtime Tool Authorization for AI Agents.
- [x] Distinguish implemented behavior, developer-preview limitations, non-goals, and future hardening.
- [x] Cover runtime tool authorization boundary.
- [x] Cover request context and trust assumptions.
- [x] Cover policy evaluation and allowed tool surface.
- [x] Cover denied tool and fallback behavior.
- [x] Cover audit event evidence and local audit limitations.
- [x] Cover JSON policy limitations.
- [x] Cover LangChain/LangGraph adapter boundary.
- [x] Cover MCP-style tool surface filtering.
- [x] Cover tenant, user, role, plan, and permission constraints.
- [x] Add a threat-model-style section.
- [x] Add explicit non-goals.
- [x] Link to existing security, architecture, policy, audit, and demo docs.
- [x] Avoid unsupported production, IAM, compliance, audit, sandbox, and hosted-control-plane claims.

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

- [x] Whitepaper claims match implemented behavior.
- [x] Developer-preview limitations are explicit.
- [x] Non-goals are explicit.
- [x] No production-readiness claim was introduced.
- [x] No IAM replacement claim was introduced.
- [x] No compliance certification claim was introduced.
- [x] No tamper-proof audit claim was introduced.
- [x] No sandboxing claim was introduced.
- [x] No hosted enterprise control-plane claim was introduced.
- [x] No runtime behavior changed unless explicitly approved.
- [x] No release action was performed.

Verification status:

- [x] `python -m json.tool feature_list.json`
- [x] `PYTHONPATH=src python -m unittest discover -s tests`
- [x] `python examples/basic_agent/run_example.py`
- [x] `python examples/demo_experience/run_demo.py`
- [x] `PYTHONPATH=src python -m unittest discover -s tests/integration`
- [ ] `python scripts/verify_release_candidate.py`

`python scripts/verify_release_candidate.py` passed local checks but failed install/build steps in the sandbox because network access was blocked while resolving build dependencies. Escalation was rejected by the environment because the workspace is out of credits.

## Phase 5: Review

Create:

- [ ] `progress/review_011-security-whitepaper.md`

Move Feature 011 to `review`, not `done`, after verification.
