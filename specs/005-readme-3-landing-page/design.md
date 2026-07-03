# Design: 005 README 3.0 Landing Page

Feature: `005-readme-3-landing-page`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

## Design Intent

The README should act like a GitHub-native product landing page.

It should help a reader answer five questions quickly:

1. What is this?
2. Why does it exist now?
3. How do I try it?
4. Can I trust the boundaries?
5. What is next?

## Messaging Hierarchy

### Primary Message

```text
Runtime Tool Authorization
for AI Agents
```

### Secondary Message

```text
Never expose every tool.
Expose the right tool.
```

### Product Category

```text
Infrastructure for AI agents.
```

### Value Proposition

Dynamic Tool Router evaluates request-time policy and injects only the tools an agent is allowed to use for the current user, tenant, plan, permissions, and context.

## README Structure

Recommended order:

1. Hero
2. One-line product statement
3. Missing layer diagram
4. Problem
5. What it does
6. Before/after contrast
7. Architecture diagram
8. Mermaid lifecycle diagram
9. Install
10. Quickstart
11. Demo output
12. Policy example
13. Audit example
14. LangChain/LangGraph compatibility
15. Documentation links
16. Security boundary
17. Verification
18. Roadmap
19. Harness SDLC evidence

## Diagram Strategy

Use both terminal-native diagrams and Mermaid.

Terminal-native diagrams support:

- fast scanning,
- plain Markdown readability,
- LinkedIn copy/paste reuse,
- terminal aesthetics.

Mermaid diagrams support:

- GitHub-native rendering,
- professional architecture review,
- future docs-site reuse.

## Trust Signals

Trust should come from verified project behavior, not invented social proof.

Allowed trust signals:

- tests,
- examples,
- docs,
- security model,
- release notes,
- harness lifecycle evidence,
- explicit limitations,
- optional dependency gates.

Do not add customer logos, fake badges, unsupported performance claims, or production readiness claims.

## CTO Review Lens

A CTO evaluating the repo should see:

- product judgment,
- security restraint,
- lifecycle discipline,
- practical examples,
- architecture clarity,
- roadmap maturity,
- commercial awareness.

## Implementation Notes

Feature 004 already upgraded the README substantially. Feature 005 should refine that upgrade into a more complete GitHub landing page, not duplicate it.

If Feature 004 remains `in_progress`, Feature 005 must remain `spec_ready` until Feature 004 has been verified and reviewed.

## Risks

- Over-polishing the README while demo behavior remains weak.
- Overclaiming enterprise security.
- Making the README too long without a clear first-screen message.
- Adding diagrams that do not match actual product behavior.
- Opening Feature 005 implementation before Feature 004 is verified.
