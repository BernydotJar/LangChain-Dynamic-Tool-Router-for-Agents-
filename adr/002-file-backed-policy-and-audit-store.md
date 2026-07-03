# 002 File-Backed Policy and Audit Store

Status: proposed

## Context

Feature 001 delivered a working Dynamic Tool Router MVP with in-memory policies and an in-memory audit log. That proved the runtime authorization model, fallback behavior, and adapter shapes, but it does not yet meet the durability expectations of an RBAC/governance product.

The next product step is local persistence that allows teams to configure tool policies outside code and retain authorization evidence after a process exits.

## Decision

Feature 002 will specify file-backed persistence before adding any hosted service or database:

- JSON policy files for local configuration.
- JSON Lines audit persistence for append-friendly local writes.
- JSON audit export helper for inspection and dashboard samples.
- Validation before policy use.
- Additive integration with the existing `ToolPolicyRouter` and `AuditEvent` contracts.

## Consequences

- The product becomes more shippable without introducing operational infrastructure.
- Policy and audit artifacts remain inspectable in source control, local demos, and tests.
- JSON policies cannot represent arbitrary callable conditions in MVP.
- Local files do not provide multi-process durability, locking guarantees, access control, or compliance-grade retention.
- Future hosted or database stores can reuse the same conceptual contracts after the local MVP proves the shape.

## Alternatives Considered

- Database-backed store: rejected for MVP because it expands setup, deployment, and migration scope.
- Hosted policy API: rejected because Feature 002 is focused on local durability and config shape.
- YAML support: deferred to keep dependencies and parsing behavior minimal.
- Auth provider integration: deferred because policy persistence should be solved before identity-provider-specific mapping.
