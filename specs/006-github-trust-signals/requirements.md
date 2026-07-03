# Requirements: 006 GitHub Trust Signals

Feature: `006-github-trust-signals`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

## Objective

Add the repository trust signals expected from a serious developer-preview infrastructure project.

## Business Goal

Make the project easier for CTOs, engineering leads, security reviewers, and design partners to evaluate without overstating production readiness.

## Functional Requirements

1. Add `SECURITY.md` with reporting guidance and developer-preview boundaries.
2. Add `CONTRIBUTING.md` with local setup, verification, and harness workflow.
3. Add `CHANGELOG.md` with developer-preview release history.
4. Add `CODE_OF_CONDUCT.md` with contributor expectations.
5. Add `LICENSE` if absent or document license gap if present state cannot be confirmed.
6. Add README trust-signal links.
7. Add simple badge links only when accurate.
8. Preserve all existing tests and examples.
9. Avoid fake stars, customers, logos, benchmarks, or compliance claims.

## Non-Goals

- No hosted release automation.
- No PyPI publishing.
- No production security certification.
- No customer logos.
- No benchmark claims.
- No legal guarantee around license selection.

## Acceptance Criteria

- Trust files exist at repo root.
- README links to trust files.
- Security disclosure path is clear.
- Contribution workflow references the harness.
- Changelog accurately lists MVP/developer-preview milestones.
- Feature registry remains valid JSON.
- Tests still pass.
