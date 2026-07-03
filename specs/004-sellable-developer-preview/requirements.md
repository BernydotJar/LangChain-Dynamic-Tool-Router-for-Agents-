# Requirements: 004 Sellable Developer Preview

Feature: `004-sellable-developer-preview`

Mode: SHIP

## Product Intent

Turn the Dynamic Tool Router into a sellable developer-preview package for teams building multi-tenant LangChain and LangGraph agents.

Positioning:

> Auth0-style authorization for AI agent tools.
>
> A runtime RBAC and governance layer that decides which tools an agent may see, inject, invoke, deny, and audit per user, tenant, plan, permission, context, and MCP server availability.

## Why Now

Agent products are moving from small demo tool lists to large, dynamic tool catalogs. MCP-style tool ecosystems increase the need for runtime selection, authorization, policy visibility, and auditability. A sellable developer preview must prove that the router is understandable, installable, demoable, and honest about security boundaries.

## User Personas

### AI Platform Engineer

Needs a policy layer to control which tools agents can access across tenants, roles, plans, and request contexts.

### Product Engineering Lead

Needs a demoable governance story before embedding agents into a multi-tenant SaaS product.

### Security / Governance Reviewer

Needs clear audit output, security caveats, and non-overclaiming documentation before approving pilot use.

### Developer Evaluator

Needs a quickstart that works locally, shows value quickly, and does not force heavy LangChain/LangGraph dependencies into the core package.

## Functional Requirements

1. Rewrite the README for buyer-facing clarity.
2. Explain the product problem in less than 30 seconds.
3. Include a futuristic text diagram showing request-time tool authorization and injection.
4. Document local installation.
5. Document one-command or clearly sequenced demo execution.
6. Demonstrate:
   - allowed tool injection,
   - denied tool fallback,
   - JSON policy loading,
   - persisted audit events,
   - audit export,
   - LangChain-style adapter shape,
   - LangGraph-style middleware shape.
7. Add or update realistic multi-tenant policy examples.
8. Add or update persisted audit log examples.
9. Document JSON policy format.
10. Document audit log format.
11. Document static admin dashboard usage and limitations.
12. Document security model and explicit non-goals.
13. Document optional LangChain/LangGraph integration behavior and dependency gates.
14. Add release notes for the developer preview.
15. Preserve all existing public core APIs unless a change is explicitly justified.
16. Preserve all existing Feature 001, 002, and 003 verification behavior.

## Documentation Requirements

Create or update:

- `README.md`
- `docs/product-positioning.md`
- `docs/security-model.md`
- `docs/policy-format.md`
- `docs/audit-log-format.md`
- `docs/demo-guide.md`
- `docs/release-notes.md`
- `docs/langchain-langgraph-integration.md` if needed
- `examples/admin_dashboard/README.md` or dashboard notes if needed

## README Requirements

The README must include:

- crisp title and product one-liner,
- buyer problem,
- why this exists now,
- quickstart,
- demo command,
- architecture text diagram,
- policy example,
- audit example,
- LangChain/LangGraph compatibility notes,
- security model summary,
- limitations,
- roadmap,
- SDLC / harness evidence summary.

The README should use strong futuristic text diagrams, but remain readable in plain Markdown and terminal contexts.

## SHIP Acceptance Criteria

1. Feature 004 is registered in `feature_list.json` as SHIP mode.
2. Feature 004 remains `spec_ready` until explicit human approval.
3. Feature 003 remains in its current lifecycle state unless separately closed.
4. README is buyer-facing and no longer reads as only an internal MVP note.
5. README includes a clear futuristic text architecture diagram.
6. Local install workflow is documented.
7. Demo flow is documented and uses existing runnable examples.
8. Policy format documentation matches the JSON examples.
9. Audit format documentation matches persisted/exported audit output.
10. Security model clearly states what the product does and does not protect.
11. Dashboard documentation states it is static and unauthenticated.
12. Optional LangChain/LangGraph dependency behavior is documented clearly.
13. Release notes exist.
14. Existing unit tests pass.
15. Existing basic example passes.
16. Integration tests either run or skip with explicit dependency messages.
17. SHIP-mode review artifact exists before closure.
18. Known gaps and production-readiness risks are documented.

## Non-Goals

- No hosted SaaS backend.
- No billing.
- No production auth provider integration.
- No enterprise compliance claim.
- No cloud deployment.
- No database unless explicitly approved.
- No real MCP server discovery unless available as a mock/example.
- No dashboard authentication.
- No tamper-proof audit storage.
- No claim of parity with Auth0, OPA, Okta, or enterprise IAM systems.

## Required Verification

Run before review closure:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
PYTHONPATH=src python -m unittest discover -s tests/integration
```

If optional LangChain/LangGraph dependencies are absent, integration tests may skip only with explicit dependency-gate messages.
