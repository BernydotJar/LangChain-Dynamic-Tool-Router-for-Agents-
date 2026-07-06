# Design: 017 Marketplace Publish And Commercial Launch

Feature: `017-marketplace-publish-commercial-launch`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Distribution And Commercial Launch

## Decision

Use VS Code Marketplace as the public distribution channel and keep commercial access separate through the entitlement and license boundary.

The extension should remain installable for discovery and trust. Premium/team access should be controlled outside the Marketplace install action.

## Distribution Architecture

```text
VS Code Marketplace
  |
  | installs extension
  v
Runtime Tool Authorization Extension
  |
  | local policy / preview / demo / audit viewer
  v
Local project workspace
```

## Commercial Access Architecture

```text
Customer / Design Partner
  |
  | receives commercial access terms
  v
Manual License Activation
  |
  | maps customer, plan, machine, and entitlement state
  v
Runtime Tool Authorization premium boundary
```

Future provider adapters remain a separate Feature 015 implementation concern.

## Publish Flow

Manual publish flow:

```sh
cd vscode-extension
npm install
npm run compile
npx @vscode/vsce package
npx @vscode/vsce publish
```

Identity-based publish flow:

```sh
cd vscode-extension
npm install
npm run compile
npx @vscode/vsce package
npx @vscode/vsce publish --azure-credential
```

Do not run either publish command until explicit publish approval is received.

## First Commercial Motion

The first commercial motion should be simple:

1. Publish public extension.
2. Invite design partners/founding customers.
3. Keep install friction low.
4. Use manual license activation for paid access.
5. Track customer, plan, activation date, renewal date, and support contact outside the extension.
6. Move provider-neutral implementation from Feature 015 only after commercial validation.

## Safety And Trust Boundaries

- No telemetry by default.
- No remote calls in the extension for this feature.
- No live provider dependency in this feature.
- No hidden publish.
- No generated VSIX committed.
- No customer data committed.
- No production IAM claim.
- No compliance certification claim.

## Review Gate

Feature 017 can move to review once:

- publish runbook exists,
- commercial access runbook exists,
- extension metadata checklist is documented,
- current progress is updated,
- explicit publish command remains gated.
