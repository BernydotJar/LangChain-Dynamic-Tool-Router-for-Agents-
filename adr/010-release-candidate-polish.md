# ADR 010: Release Candidate Polish Strategy

Status: accepted

Feature: `010-release-candidate-polish`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

## Context

SHIP-001 Wave 1 has delivered product positioning, README polish, trust signals, architecture documentation, guided demo experience, and package metadata work.

The repository is now close to a developer-preview release candidate, but it needs a focused consistency pass before any later release decision.

## Decision

Create Feature 010 as a SHIP-mode release-candidate polish gate.

The feature should focus on repository readiness, documentation consistency, metadata consistency, and verification evidence.

## Rationale

A small polish feature is better than mixing release readiness, selling assets, docs-site work, and runtime changes in one broad change.

This preserves harness discipline and keeps the next increment reviewable.

## Consequences

Positive:

- cleaner release candidate surface,
- stronger reviewer confidence,
- clearer local verification path,
- less risk of accidental release action,
- better separation between GitHub readiness and outbound sales assets.

Tradeoff:

- design-partner material remains a separate future SHIP feature.

## Lifecycle Rule

Feature 010 must remain in `spec_ready` until explicit human approval.

After implementation, it should move to `review`, not `done`, until closure is explicitly approved.
