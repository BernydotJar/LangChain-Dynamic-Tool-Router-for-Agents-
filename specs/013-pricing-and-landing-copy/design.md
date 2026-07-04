# Design: 013 Pricing And Landing Copy

Feature: `013-pricing-and-landing-copy`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Commercial Readiness

## Design Principle

Pricing should make Runtime Tool Authorization feel like agent infrastructure, not a cheap extension.

The copy should avoid bargain-bin positioning while still creating a low-friction entry point for individual builders and small teams.

## Placement Architecture

### 1. README.md

Role: public conversion surface.

Placement: after `Design Partner Signal`, before `Harness SDLC Evidence`.

Purpose:

- Make pricing visible without overwhelming technical readers.
- State the 30-day free trial.
- State Solo and Team pricing.
- State the first-20 design partner offer.
- Link to `docs/pricing.md` for details.

README copy should be short and sharp.

### 2. docs/pricing.md

Role: canonical pricing and packaging page.

Purpose:

- Explain the pricing model.
- Make the $9 and $19 price points feel intentional.
- Present the design partner offer.
- Explain enterprise as future/custom scope.
- Preserve developer-preview limits.

### 3. docs/design-partner-kit.md

Role: sales enablement for early conversations.

Purpose:

- Give prospects a concrete pilot offer.
- Create scarcity with first 20 design partners.
- Use the `$49/month` flat plan for up to 5 users as the evaluation motion.
- Keep the pilot non-production.

### 4. docs/product-positioning.md

Role: optional buyer narrative reinforcement.

Purpose:

- Tie pricing to the category: runtime authorization for agent tools.
- Explain why the product is not priced like a generic extension.

This file is optional for implementation.

## Pricing Architecture

### Free Trial

30-day free trial.

Goal: remove evaluation friction.

### Solo

`$9/month`

Buyer: individual AI engineer, indie builder, consultant, or technical founder.

Positioning:

- below common premium AI developer-tool seats,
- serious enough to avoid cheap-extension perception,
- low enough for impulse evaluation.

### Team

`$19/user/month`

Buyer: engineering teams building multi-tenant agents.

Positioning:

- aligned with professional developer-tool budgets,
- still accessible for small teams,
- stronger anchor than Solo.

### Design Partner

`$49/month flat for up to 5 users`

Constraints:

- first 20 design partners only,
- founding price locked for 12 months,
- non-production evaluation only.

Positioning:

- creates scarcity,
- converts the product from cheap tool to early-access infrastructure,
- makes the buyer feel like they are helping shape a category.

### Enterprise

Custom.

May include future/custom scope language:

- production hardening,
- SSO,
- hosted policy APIs,
- compliance workflows,
- audit retention,
- security review.

Must not imply these capabilities are currently available.

## Core Copy Blocks

### Category Contrast

```text
Most agent frameworks ask:
Which tools should the agent use?

Runtime Tool Authorization asks:
Which tools is this user, tenant, role, plan, and request allowed to use right now?
```

### Hero

```text
Your AI agent should not see every tool.
```

### Pricing CTA

```text
Start free for 30 days.
Then $9/month for solo builders or $19/user/month for teams.
```

### Design Partner CTA

```text
We are accepting 20 design partners to shape the runtime authorization layer for AI agents.
```

### Value Anchor

```text
For less than the cost of one premium AI developer-tool seat, add runtime tool authorization to your agent stack.
```

## Verification Strategy

Because this is documentation and positioning work, verification should include:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
python examples/demo_experience/run_demo.py
PYTHONPATH=src python -m unittest discover -s tests/integration
python scripts/verify_release_candidate.py
```

Manual checks:

- README link to `docs/pricing.md` resolves.
- `docs/pricing.md` exists.
- `docs/design-partner-kit.md` includes the design partner offer.
- No production-readiness claim is introduced.
- No enterprise-readiness claim is introduced.
- No compliance certification claim is introduced.
- No guaranteed security outcome claim is introduced.
- Enterprise section is explicitly future/custom scope.
- No runtime code changes are introduced.
- No dependency changes are introduced.
- No release action is performed.
