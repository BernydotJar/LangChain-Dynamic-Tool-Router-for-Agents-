# Audit Log Format

Dynamic Tool Router records routing and tool-use events so teams can inspect authorization behavior after execution.

## Storage Shape

Developer preview uses local JSON Lines for persisted audit events.

```text
runtime_audit.jsonl
  {event 1}\n
  {event 2}\n
  {event 3}\n
```

Audit events can also be exported to JSON for demo and review.

## Event Types

Common event types:

| Event | Meaning |
|---|---|
| `allow` | Policy allowed a tool for the request context. |
| `deny` | Policy denied a tool for the request context. |
| `fallback` | A denied tool was mapped to fallback behavior. |
| `invoke` | An audited tool was invoked. |

## Example Event

```json
{
  "event_type": "deny",
  "tool_name": "delete_customer_record",
  "user_id": "user_123",
  "tenant_id": "tenant_acme",
  "reason": "missing required permission: records:delete"
}
```

## Example Export

```json
[
  {
    "event_type": "allow",
    "tool_name": "search_docs",
    "user_id": "user_123",
    "tenant_id": "tenant_acme"
  },
  {
    "event_type": "fallback",
    "tool_name": "delete_customer_record",
    "fallback_tool_name": "not_authorized",
    "user_id": "user_123",
    "tenant_id": "tenant_acme"
  }
]
```

## Privacy Defaults

Audit metadata should avoid raw tool arguments by default. This prevents accidental persistence of sensitive prompt, customer, or record data in the developer-preview audit file.

If an application needs argument-level audit, it should add an explicit redaction policy before persisting data.

## Local Audit Limitations

File-backed audit is useful for:

- local demos,
- test evidence,
- single-process developer evaluation,
- static dashboard sample data,
- product reviews.

It is not:

- tamper-proof,
- encrypted by default,
- retention-managed,
- compliance-ready,
- safe against a user with filesystem write access.

## Future Production Hardening

- Append-only audit sink.
- Hash-chained audit records.
- Redaction policy.
- Retention policy.
- Hosted audit API.
- Export to SIEM or observability backend.
