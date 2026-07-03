# 001 Standalone Product Using Harness SDLC Authority

Status: accepted

## Context

The user requested a standalone Dynamic Tool Router product repository and asked to use the harness SDLC repository as process reference. The linked target GitHub repository was empty except for `.gitignore`.

The harness methodology normally requires a spec-ready state, explicit human approval, implementation, verification, and review as separate gates.

## Decision

Build a working MVP in this repository while preserving the harness artifact structure:

- `feature_list.json`
- `specs/`
- `progress/`
- `adr/`
- `docs/`

The initial feature is set to `review` after implementation and verification, not `done`, because final closure remains a human/reviewer action.

## Consequences

- The repo has usable product code immediately.
- The initial task is auditable as an intentional bootstrap exception.
- Future features should follow the normal approval-gated lifecycle.
