# ADR 012: Design Partner Kit Strategy

Status: accepted

Feature: `012-design-partner-kit`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Design Partner Readiness

## Context

The project now has developer-preview readiness, release-candidate polish, architecture documentation, a guided demo, packaging verification, and a security whitepaper.

The next SHIP gap is not another runtime feature. The next gap is a structured design partner asset that helps technical buyers evaluate whether Runtime Tool Authorization for AI Agents fits their agent architecture.

## Decision

Create Feature 012 as a SHIP-mode design partner kit spec gate.

The later implementation should create a lightweight but complete design partner kit focused on evaluation, discovery, pilot scoping, demo flow, and feedback collection.

## Rationale

A design partner kit creates outbound readiness without overstating maturity.

It also keeps selling artifacts separate from runtime implementation, security posture, release verification, and product documentation.

## Consequences

Positive:

- clearer outbound motion,
- better design partner qualification,
- repeatable discovery process,
- safer pilot framing,
- more useful feedback collection,
- cleaner separation between product evidence and sales conversation assets.

Tradeoff:

- CI release verification remains a separate future feature.

## Lifecycle Rule

Feature 012 must remain in `spec_ready` until explicit human approval.

After implementation, it should move to `review`, not `done`, until explicit closure approval is received.
