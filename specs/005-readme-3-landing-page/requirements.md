# Requirements: 005 README 3.0 Landing Page

Feature: `005-readme-3-landing-page`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

## Objective

Turn the repository README into a polished open-source landing page that helps visitors understand, evaluate, run, and share the project.

## Product Message

Use the product identity:

```text
Runtime Tool Authorization
for AI Agents

Never expose every tool.
Expose the right tool.
```

## Business Goal

A CTO, AI platform engineer, or product engineering lead should understand the product value in under 30 seconds.

## Target Reader

- CTO evaluating product engineering quality.
- AI platform engineer evaluating agent infrastructure.
- Product lead looking for multi-tenant agent governance.
- Developer deciding whether to star, clone, and run the repo.
- Early design partner evaluating whether to discuss a pilot.

## Functional Requirements

1. Create a README landing-page structure with a stronger hero.
2. Add badges or badge placeholders where appropriate.
3. Add a crisp problem statement.
4. Add a buyer-facing product statement.
5. Add terminal-native diagrams.
6. Add Mermaid diagrams for GitHub-native rendering.
7. Add a quickstart that remains copy-paste runnable.
8. Add a demo section with expected output.
9. Add a clear feature grid.
10. Add a multi-tenant example.
11. Add a security boundary summary.
12. Add a roadmap tied to `SHIP-001`.
13. Add contribution and trust-signal sections.
14. Preserve existing verification commands.
15. Avoid overclaiming production security or Auth0 parity.

## Non-Goals

- No runtime code changes.
- No hosted website.
- No new dependencies.
- No screenshots or GIFs unless existing assets already exist.
- No benchmark claims without evidence.
- No production security claims.
- No customer or logo claims.

## Acceptance Criteria

- README opens with the Runtime Tool Authorization identity.
- README explains the product in under 30 seconds.
- README contains at least one terminal architecture diagram.
- README contains at least one Mermaid diagram.
- README contains a before/after tool exposure contrast.
- README contains quickstart and verification commands.
- README links to product docs, policy docs, audit docs, demo guide, and security model.
- README explicitly states developer-preview limitations.
- README has a roadmap aligned with SHIP-001.
- `feature_list.json` remains valid JSON.

## Required Verification

Run locally before review closure:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
PYTHONPATH=src python -m unittest discover -s tests/integration
```

Manual review:

- README renders correctly on GitHub.
- Mermaid diagram renders correctly on GitHub.
- Quickstart matches actual behavior.
- Claims match verified product behavior.
