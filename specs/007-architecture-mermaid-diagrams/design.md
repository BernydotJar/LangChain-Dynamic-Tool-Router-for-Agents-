# Design: 007 Architecture Mermaid Diagrams

Feature: `007-architecture-mermaid-diagrams`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: SHIP-001 Wave 1

## Approach

Feature 007 will create a dedicated architecture document in the implementation phase:

```text
docs/architecture.md
```

The document should make the product category obvious:

```text
Runtime Tool Authorization for AI Agents
```

It should explain that the product sits between LLM-powered agents and tool/infrastructure access, enforcing tenant-aware, policy-driven, runtime tool exposure.

## Required Diagram Set

The implementation phase must include at least these diagrams:

- System architecture
- Request lifecycle
- Policy decision flow
- Before/after tool exposure
- Audit event lifecycle

## Diagram Formats

Each major concept should prefer two compatible formats where useful:

- terminal-native plain Markdown diagrams for raw README/docs readability
- Mermaid diagrams for GitHub rendering

Plain text diagrams should remain readable in terminals, source views, copied docs, and LLM contexts. Mermaid diagrams should be concise and GitHub-compatible.

## Required Concepts

The visual language must explain:

- Runtime Tool Authorization layer
- policy evaluation
- request context
- allowed tool surface
- denied tool path
- fallback behavior
- audit evidence
- MCP-style tool surface filtering
- LangChain/LangGraph adapter boundary

## Proposed Architecture Narrative

The document should frame Dynamic Tool Router as:

```text
The missing authorization layer between
LLMs -> Agents -> Tools -> Your Infrastructure
```

The central question for every request is:

```text
Which tools should this user, tenant, plan, policy, and context expose right now?
```

## Grounding Rules

The diagrams must reflect existing verified behavior:

- `ToolPolicyRouter`
- `RuntimeToolInjector`
- `LangGraphToolRouterMiddleware`
- `FilePolicyStore`
- `FileAuditStore`
- fallback tool behavior
- JSON policy loading
- local audit evidence
- optional LangChain/LangGraph integration tests

The diagrams must not imply:

- hosted IAM
- centralized SaaS control plane
- compliance certification
- production-grade security boundary
- automatic MCP discovery beyond current documented surface filtering

## Files You May Read

- `feature_list.json`
- `README.md`
- `docs/**`
- `src/**`
- `tests/**`
- `examples/**`
- `progress/**`
- `specs/007-architecture-mermaid-diagrams/**`
- `adr/007-architecture-visual-language.md`

## Files You May Touch After Approval

- `docs/architecture.md`
- `docs/langchain-integration.md` if cross-reference is needed
- `docs/policy-model.md` if cross-reference is needed
- `docs/security-model.md` if cross-reference is needed
- `README.md` only if explicitly included in the implementation approval
- `feature_list.json`
- `progress/007-architecture-mermaid-diagrams.md`
- `progress/review_007-architecture-mermaid-diagrams.md`
- `progress/current.md`
- `progress/history.md`

## Files You Must Not Touch

- runtime source code unless explicitly approved
- packaging artifacts
- release artifacts
- secrets or credentials
- `.git`
- unrelated repositories

## Risks

- Risk: diagrams overclaim production security.
  - Mitigation: include explicit developer-preview boundaries and link to security model.
- Risk: Mermaid diagrams become too complex to read.
  - Mitigation: keep diagrams small and pair them with terminal-native diagrams.
- Risk: README and docs diverge.
  - Mitigation: use `docs/architecture.md` as the canonical architecture visual source.
- Risk: architecture suggests a hosted product that does not exist.
  - Mitigation: describe current library behavior and future-facing product direction separately.

## Verification Plan

Spec gate:

```sh
python -m json.tool feature_list.json
```

After implementation approval:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
```
