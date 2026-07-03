# Tasks: 004 Sellable Developer Preview

Feature: `004-sellable-developer-preview`

Mode: SHIP

## Phase 1 — Spec Gate

- [x] Create requirements.
- [x] Create design.
- [x] Create tasks.
- [ ] Create ADR.
- [ ] Create progress artifact.
- [ ] Register Feature 004 in `feature_list.json` as `spec_ready`.
- [ ] Update `progress/current.md`.
- [ ] Append `progress/history.md`.
- [ ] Validate `feature_list.json`.

## Phase 2 — Approval Gate

Do not begin implementation until explicit human approval is recorded.

Approval must decide what to do with Feature 003, which is currently in `review` in the live repository.

Recommended approval sequence:

1. Close Feature 003 as `done` if accepted.
2. Approve Feature 004: `spec_ready -> approved`.
3. Begin SHIP-mode implementation.

## Phase 3 — README Productization

- [ ] Rewrite README hero and one-liner.
- [ ] Add buyer problem statement.
- [ ] Add "why now" section.
- [ ] Add futuristic terminal-friendly architecture diagram.
- [ ] Add quickstart.
- [ ] Add demo commands.
- [ ] Add policy example.
- [ ] Add audit example.
- [ ] Add LangChain/LangGraph compatibility section.
- [ ] Add security model summary.
- [ ] Add limitations.
- [ ] Add roadmap.
- [ ] Add SDLC / verification evidence.

## Phase 4 — Product Documentation

- [ ] Create/update `docs/product-positioning.md`.
- [ ] Create/update `docs/security-model.md`.
- [ ] Create/update `docs/policy-format.md`.
- [ ] Create/update `docs/audit-log-format.md`.
- [ ] Create/update `docs/demo-guide.md`.
- [ ] Create/update `docs/release-notes.md`.
- [ ] Cross-link integration docs.
- [ ] Cross-link persistent policy/audit docs.

## Phase 5 — Examples And Demo Flow

- [ ] Confirm `python examples/basic_agent/run_example.py` remains the primary demo.
- [ ] Ensure the demo shows allowed tools.
- [ ] Ensure the demo shows denied tool fallback.
- [ ] Ensure the demo shows JSON policy loading.
- [ ] Ensure the demo shows persisted audit events.
- [ ] Ensure the demo shows audit export.
- [ ] Ensure dashboard docs reference persisted sample data.
- [ ] Add realistic multi-tenant policy example if current example is too small.

## Phase 6 — Verification

Run:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
PYTHONPATH=src python -m unittest discover -s tests/integration
```

If optional integration dependencies are absent, record explicit skip messages.

## Phase 7 — SHIP Review

Create `progress/review_004-sellable-developer-preview.md` with:

- summary,
- changed files,
- product-readiness assessment,
- README assessment,
- documentation assessment,
- demo assessment,
- security assessment,
- verification commands,
- verification results,
- known limitations,
- SHIP-mode gaps,
- recommendation.

## Phase 8 — Closure

Only close as `done` if:

- README is buyer-facing,
- docs are complete enough for developer preview,
- test commands pass,
- demo command passes,
- integration dependency gates are clear,
- security model avoids overclaiming,
- review artifact recommends closure.

Otherwise keep Feature 004 in `review` or move to `blocked` with exact blockers.
