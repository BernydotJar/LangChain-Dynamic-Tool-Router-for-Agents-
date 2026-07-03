# 008 Demo Experience Strategy

Status: proposed

Feature: `008-demo-experience`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: SHIP-001 Wave 1

## Context

Runtime Tool Authorization for AI Agents needs a demo that makes the product understandable in under three minutes. The repository already has local examples, architecture docs, trust signals, and packaging readiness. The remaining Wave 1 gap is a guided demo experience that shows the core value quickly.

## Decision

Feature 008 will specify, and later implement after approval, a local developer-preview demo experience that shows:

- request context
- JSON policy loading
- allowed tool exposure
- denied tool path
- fallback behavior
- audit evidence
- LangChain-style boundary
- LangGraph-style boundary

The implementation should prefer local mock tools and existing policy/audit primitives. It should avoid external services and runtime capability changes unless explicitly approved.

## Consequences

- New developers get a faster path to understanding the product.
- The demo can become the basis for screenshots, launch material, and design partner walkthroughs.
- The demo must stay grounded in developer-preview behavior.
- The demo should not become a substitute for production security claims.

## Alternatives Considered

- README-only demo: rejected for this feature because the user requested no README changes in the spec gate.
- Hosted demo: rejected because SHIP-001 Wave 1 should remain local and dependency-light.
- Video-only demo: rejected because local verification and source-reviewability matter more at this stage.
- Runtime feature expansion: rejected unless explicitly approved in implementation.
