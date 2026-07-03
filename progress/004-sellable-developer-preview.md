# 004 Sellable Developer Preview Progress

Feature: `004-sellable-developer-preview`

Mode: SHIP

## State

Status: `in_progress`

## Summary

Feature 004 reframes the product from MVP validation into a SHIP-mode developer-preview release track.

The goal is to make the Dynamic Tool Router sellable as:

> Auth0-style authorization for AI agent tools.

## Preconditions

- Feature 001: `done`
- Feature 002: `done`
- Feature 003: `done`

Human approval was received to close Feature 003 and approve Feature 004 for SHIP-mode implementation.

## Implemented In This Pass

- [x] Feature 003 moved from `review` to `done` in `feature_list.json`.
- [x] Feature 004 moved from `spec_ready` to `in_progress` in `feature_list.json`.
- [x] README rewritten for buyer-facing developer-preview positioning.
- [x] README includes futuristic terminal-native diagrams.
- [x] README includes install, quickstart, demo, policy, audit, integration, security, verification, roadmap, and harness evidence sections.
- [x] `docs/product-positioning.md` added.
- [x] `docs/security-model.md` expanded.
- [x] `docs/policy-format.md` added.
- [x] `docs/audit-log-format.md` added.
- [x] `docs/demo-guide.md` added.
- [x] `docs/admin-dashboard.md` added.
- [x] `docs/release-notes.md` added.

## SHIP Scope

- [x] buyer-facing README
- [x] futuristic text diagrams
- [x] product positioning docs
- [x] security model docs
- [x] policy format docs
- [x] audit format docs
- [x] demo guide
- [x] admin dashboard docs
- [x] release notes
- [ ] local verification evidence
- [ ] SHIP-mode review artifact

## Non-Goals

- hosted SaaS backend
- billing
- production auth provider integration
- enterprise compliance claim
- cloud deployment
- database
- real MCP discovery unless mock/example only
- authenticated admin dashboard
- tamper-proof audit storage

## Benchmark Principles Applied

Feature 004 applies developer-tool product principles:

1. one-screen clarity,
2. copy-paste quickstart,
3. immediate demo path,
4. strong visual explanation,
5. realistic examples,
6. security honesty,
7. visible verification evidence,
8. progressive docs,
9. integration proof,
10. roadmap.

## Spec Artifacts

- `specs/004-sellable-developer-preview/requirements.md`
- `specs/004-sellable-developer-preview/design.md`
- `specs/004-sellable-developer-preview/tasks.md`
- `adr/004-ship-mode-sellable-developer-preview.md`

## Implementation Artifacts

- `README.md`
- `docs/product-positioning.md`
- `docs/security-model.md`
- `docs/policy-format.md`
- `docs/audit-log-format.md`
- `docs/demo-guide.md`
- `docs/admin-dashboard.md`
- `docs/release-notes.md`

## Required Local Verification

Run:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
PYTHONPATH=src python -m unittest discover -s tests/integration
```

Feature 004 must remain `in_progress` until local verification evidence is reported.

## Next Valid Lifecycle Action

After verification passes, create `progress/review_004-sellable-developer-preview.md` and move Feature 004 to `review`.
