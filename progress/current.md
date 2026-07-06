# Current Progress

## Active Feature

`016-vscode-marketplace-extension`

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

Feature 016 status: `review`

Feature 016 has a VS Code extension scaffold prepared. Local compile, VSIX package creation, local VSIX install, installed-extension listing, and manual Command Palette validation have passed. Feature 016 is now in `review` and should not be closed or published until review approval.

## Product Direction

The product is framed as:

> Runtime Tool Authorization for AI Agents.
>
> Never expose every tool. Expose the right tool.

The intended buyer is a team building multi-tenant LangChain/LangGraph agents that needs runtime tool authorization, tenant-aware policy control, fallback behavior, audit evidence, and entitlement-backed premium access.

## Distribution Direction

Feature 016 adds a VS Code extension wrapper under `vscode-extension/`.

The extension is a thin local workflow shell for:

- initializing policy files,
- validating policy shape,
- previewing configured tool gates,
- launching the local demo,
- viewing local audit exports,
- preparing a local VSIX package.

## Recently Closed

Feature 014 is closed as `done` after entitlement contract implementation, release-candidate verification, SHIP review artifact creation, and closure approval.

## Parallel Spec Gate

Feature 015 remains `spec_ready` for provider-neutral entitlement architecture.

## Feature 016 Created And Updated

- `specs/016-vscode-marketplace-extension/requirements.md`
- `specs/016-vscode-marketplace-extension/design.md`
- `specs/016-vscode-marketplace-extension/tasks.md`
- `adr/016-vscode-marketplace-extension.md`
- `progress/016-vscode-marketplace-extension.md`
- `progress/review_016-vscode-marketplace-extension.md`
- `docs/vscode-extension-manual-test.md`
- `vscode-extension/package.json`
- `vscode-extension/package-lock.json`
- `vscode-extension/tsconfig.json`
- `vscode-extension/src/extension.ts`
- `vscode-extension/README.md`
- `vscode-extension/CHANGELOG.md`
- `vscode-extension/LICENSE`
- `vscode-extension/.vscodeignore`

## Local Verification

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

Do not run public publish until review approval, publisher id confirmation, README rendering review, extension name confirmation, and explicit publish approval.
