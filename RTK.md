# Repo Tooling Kit

This repository uses a harness-style SDLC for controlled agentic delivery.

## Core Rule

Implementation must be traceable to a feature spec and verification evidence.

The reference harness requires explicit human approval before implementation. This repository documents the initial bootstrap exception in `adr/001-standalone-product-using-harness-sdlc-authority.md` because the user requested a working MVP in the same task.

## Lifecycle

Features move through:

`pending -> spec_ready -> approved -> in_progress -> review -> done`

Additional stop state:

`blocked`

## Source Of Truth

1. `feature_list.json`
2. `specs/<feature-id>/requirements.md`
3. `specs/<feature-id>/design.md`
4. `specs/<feature-id>/tasks.md`
5. `progress/current.md`
6. `progress/history.md`

## Allowed Commands

- read-only inspection commands
- `python -m unittest discover -s tests`
- `python examples/basic_agent/run_example.py`

## Forbidden Without Explicit Approval

- package installs
- dependency changes outside the approved spec
- destructive filesystem commands
- commands that expose secrets
- deployment or release commands

## Verification

Run:

```sh
python -m unittest discover -s tests
python examples/basic_agent/run_example.py
```
