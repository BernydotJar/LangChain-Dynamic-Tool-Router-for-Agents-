# ADR 005: README as Product Landing Page

Date: 2026-07-03

Feature: `005-readme-3-landing-page`

Status: Proposed

## Context

Dynamic Tool Router is moving from MVP validation toward a sellable developer-preview product.

The repository README is the first product surface most users and buyers will see. For a developer tool, the README must function as both documentation and positioning.

## Decision

Treat the README as a GitHub-native product landing page.

The README should lead with:

```text
Runtime Tool Authorization
for AI Agents

Never expose every tool.
Expose the right tool.
```

The README must prioritize:

- fast comprehension,
- local demo path,
- architecture clarity,
- trust signals,
- security boundaries,
- roadmap maturity.

## Rationale

A polished README can increase the probability that a visitor:

- understands the product,
- runs the demo,
- trusts the maintainer's engineering discipline,
- shares the repo,
- starts a design-partner conversation.

## Consequences

### Positive

- Stronger first impression.
- Clearer product category.
- Better CTO-readiness.
- Better launch readiness.
- Better alignment with SHIP-001.

### Tradeoffs

- More documentation maintenance.
- More need to keep product claims aligned with verified behavior.
- Higher bar for examples and demos.

## Guardrails

Do not add unsupported:

- production security claims,
- performance claims,
- compliance claims,
- customer claims,
- Auth0 parity claims.

## Follow-Up

Feature 006 should focus on architecture visuals and Mermaid diagrams if Feature 005 only partially addresses diagram depth.
