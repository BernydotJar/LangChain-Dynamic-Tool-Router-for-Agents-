# Design: 016 VS Code Marketplace Extension

Feature: `016-vscode-marketplace-extension`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Distribution Readiness

## Decision

Create a VS Code extension as a thin developer-facing shell around the existing local policy and audit workflow.

The extension should not reimplement the Python router. It should help a developer initialize, inspect, validate, and demo the local authorization layer from inside VS Code.

## Architecture

```text
VS Code Extension
  |
  +-- Command Palette commands
  +-- Workspace file helpers
  +-- Output channel
  +-- Terminal launcher
  +-- Audit webview
  |
  v
Workspace files
  |
  +-- tool_policies.json
  +-- runtime_audit_export.json
  |
  v
Existing Python package and examples
```

## Extension Commands

### Initialize Policy

Creates `tool_policies.json` in the workspace root if absent.

### Validate Policy

Parses the configured policy file and checks the minimum developer-preview shape.

### Preview Authorized Tools

Displays configured tools and basic gates in an output channel.

### Run Demo

Starts a VS Code terminal and runs:

```sh
python examples/basic_agent/run_example.py
```

### Open Audit Viewer

Reads the configured audit export path and renders formatted JSON in a webview.

## Configuration

Add configuration keys:

```text
runtimeToolAuth.policyPath
runtimeToolAuth.auditPath
```

Defaults:

```text
tool_policies.json
runtime_audit_export.json
```

## Packaging

The extension should use TypeScript with:

```text
src/extension.ts
out/extension.js
```

`package.json` should include scripts:

```text
compile
watch
package
```

The first validation target is local VSIX packaging, not immediate public publish.

## Publisher

Use a placeholder publisher id in `package.json`.

The final publisher id must match the Visual Studio Marketplace publisher created by the user before public release.

## Risk Controls

- No telemetry.
- No remote calls.
- No credential handling.
- No automatic publish.
- No hidden workspace mutation beyond explicitly initialized policy file.
- No production readiness claim.

## Local Verification Target

Run from `vscode-extension/`:

```sh
npm install
npm run compile
npx @vscode/vsce package
code --install-extension runtime-tool-authorization-0.0.1.vsix
```

Then test the commands from the VS Code Command Palette.
