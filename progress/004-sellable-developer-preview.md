# 004 Sellable Developer Preview Progress

Feature: `004-sellable-developer-preview`

Mode: SHIP

## State

Status: `spec_ready`

## Summary

Feature 004 reframes the next product increment from another MVP-only implementation feature into a SHIP-mode developer-preview release track.

The goal is to make the Dynamic Tool Router sellable as:

> Auth0-style authorization for AI agent tools.

## Preconditions

- Feature 001: `done`
- Feature 002: `done`
- Feature 003: currently `review` in the live repository at the time this feature was created

Feature 004 may be specified while Feature 003 is in review, but implementation should not begin until lifecycle handling is explicit.

## Scope

- [x] buyer-facing README plan
- [x] futuristic text diagram requirement
- [x] product positioning docs
- [x] security model docs
- [x] policy format docs
- [x] audit format docs
- [x] demo guide
- [x] release notes
- [x] SHIP-mode review requirements
- [x] verification plan

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

## Next Valid Lifecycle Action

Human approval may move Feature 004 from `spec_ready` to `approved` after the team explicitly resolves Feature 003 lifecycle handling.

Recommended handling:

1. Close Feature 003 as `done` if review evidence is accepted.
2. Approve Feature 004.
3. Implement Feature 004 in SHIP mode.

## Required Verification During Implementation

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
PYTHONPATH=src python -m unittest discover -s tests/integration
```
