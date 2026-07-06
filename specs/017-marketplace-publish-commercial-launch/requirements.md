# Requirements: 017 Marketplace Publish And Commercial Launch

Feature: `017-marketplace-publish-commercial-launch`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Distribution And Commercial Launch

## Context

Feature 016 closed the VS Code extension scaffold and local validation path.

The next step is not additional command implementation. The next step is to prepare the public distribution and commercial access gate.

The extension should remain installable from the Marketplace while commercial access is managed through the project's entitlement and license boundary, not through Marketplace install gating.

## Goals

- Prepare a public Marketplace publish runbook.
- Prepare a commercial access runbook for the first customers.
- Keep the extension free to install while premium or team access is controlled by entitlement state.
- Preserve manual license activation as the first commercial path.
- Avoid public publish until final explicit approval.
- Avoid adding a live provider integration in this feature.
- Keep Feature 015 as the future provider-neutral implementation path.

## Non-Goals

- Do not run public `vsce publish` from this assistant session.
- Do not add live provider integration.
- Do not add remote service calls to the VS Code extension.
- Do not claim Marketplace-native billing.
- Do not claim production IAM, compliance certification, or enterprise security certification.
- Do not remove local developer-preview boundaries.

## Functional Requirements

### FR-1 Publish Runbook

Create a documented publish runbook with:

- publisher id confirmation,
- extension id confirmation,
- README rendering review,
- version confirmation,
- local package command,
- publish command,
- rollback/unpublish notes,
- post-publish smoke test.

### FR-2 Commercial Access Runbook

Create a documented first-customer commercial access path with:

- design partner / founding customer offer,
- manual activation workflow,
- entitlement state source of truth,
- support and renewal notes,
- non-goals and limitations.

### FR-3 Extension Metadata Review

Verify existing extension metadata:

- `publisher`,
- `name`,
- `displayName`,
- `description`,
- `repository`,
- `license`,
- README,
- CHANGELOG,
- `.vscodeignore`.

### FR-4 Explicit Publish Gate

Document the exact phrase required before running public publish:

```text
APPROVAL TO PUBLISH
TARGET: VS Code Marketplace
EXTENSION: bernydotjar.runtime-tool-authorization
ACTION: vsce publish
```

### FR-5 No Hidden Publish

The repo may include commands and runbooks, but no public publish should be run without explicit approval.

## Acceptance Criteria

- Feature 017 is registered as `in_progress`.
- Publish runbook exists.
- Commercial launch runbook exists.
- Current progress identifies Feature 017 as active.
- Feature 016 remains `done`.
- Feature 015 remains `spec_ready`.
- Public publish remains gated.
