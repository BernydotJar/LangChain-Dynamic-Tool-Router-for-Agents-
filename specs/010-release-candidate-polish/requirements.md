# Requirements: 010 Release Candidate Polish

Feature: `010-release-candidate-polish`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

State: `spec_ready`

## Objective

Prepare the repository for a cleaner developer-preview release candidate.

Feature 010 focuses on presentation consistency, release-readiness documentation, and verification evidence after the README, trust signals, packaging, architecture, and demo experience features have landed.

## Product Identity

```text
Runtime Tool Authorization
for AI Agents

Never expose every tool.
Expose the right tool.
```

## Problem

The repository now has product positioning, architecture documentation, trust signals, packaging metadata, and a guided demo. It needs a final polish pass before any later release action is considered.

## User Stories

1. As a developer, I want the repo to look ready to clone, install, and run.
2. As a technical reviewer, I want lifecycle discipline and clear known boundaries.
3. As a maintainer, I want release steps documented without accidental release actions.
4. As a reader, I want docs to agree on product identity, version status, demo commands, and known limitations.

## Required Scope For Implementation Phase

Capture requirements for a later implementation pass to review and polish:

- README release-readiness consistency.
- docs index and cross-link consistency.
- release checklist consistency.
- version and packaging metadata consistency.
- CHANGELOG readiness for `0.1.0.dev0`.
- demo command consistency across README and docs.
- architecture and security-model language consistency.
- known limitations and non-goals consistency.
- verification command consistency.

## Non-Goals

- Do not publish a package.
- Do not create a tag.
- Do not create a hosted release entry.
- Do not change runtime behavior.
- Do not add external services.
- Do not introduce mandatory LangChain or LangGraph dependencies.
- Do not change the product maturity claim.

## Acceptance Criteria For This Spec Gate

- Feature 010 is registered as `spec_ready`.
- Requirements, design, tasks, ADR, and progress artifacts are created.
- `progress/current.md` points to Feature 010 as the active spec-gate feature.
- `progress/history.md` records the spec-gate opening.
- No implementation files are changed beyond lifecycle and spec artifacts.
- Feature 010 is explicitly tied to SHIP-001.

## Later Implementation Acceptance Criteria

Implementation must not start until explicit approval changes Feature 010 from `spec_ready` to `approved`.

When approved, the implementation should move Feature 010 to `review`, not `done`, after verification evidence is captured.
