# Runtime Tool Authorization

Policy and audit workflows for AI agent tool authorization inside VS Code.

This extension is a developer-preview shell for the Runtime Tool Authorization project. It helps agent builders initialize a policy file, validate policy shape, preview tool gates, run the local demo, and inspect audit exports without leaving VS Code.

## Commands

Open the Command Palette and run:

```text
Runtime Tool Auth: Initialize Policy
Runtime Tool Auth: Validate Policy
Runtime Tool Auth: Preview Authorized Tools
Runtime Tool Auth: Run Demo
Runtime Tool Auth: Open Audit Viewer
```

## Settings

```json
{
  "runtimeToolAuth.policyPath": "tool_policies.json",
  "runtimeToolAuth.auditPath": "runtime_audit_export.json",
  "runtimeToolAuth.pythonCommand": "python"
}
```

## Local development

```sh
npm install
npm run compile
```

## Package locally

```sh
npx @vscode/vsce package
```

## Install local VSIX

```sh
code --install-extension runtime-tool-authorization-0.0.1.vsix
```

## Publish checklist

Before public publish:

- Confirm the Marketplace publisher id matches `publisher` in `package.json`.
- Confirm extension name availability.
- Run `npm install`.
- Run `npm run compile`.
- Run `npx @vscode/vsce package`.
- Install the generated VSIX locally.
- Validate every command from the Command Palette.
- Review README rendering in the Marketplace.

## Scope

Developer preview only.

This extension does not provide a hosted service, production authorization system, enterprise control plane, or compliance certification.
