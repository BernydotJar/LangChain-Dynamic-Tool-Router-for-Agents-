# Tasks: 007 Architecture Mermaid Diagrams

Feature: `007-architecture-mermaid-diagrams`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: SHIP-001 Wave 1

## Spec Gate

- [x] Confirm Feature 009 closure approval exists.
- [x] Close Feature 009 as `done`.
- [x] Register Feature 007 as `spec_ready` without renumbering completed features.
- [x] Create requirements spec.
- [x] Create design spec.
- [x] Create task list.
- [x] Create ADR.
- [x] Create progress artifact.
- [x] Update current progress.
- [x] Update history.
- [x] Validate `feature_list.json`.

## Implementation Tasks After Approval

- [x] Move Feature 007 from `spec_ready` to `approved` only after explicit human approval.
- [x] Move Feature 007 from `approved` to `in_progress` before implementation.
- [x] Create `docs/architecture.md`.
- [x] Add terminal-native system architecture diagram.
- [x] Add Mermaid system architecture diagram.
- [x] Add terminal-native request lifecycle diagram.
- [x] Add Mermaid request lifecycle diagram.
- [x] Add policy decision flow diagram.
- [x] Add before/after tool exposure diagram.
- [x] Add audit event lifecycle diagram.
- [x] Explain request context, policy evaluation, allowed tools, denied path, fallback, audit evidence, MCP-style filtering, and LangChain/LangGraph adapter boundary.
- [x] Keep developer-preview limitations explicit.
- [x] Avoid production-readiness, hosted IAM, SaaS, or compliance claims.

## Verification Tasks After Approval

- [x] Run `python -m json.tool feature_list.json`.
- [x] Run `PYTHONPATH=src python -m unittest discover -s tests`.
- [x] Run `python examples/basic_agent/run_example.py`.
- [x] Record exact verification output.

## Review Tasks After Approval

- [x] Create `progress/review_007-architecture-mermaid-diagrams.md`.
- [x] Document changed files.
- [x] Document verification evidence.
- [x] Document known limitations.
- [x] Move Feature 007 to `review` only after implementation and verification pass.
- [ ] Move Feature 007 to `done` only after explicit closure approval.

## Stop Conditions

- Approval is missing.
- Implementation would require runtime code changes.
- Diagrams would imply production readiness or hosted compliance behavior.
- README changes are requested without explicit approval in the implementation gate.
