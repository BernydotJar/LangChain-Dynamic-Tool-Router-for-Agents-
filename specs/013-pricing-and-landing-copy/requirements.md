# Requirements: 013 Pricing And Landing Copy

Feature: `013-pricing-and-landing-copy`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Commercial Readiness

## Objective

Add commercially clear pricing and landing-page copy for Runtime Tool Authorization for AI Agents without overclaiming maturity, production readiness, compliance posture, or enterprise security guarantees.

## Primary Placement Strategy

The pricing message should be placed in three layers:

1. `README.md` - concise public conversion layer.
2. `docs/pricing.md` - canonical pricing, trial, offer, and packaging explanation.
3. `docs/design-partner-kit.md` - design partner offer and qualification flow.

Optional later placement:

- `docs/product-positioning.md` - buyer narrative and pricing justification.

## Required Pricing

Public launch pricing:

- 30-day free trial.
- Solo: `$9/month`.
- Team: `$19/user/month`.

Design partner offer:

- First 20 design partners.
- `$49/month` flat for up to 5 users.
- Founding price locked for 12 months.

Enterprise:

- Custom pricing.
- Reserved for production hardening, SSO, hosted policy APIs, compliance workflows, audit retention, and security review.

## Required Positioning Copy

Use this core message:

```text
Most agent frameworks ask:
Which tools should the agent use?

Runtime Tool Authorization asks:
Which tools is this user, tenant, role, plan, and request allowed to use right now?
```

Use this hero message:

```text
Your AI agent should not see every tool.
```

Use this pricing CTA:

```text
Start free for 30 days.
Then $9/month for solo builders or $19/user/month for teams.
```

Use this design partner message:

```text
We are accepting 20 design partners to shape the runtime authorization layer for AI agents.
```

Use this value anchor:

```text
For less than the cost of one premium AI developer-tool seat, add runtime tool authorization to your agent stack.
```

## Required README Changes

README should include a short pricing section after `Design Partner Signal` and before `Harness SDLC Evidence`.

The README section should be concise, no more than 120 words, and should link to `docs/pricing.md`.

README must not become a long pricing page.

## Required `docs/pricing.md`

Create a canonical pricing document covering:

- positioning headline,
- 30-day free trial,
- Solo plan,
- Team plan,
- Design Partner plan,
- Enterprise plan,
- why $9 and $19 are the right entry points,
- design partner scarcity and founding price lock,
- limitations and non-claims.

## Required `docs/design-partner-kit.md` Changes

Update the design partner kit to include:

- the first-20 design partner offer,
- `$49/month` flat for up to 5 users,
- 12-month founding price lock,
- non-production pilot boundary,
- qualification language for teams building real agent tooling.

## Non-Claims

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

Enterprise copy may mention these only as future/custom enterprise scope, not current product capabilities.

## Acceptance Criteria

- Pricing is visible from README.
- Pricing has a canonical docs page.
- Design partner offer is visible in the design partner kit.
- The copy preserves developer-preview maturity.
- The copy does not overclaim security or production readiness.
- No runtime code changes are made.
- No dependency changes are made.
- No release action is performed.
