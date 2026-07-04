# ADR 011: Security Whitepaper Strategy

Status: accepted

Feature: `011-security-whitepaper`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 2 - Make CTOs Trust It

## Context

Runtime Tool Authorization for AI Agents now has a developer-preview implementation, product positioning, architecture diagrams, trust signals, demos, packaging metadata, and release-candidate polish.

SHIP-001 Wave 2 starts the trust-building phase for CTOs and technical reviewers. The next useful artifact is a security whitepaper that consolidates the security model, threat assumptions, boundaries, non-goals, and future hardening path.

## Decision

Open Feature 011 as a SHIP-mode spec gate for a future security whitepaper.

The spec gate records the required scope and constraints but does not create `docs/security-whitepaper.md`.

## Rationale

A whitepaper is a trust artifact, not a runtime feature. It should be created only after its scope is explicit and approved, because security language must be conservative and tied to verified behavior.

Separating this spec gate from implementation preserves the harness lifecycle and avoids introducing unsupported production, IAM, compliance, sandboxing, tamper-proof audit, or hosted control-plane claims.

## Consequences

Positive:

- establishes the next SHIP-001 Wave 2 feature without renumbering completed history,
- creates a clear approval gate before writing security claims,
- gives reviewers a structured future artifact to evaluate,
- keeps documentation claims aligned with developer-preview behavior.

Tradeoff:

- the whitepaper itself is not created until a later approved implementation pass.

## Lifecycle Rule

Feature 011 must remain in `spec_ready` until explicit human approval.

The next valid lifecycle action is:

```text
APPROVAL
FEATURE: 011-security-whitepaper
MODE: SHIP
STATE CHANGE: spec_ready -> approved
```
