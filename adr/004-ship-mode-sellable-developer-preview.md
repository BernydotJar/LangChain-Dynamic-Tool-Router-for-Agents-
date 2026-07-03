# ADR 004: SHIP-Mode Sellable Developer Preview

Date: 2026-07-03

Feature: `004-sellable-developer-preview`

Status: Proposed

## Context

The repository has completed MVP increments for dynamic tool routing, persisted policy/audit storage, and optional framework integration proof.

The product goal has changed from prototype validation to a sellable developer-preview package.

The intended buyer story is:

> Auth0-style authorization for AI agent tools.

The product must remain honest: this positioning does not imply parity with Auth0, Okta, OPA, enterprise IAM platforms, or production compliance controls.

## Decision

Create Feature 004 as a SHIP-mode product-readiness increment rather than continuing with narrow MVP-only features.

Feature 004 will focus on:

- buyer-facing README,
- product positioning,
- demo flow,
- documentation completeness,
- policy format docs,
- audit format docs,
- security model,
- release notes,
- integration proof documentation,
- SHIP-mode review evidence.

## Rationale

A sellable developer tool needs more than core code. It needs:

1. immediate buyer clarity,
2. local install path,
3. a demo that shows the value proposition,
4. examples matching realistic usage,
5. visible security boundaries,
6. test and review evidence,
7. a roadmap that explains why the product can mature.

Developer-tool adoption is strongly affected by documentation quality, trust signals, ease of setup, and integration proof. Feature 004 packages those qualities into the repository.

## Consequences

### Positive

- The repo becomes easier to evaluate.
- The product story becomes clearer.
- The README becomes suitable for demos, outreach, and buyer review.
- Security caveats become explicit.
- Future features can build from a SHIP-mode baseline.

### Negative / Tradeoffs

- Feature 004 is documentation/productization-heavy.
- It does not add a hosted API or enterprise backend.
- It may expose current product limitations more visibly.
- It requires restraint to avoid overclaiming production readiness.

## Non-Goals

- No SaaS backend.
- No billing.
- No database.
- No production auth provider integration.
- No enterprise compliance claim.
- No tamper-proof audit log.
- No authenticated admin dashboard.

## Follow-Up Candidates

- `005-mcp-server-discovery-adapter`
- `005-admin-policy-editor`
- `005-release-packaging-and-versioning`
