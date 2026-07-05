# Requirements: 016 VS Code Marketplace Extension

Feature: `016-vscode-marketplace-extension`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Distribution Readiness

## Context

The Python package has developer-preview value, but distribution through the VS Code ecosystem requires a VS Code extension project.

The first extension should be a thin client around the repository's local policy and audit workflow.

## Goals

- Create a VS Code extension scaffold under `vscode-extension/`.
- Provide a valid extension manifest.
- Add command palette commands for core local workflows.
- Add TypeScript source that can compile into an extension entrypoint.
- Add Marketplace-specific README and changelog.
- Add `.vscodeignore` for VSIX packaging.
- Provide local commands for compile, package, and install-from-VSIX testing.
- Avoid public publish until local verification is completed by a human on a machine with Node, VS Code, and `vsce`.

## Non-Goals

- Do not publish automatically from this assistant session.
- Do not assume access to the user's local Azure, Visual Studio Marketplace, Node, or VS Code session.
- Do not create a Marketplace publisher identity from code.
- Do not add telemetry.
- Do not add remote services.
- Do not add entitlement enforcement to the extension in this feature.
- Do not claim production security certification.

## Functional Requirements

### FR-1 Extension Manifest

Create `vscode-extension/package.json` with:

- extension name,
- display name,
- description,
- publisher placeholder,
- version,
- VS Code engine range,
- command contributions,
- configuration contributions,
- scripts for compile and packaging.

### FR-2 Commands

Implement commands:

- `Runtime Tool Auth: Initialize Policy`
- `Runtime Tool Auth: Validate Policy`
- `Runtime Tool Auth: Preview Authorized Tools`
- `Runtime Tool Auth: Run Demo`
- `Runtime Tool Auth: Open Audit Viewer`

### FR-3 Policy Initialization

The extension should create a starter `tool_policies.json` in the workspace root if missing.

### FR-4 Policy Validation

The extension should validate the local policy JSON shape enough for developer-preview usage:

- root object exists,
- `version` exists,
- `fallback_tool_name` exists,
- `policies` exists and is an object.

### FR-5 Policy Preview

The extension should show policy tool names and basic plan/permission gates from the local policy file.

### FR-6 Demo Runner

The extension should open a VS Code terminal with the existing local Python demo command.

### FR-7 Audit Viewer

The extension should open a simple webview showing formatted local audit JSON if available.

### FR-8 Packaging Notes

Add docs for:

- `npm install`,
- `npm run compile`,
- `npx @vscode/vsce package`,
- `code --install-extension <vsix>`.

## Acceptance Criteria

- `vscode-extension/` exists.
- Extension manifest exists.
- TypeScript source exists.
- README and CHANGELOG exist for the extension.
- `.vscodeignore` exists.
- Repo progress files record that local verification still needs to be run by the user.
