# VS Code Marketplace Publish Runbook

Feature: `017-marketplace-publish-commercial-launch`

## Purpose

This runbook describes the public publish gate for the Runtime Tool Authorization VS Code extension.

The extension has already been packaged, installed locally, and manually validated. Public publish is a separate gate.

## Extension Identity

Expected extension identity:

```text
publisher: bernydotjar
name: runtime-tool-authorization
extension id: bernydotjar.runtime-tool-authorization
version: 0.0.1
```

## Preconditions

Before public publish:

- Confirm the Marketplace publisher id exists.
- Confirm the publisher id matches `vscode-extension/package.json`.
- Confirm the extension name is available.
- Confirm README rendering is acceptable.
- Confirm CHANGELOG and LICENSE are included.
- Confirm `.vscodeignore` excludes generated local artifacts.
- Confirm no generated VSIX is committed.
- Confirm no generated compiled output is committed.
- Confirm public publish approval has been granted.

## Local Verification

Run from the repository root:

```sh
cd vscode-extension
npm install
npm run compile
npx @vscode/vsce package
code --install-extension runtime-tool-authorization-0.0.1.vsix --force
code --list-extensions --show-versions | rg 'bernydotjar.runtime-tool-authorization'
```

Expected installed extension:

```text
bernydotjar.runtime-tool-authorization@0.0.1
```

## Public Publish Command

Manual publish command:

```sh
cd vscode-extension
npx @vscode/vsce publish
```

Identity-based publish command:

```sh
cd vscode-extension
npx @vscode/vsce publish --azure-credential
```

Do not run either command without explicit approval.

## Explicit Publish Approval Required

Required phrase:

```text
APPROVAL TO PUBLISH
TARGET: VS Code Marketplace
EXTENSION: bernydotjar.runtime-tool-authorization
ACTION: vsce publish
```

## Post-Publish Smoke Test

After public publish:

1. Open the Marketplace listing.
2. Confirm title, description, repository link, README, license, and version.
3. Install from VS Code Marketplace.
4. Run Command Palette validation:

```text
Runtime Tool Auth: Initialize Policy
Runtime Tool Auth: Validate Policy
Runtime Tool Auth: Preview Authorized Tools
Runtime Tool Auth: Run Demo
Runtime Tool Auth: Open Audit Viewer
```

5. Confirm installed extension id:

```sh
code --list-extensions --show-versions | rg 'bernydotjar.runtime-tool-authorization'
```

## Unpublish / Rollback Notes

If a public publish has a serious issue:

- Use the Visual Studio Marketplace publisher management page to unpublish.
- Prefer unpublish over remove unless the extension name should never be reused.
- Do not delete versions casually; version removal is not reversible.
- Create a follow-up feature before republishing.

## Current State

Public publish has not been run.
