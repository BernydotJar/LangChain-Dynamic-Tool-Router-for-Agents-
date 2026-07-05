# ADR 016: VS Code Marketplace Extension

Feature: `016-vscode-marketplace-extension`

Status: Accepted

Mode: SHIP

## Context

The project is currently distributed as a Python developer-preview package. To reach agent builders inside their IDE, the project needs a VS Code extension wrapper.

## Decision

Create a TypeScript VS Code extension under `vscode-extension/`.

The extension will be a thin local workflow shell, not a hosted control plane. It will help developers initialize policy files, validate policy shape, preview tool gates, run the local demo, and inspect audit exports.

## Consequences

Positive:

- Creates a Marketplace-ready distribution path.
- Makes the project easier to demo from VS Code.
- Keeps the existing Python core intact.
- Avoids premature hosted service claims.

Negative:

- Adds Node/TypeScript packaging to the repository.
- Requires local user verification before publish.
- Requires publisher identity and Marketplace validation outside the repository.

## Constraints

- No telemetry.
- No remote service dependency.
- No automatic public publish from the assistant session.
- No credential handling.
- No hidden workspace mutations.
- No production readiness claim.
