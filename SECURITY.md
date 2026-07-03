# Security Policy

## Supported Status

Dynamic Tool Router is currently a developer-preview project.

It is designed to demonstrate runtime tool authorization patterns for AI agents. It is not yet a hosted security product, enterprise IAM layer, compliance platform, sandbox, or tamper-proof audit system.

## What To Report

Please report issues related to:

- policy bypass behavior,
- tools being exposed when policy should withhold them,
- audit events missing for authorization or invocation flows,
- unsafe fallback behavior,
- documentation that overstates the security boundary,
- examples that encourage insecure usage.

## What Is Out Of Scope For Developer Preview

The following are known limitations, not vulnerabilities by themselves:

- local audit files are editable by users with filesystem access,
- static dashboard examples are unauthenticated,
- no hosted policy API exists yet,
- no production auth-provider integration exists yet,
- no tamper-proof audit sink exists yet,
- no sandboxing is provided for tool implementations,
- no compliance certification is claimed.

## Reporting Process

Open a GitHub issue with:

- description of the behavior,
- reproduction steps,
- expected behavior,
- actual behavior,
- affected files or examples,
- any relevant logs or audit events.

If the issue involves sensitive details, avoid posting secrets, tokens, credentials, private customer data, or production infrastructure details.

## Security Boundary

The application using this package must own authenticated identity and build `Principal` from trusted server-side session data. The LLM must not be allowed to set `user_id`, `tenant_id`, `plan`, `roles`, or `permissions`.

Tools should be registered server-side and routed through `ToolPolicyRouter` before being exposed to an agent.

See `docs/security-model.md` for the full developer-preview security model.
