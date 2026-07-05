# 016 VS Code Marketplace Extension Progress

Feature: `016-vscode-marketplace-extension`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Distribution Readiness

## State

Status: `in_progress`

## Summary

Feature 016 creates a VS Code extension scaffold for local developer-preview workflows.

The extension is prepared for local compile and VSIX packaging, but local verification has not yet been run in the user's environment.

## Created

- `specs/016-vscode-marketplace-extension/requirements.md`
- `specs/016-vscode-marketplace-extension/design.md`
- `specs/016-vscode-marketplace-extension/tasks.md`
- `adr/016-vscode-marketplace-extension.md`
- `vscode-extension/package.json`
- `vscode-extension/tsconfig.json`
- `vscode-extension/src/extension.ts`
- `vscode-extension/README.md`
- `vscode-extension/CHANGELOG.md`
- `vscode-extension/.vscodeignore`

## Extension Commands

- Runtime Tool Auth: Initialize Policy
- Runtime Tool Auth: Validate Policy
- Runtime Tool Auth: Preview Authorized Tools
- Runtime Tool Auth: Run Demo
- Runtime Tool Auth: Open Audit Viewer

## Local Verification Required

Run from the repository root:

```sh
cd vscode-extension
npm install
npm run compile
npx @vscode/vsce package
code --install-extension runtime-tool-authorization-0.0.1.vsix
```

## Publish Gate

Do not publish publicly until:

- compile passes,
- VSIX package is generated,
- VSIX installs locally,
- commands are validated in VS Code,
- publisher id is confirmed,
- README rendering is reviewed,
- extension name is confirmed.

## Notes

The assistant cannot access the user's local Azure CLI, Visual Studio Marketplace session, VS Code installation, Node installation, or generated VSIX file from this repository-only workflow.
