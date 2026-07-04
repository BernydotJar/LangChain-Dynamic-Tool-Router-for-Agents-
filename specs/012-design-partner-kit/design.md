# Design: 012 Design Partner Kit

Feature: `012-design-partner-kit`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Design Partner Readiness

## Design Intent

Feature 012 should turn the repository from a developer-preview artifact into a conversation-ready design partner asset.

The design partner kit should help a technical buyer quickly answer:

1. Is this relevant to my agent architecture?
2. Can I evaluate it safely?
3. What scenarios should I test?
4. What does a useful pilot look like?
5. What feedback does the maintainer need?

## Design Principle

Sell the evaluation, not a finished enterprise product.

The kit should be concrete enough to support outbound conversations while staying honest about developer-preview maturity and current limitations.

## Expected Information Architecture

The later implementation should likely create:

```text
docs/design-partner-kit.md
```

Potential structure:

1. Executive one-liner
2. Ideal design partner profile
3. Pain points this project targets
4. Evaluation scenarios
5. Pilot scope template
6. Discovery questions
7. Demo walkthrough
8. Security discussion guide
9. Success criteria
10. Feedback checklist
11. Non-goals and boundaries
12. Suggested outbound message

## Design Partner Conversation Flow

```text
problem fit -> architecture fit -> safe demo -> pilot scenario -> feedback loop -> next step
```

## Positioning Rules

Use precise language:

- developer-preview
- evaluation
- design partner
- runtime tool authorization
- controlled tool surface
- audit evidence
- policy-driven routing
- non-production pilot

Avoid overclaims:

- production-ready
- enterprise-ready
- compliant
- certified
- guaranteed secure
- replaces IAM
- prevents prompt injection

## Constraints

- No runtime behavior changes.
- No dependency changes.
- No release actions.
- No unsupported security or commercial claims.
- Keep the kit lightweight and reviewable.
- Preserve harness lifecycle discipline.
