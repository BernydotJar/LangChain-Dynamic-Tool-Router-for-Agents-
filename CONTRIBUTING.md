# Contributing

Thanks for considering a contribution to Dynamic Tool Router.

This project uses a harness-style SDLC. Contributions should preserve traceability from specification to verification.

## Local Setup

```sh
python -m pip install -e .
```

## Required Verification

Run before submitting changes:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
PYTHONPATH=src python -m unittest discover -s tests/integration
```

Optional LangChain/LangGraph integration tests may skip if optional dependencies are not installed. Skips should be explicit and documented.

## Harness Workflow

Feature work should follow:

```text
SPEC -> APPROVAL -> IMPLEMENT -> VERIFY -> REVIEW -> CLOSE
```

Expected artifacts:

```text
feature_list.json
specs/<feature-id>/requirements.md
specs/<feature-id>/design.md
specs/<feature-id>/tasks.md
progress/<feature-id>.md
progress/review_<feature-id>.md
adr/<decision>.md when needed
```

## Contribution Standards

- Keep product claims aligned with verified behavior.
- Do not add unsupported benchmark, compliance, customer, or production-security claims.
- Preserve the developer-preview security boundary.
- Prefer small, reviewable increments.
- Add or update tests when runtime behavior changes.
- Update docs when public behavior changes.

## Good First Contribution Areas

- Improve examples.
- Improve policy documentation.
- Add typed examples for common agent patterns.
- Improve dashboard sample data.
- Add clearer integration notes.
- Add packaging/release automation under a dedicated SHIP feature.

## Pull Request Checklist

- [ ] Feature registry updated when needed.
- [ ] Spec/progress artifacts added or updated.
- [ ] Tests pass locally.
- [ ] Demo still runs.
- [ ] README/docs updated when behavior changes.
- [ ] Security model remains accurate.
