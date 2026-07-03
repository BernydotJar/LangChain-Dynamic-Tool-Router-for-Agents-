# ADR 005: README 3.0 Product Landing Page Strategy

Status: accepted

Feature: `005-readme-3-landing-page`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

## Context

Dynamic Tool Router already has a working developer-preview implementation and a stronger README created during Feature 004. The next product-readiness gap is GitHub-native comprehension and conversion.

The project should be understandable as infrastructure for AI agents, specifically runtime authorization for agent tools.

## Decision

Use the README as the primary landing page for the developer preview.

Primary product identity:

```text
Runtime Tool Authorization
for AI Agents

Never expose every tool.
Expose the right tool.
```

The README should explain:

- the authorization gap in agent systems,
- how runtime policy reduces overexposed tool surfaces,
- how tenant, user, role, plan, permissions, context, and MCP server constraints affect tool visibility,
- how developers can run the local demo,
- how the project fits into the SHIP-001 developer-preview roadmap.

## Rationale

Developer tools win when they are easy to understand, easy to try, easy to trust, and easy to share.

A GitHub README is the first buyer-facing and developer-facing asset. For this project, the README must function as both a technical entry point and a product landing page.

## Consequences

Positive:

- faster visitor comprehension,
- clearer market category,
- stronger CTO review path,
- cleaner design-partner narrative,
- better reuse for LinkedIn, website, docs, and launch material.

Tradeoffs:

- the README becomes more opinionated and product-led,
- claims must stay aligned to verified behavior,
- follow-up SHIP features are still needed for diagrams, demo polish, badges, release packaging, and trust files.

## Follow-up

After Feature 005, continue SHIP-001 with smaller reviewable features for diagrams, demo experience, trust signals, packaging, and release assets.
