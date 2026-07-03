# 007 Architecture Visual Language

Status: proposed

Feature: `007-architecture-mermaid-diagrams`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: SHIP-001 Wave 1

## Context

The product is positioned as Runtime Tool Authorization for AI Agents:

```text
Never expose every tool. Expose the right tool.
```

Features 001-006 and 009 established product behavior, trust signals, and packaging readiness. The next missing Wave 1 asset is a visual architecture explanation that makes the product understandable to a CTO or infrastructure buyer in seconds.

## Decision

Feature 007 will use a dedicated architecture visual language:

- terminal-native diagrams for plain Markdown and source readability
- Mermaid diagrams for GitHub rendering
- infrastructure-grade wording
- developer-preview boundaries
- no production-readiness or compliance claims

The canonical implementation artifact will be:

```text
docs/architecture.md
```

## Consequences

- The repository gains a clearer architecture narrative without changing runtime behavior.
- The product category becomes easier to understand in GitHub, terminal, and copied-document contexts.
- Diagrams can later be reused in README, docs site, launch material, and sales conversations.
- The architecture doc must be maintained as behavior evolves.
- Claims must stay grounded in verified local library behavior.

## Alternatives Considered

- Add diagrams directly to README first: deferred to keep this feature focused and reviewable.
- Use only Mermaid: rejected because terminal/source readability is part of the product tone.
- Use only ASCII diagrams: rejected because GitHub-native rendering improves executive readability.
- Create a hosted architecture page: rejected as outside Wave 1 spec scope.
