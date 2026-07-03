# 002-persistent-policy-and-audit-store Design

## Approach

Feature 002 will add local file-backed stores as additive infrastructure around the existing Feature 001 router:

- `FilePolicyStore` loads and validates JSON policy configuration.
- `FileAuditStore` records `AuditEvent` objects durably.
- Policy loading converts JSON records into existing `ToolPolicy` dataclasses.
- Audit persistence reuses existing `AuditEvent.to_dict()` output.
- The router continues to accept an audit sink through its existing constructor.
- The static admin dashboard receives a persisted sample audit artifact or documented static data flow.

No runtime database, hosted API, or external dependency is introduced in MVP.

## Files You May Read

- `feature_list.json`
- `README.md`
- `AGENTS.md`
- `RTK.md`
- `CLAUDE.md`
- `src/tool_policy_router/**`
- `tests/**`
- `examples/**`
- `docs/**`
- `progress/**`
- `specs/002-persistent-policy-and-audit-store/**`
- `adr/002-file-backed-policy-and-audit-store.md`

## Files You May Touch After Approval

- `feature_list.json`
- `README.md` if usage documentation needs a top-level pointer
- `src/tool_policy_router/**`
- `tests/**`
- `examples/basic_agent/**`
- `examples/admin_dashboard/**`
- `examples/policies/**` if created for sample policy files
- `examples/audit/**` if created for sample audit output
- `docs/persistent-policy-and-audit-store.md`
- `docs/policy-model.md` if cross-reference is needed
- `docs/security-model.md` if caveats need updating
- `progress/002-persistent-policy-and-audit-store.md`
- `progress/review_002-persistent-policy-and-audit-store.md`
- `progress/history.md`

## Files You Must Not Touch

- secrets
- credentials
- deployment configuration
- unrelated local repositories
- `.git`
- harness-sdlc reference repository

## Proposed Policy JSON Shape

The MVP policy file should be explicit and dependency-free:

```json
{
  "version": 1,
  "default_allow": false,
  "fallback_tool_name": "not_authorized",
  "policies": {
    "search_docs": {
      "allowed_tenants": ["tenant_acme"],
      "allowed_plans": ["pro", "enterprise"],
      "required_permissions": ["docs:search"],
      "reason": "authorized"
    }
  }
}
```

Supported policy fields should map to existing `ToolPolicy` fields:

- `allowed_users`
- `allowed_tenants`
- `allowed_plans`
- `required_roles`
- `required_permissions`
- `required_mcp_servers`
- `reason`

`condition` is intentionally excluded from JSON loading in MVP because callables are not safely serializable.

## Proposed Policy Store Contract

`FilePolicyStore` responsibilities:

- read JSON from a local path
- reject invalid JSON
- reject unsupported schema versions
- reject unknown top-level fields
- reject unknown policy fields
- reject non-list set fields
- reject non-string values in set fields
- return a loaded policy bundle containing policies, fallback tool name, and default allow mode
- provide a helper to construct `ToolPolicyRouter` inputs without requiring users to hand-convert JSON

Validation failures should raise concise `ValueError` messages that do not expose host paths beyond the file explicitly requested by the caller.

## Proposed Audit Store Contract

`FileAuditStore` responsibilities:

- implement the same `record(event)` behavior expected by `ToolPolicyRouter`
- preserve existing in-memory audit ergonomics where reasonable through `events()` and `to_dicts()`
- persist each event after it is recorded
- support local export through an explicit helper
- create parent directories only for the configured audit path

MVP persistence should prefer JSON Lines for append-friendly writes:

```json
{"event_id":"...","timestamp":"...","action":"authorize","tool_name":"search_docs","allowed":true}
```

Audit export may produce a JSON array for dashboard samples or inspection.

## Admin Dashboard Example

The static dashboard should remain static and unauthenticated. Feature 002 may add:

- a checked-in sample audit JSON file
- dashboard copy explaining the sample comes from persisted audit output
- a small script or example command that exports audit events

The MVP should not add a server or browser-side file picker.

## Compatibility

Feature 002 must preserve:

- `ToolPolicyRouter`
- `InMemoryAuditLog`
- `AuditEvent`
- `RuntimeToolInjector`
- `LangGraphToolRouterMiddleware`
- `fallback_tool`
- existing tests and examples

New stores should be optional. Existing applications using in-memory policies and audit logs should continue to work.

## Risks

- Risk: file policy config can drift from code-defined tools.
  - Mitigation: validate config shape and document that tool existence is checked separately through `ToolRegistry`.
- Risk: JSON policies cannot represent callable `condition` policies.
  - Mitigation: explicitly document this as an MVP limitation.
- Risk: audit file writes can fail at runtime.
  - Mitigation: tests should cover basic persistence; SHIP mode should define failure policy and durability guarantees.
- Risk: persisted audit logs can contain tenant/user identifiers.
  - Mitigation: document privacy caveats and avoid compliance claims.
- Risk: static dashboard may imply production admin support.
  - Mitigation: label it as a static example and keep hosted admin UI out of scope.

## Verification Plan

After implementation approval, run:

```sh
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
```

Spec-gate validation:

```sh
python -m json.tool feature_list.json
```
