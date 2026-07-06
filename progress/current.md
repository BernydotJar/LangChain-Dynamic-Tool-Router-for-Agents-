# Current Progress

## Active Feature

`017-marketplace-publish-commercial-launch`

## Current State

Feature 001 status: `done`

Feature 002 status: `done`

Feature 003 status: `done`

Feature 004 status: `done`

Feature 005 status: `done`

Feature 006 status: `done`

Feature 007 status: `done`

Feature 008 status: `done`

Feature 009 status: `done`

Feature 010 status: `done`

Feature 011 status: `done`

Feature 012 status: `done`

Feature 013 status: `done`

Feature 014 status: `done`

Feature 015 status: `spec_ready`

Feature 016 status: `done`

Feature 017 status: `in_progress`

Feature 017 prepares the public Marketplace publish gate and the first commercial access path. Public Marketplace publish remains separate and has not been run.

## Product Direction

The product is framed as:

> Runtime Tool Authorization for AI Agents.
>
> Never expose every tool. Expose the right tool.

The intended buyer is a team building multi-tenant LangChain/LangGraph agents that needs runtime tool authorization, tenant-aware policy control, fallback behavior, audit evidence, and entitlement-backed premium access.

## Distribution Direction

Feature 016 added a VS Code extension wrapper under `vscode-extension/`.

Feature 017 prepares the distribution and commercial launch gate:

- Marketplace publish runbook,
- commercial access runbook,
- publisher and extension id confirmation,
- README rendering review,
- explicit publish approval phrase,
- post-publish smoke test.

## Recently Closed

Feature 016 is closed as `done` after VSIX packaging, local install, manual Command Palette validation, review artifact creation, and closure approval.

Feature 014 remains closed as `done` after entitlement contract implementation, release-candidate verification, SHIP review artifact creation, and closure approval.

## Parallel Spec Gate

Feature 015 remains `spec_ready` for provider-neutral entitlement architecture.

## Feature 017 Created And Updated

- `specs/017-marketplace-publish-commercial-launch/requirements.md`
- `specs/017-marketplace-publish-commercial-launch/design.md`
- `specs/017-marketplace-publish-commercial-launch/tasks.md`
- `docs/vscode-marketplace-publish-runbook.md`
- `docs/commercial-launch-runbook.md`

## Last Verified Extension State

Passed:

```sh
cd vscode-extension
npm install
npm run compile
npx @vscode/vsce package
code --install-extension runtime-tool-authorization-0.0.1.vsix --force
code --list-extensions --show-versions | rg 'bernydotjar.runtime-tool-authorization'
```

The installed extension was confirmed as:

```text
bernydotjar.runtime-tool-authorization@0.0.1
```

Manual Command Palette validation passed:

```text
- Initialize Policy: PASS
- Validate Policy: PASS
- Preview Authorized Tools: PASS
- Run Demo: PASS
- Open Audit Viewer: PASS
```

## Publish Gate

Do not run public publish until publisher id confirmation, README rendering review, extension name confirmation, Marketplace auth path confirmation, and explicit publish approval.
