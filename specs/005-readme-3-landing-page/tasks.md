# Tasks: 005 README 3.0 Landing Page

Feature: `005-readme-3-landing-page`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

## Phase 1: Spec Gate

- [x] Create requirements.
- [x] Create design.
- [x] Create tasks.
- [ ] Create ADR.
- [ ] Create progress artifact.
- [ ] Register Feature 005 as `spec_ready`.
- [ ] Update `progress/current.md`.
- [ ] Update `progress/history.md`.

## Phase 2: Approval Gate

- [ ] Confirm Feature 004 status.
- [ ] Do not implement Feature 005 while Feature 004 remains unverified.
- [ ] Record explicit approval before moving Feature 005 to `approved`.

## Phase 3: README Refinement

- [ ] Strengthen hero.
- [ ] Add or refine badge section.
- [ ] Add product-category line.
- [ ] Add buyer persona section if useful.
- [ ] Add feature grid.
- [ ] Add Mermaid architecture diagram.
- [ ] Add multi-tenant example.
- [ ] Add design-partner callout if appropriate.
- [ ] Add contribution/trust-signal section.
- [ ] Tighten roadmap.
- [ ] Confirm security language remains bounded.

## Phase 4: Verification

Run:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
PYTHONPATH=src python -m unittest discover -s tests/integration
```

Manual checks:

- [ ] README renders cleanly on GitHub.
- [ ] Mermaid renders cleanly.
- [ ] Quickstart is accurate.
- [ ] Product claims match implementation.
- [ ] No unsupported benchmark, security, customer, or revenue claims.

## Phase 5: Review

Create:

- [ ] `progress/review_005-readme-3-landing-page.md`

The review artifact must include:

- files changed,
- product-readiness assessment,
- CTO-readiness assessment,
- verification output,
- manual README checks,
- known gaps,
- next recommended feature.
