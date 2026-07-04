# ADR 013: Pricing And Landing Copy Strategy

Feature: `013-pricing-and-landing-copy`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Status: Proposed

## Context

Runtime Tool Authorization for AI Agents now has developer-preview functionality, trust documentation, security positioning, architecture material, demo experience, and a design partner kit.

The next commercial gap is pricing and landing-page copy.

The product should not be positioned as a cheap generic extension. It should be positioned as an agent infrastructure layer that controls tool visibility, injection, fallback behavior, and audit evidence at request time.

## Decision

Use a three-layer placement strategy:

1. `README.md` for concise public conversion.
2. `docs/pricing.md` as the canonical pricing page.
3. `docs/design-partner-kit.md` for the design partner sales motion.

Use the following pricing model:

- 30-day free trial.
- Solo: `$9/month`.
- Team: `$19/user/month`.
- Design Partner: `$49/month` flat for up to 5 users.
- First 20 design partners only.
- Founding price locked for 12 months.
- Enterprise: custom future/custom scope.

Use the following market framing:

```text
For less than the cost of one premium AI developer-tool seat, add runtime tool authorization to your agent stack.
```

Use this category contrast:

```text
Most agent frameworks ask:
Which tools should the agent use?

Runtime Tool Authorization asks:
Which tools is this user, tenant, role, plan, and request allowed to use right now?
```

## Rationale

`$1.99` or `$4.99` would position the product as a low-value plugin. `$9/month` creates a low-friction solo entry point while still supporting the category narrative.

`$19/user/month` aligns the team plan with professional developer-tool budgets.

`$49/month` flat for up to 5 users gives design partners a simple pilot motion without turning the first commercial conversations into procurement-heavy enterprise deals.

The 20-design-partner cap creates scarcity and helps frame the offer as early category-shaping access rather than discounting.

## Consequences

Positive:

- Pricing becomes visible and easy to explain.
- Design partners get a concrete offer.
- README becomes stronger as a conversion surface.
- The product is framed as agent infrastructure, not a cheap extension.

Tradeoffs:

- Publishing pricing may attract low-intent users.
- The product must keep developer-preview limitations clear.
- Enterprise copy must remain careful because hosted policy APIs, SSO, compliance workflows, and audit retention are not current capabilities.

## Constraints

Do not claim:

- production readiness,
- enterprise readiness,
- compliance certification,
- IAM replacement,
- sandboxing,
- prompt-injection prevention,
- guaranteed security outcomes,
- hosted policy API availability,
- SSO availability,
- audit retention availability.

## Status

Spec gate only. No implementation changes until explicit approval.
