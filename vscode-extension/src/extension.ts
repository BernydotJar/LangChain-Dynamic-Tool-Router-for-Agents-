import * as vscode from 'vscode';
import * as fs from 'node:fs/promises';
import * as path from 'node:path';

const OUTPUT_CHANNEL_NAME = 'Runtime Tool Authorization';

interface RuntimePolicy {
  version?: unknown;
  fallback_tool_name?: unknown;
  policies?: Record<string, unknown>;
}

interface PolicyValidationResult {
  ok: boolean;
  errors: string[];
  policy?: RuntimePolicy;
}

const starterPolicy = {
  version: 1,
  fallback_tool_name: 'not_authorized',
  policies: {
    search_docs: {
      allowed_plans: ['free', 'pro', 'enterprise']
    },
    fetch_customer_record: {
      allowed_plans: ['pro', 'enterprise'],
      required_permissions: ['records:read']
    },
    delete_customer_record: {
      allowed_plans: ['enterprise'],
      required_permissions: ['records:delete']
    }
  }
};

export function activate(context: vscode.ExtensionContext): void {
  const output = vscode.window.createOutputChannel(OUTPUT_CHANNEL_NAME);

  context.subscriptions.push(
    output,
    vscode.commands.registerCommand('runtimeToolAuth.initializePolicy', () => initializePolicy(output)),
    vscode.commands.registerCommand('runtimeToolAuth.validatePolicy', () => validatePolicyCommand(output)),
    vscode.commands.registerCommand('runtimeToolAuth.previewAuthorizedTools', () => previewAuthorizedTools(output)),
    vscode.commands.registerCommand('runtimeToolAuth.runDemo', () => runDemo()),
    vscode.commands.registerCommand('runtimeToolAuth.openAuditViewer', () => openAuditViewer(context))
  );
}

export function deactivate(): void {
  // No cleanup required.
}

async function initializePolicy(output: vscode.OutputChannel): Promise<void> {
  const workspaceRoot = getWorkspaceRoot();
  if (!workspaceRoot) {
    return;
  }

  const policyPath = getWorkspacePath('policyPath');

  try {
    await fs.access(policyPath);
    vscode.window.showInformationMessage(`Policy already exists: ${relativeToWorkspace(policyPath)}`);
    return;
  } catch {
    // File does not exist; create it below.
  }

  await fs.writeFile(policyPath, `${JSON.stringify(starterPolicy, null, 2)}\n`, 'utf8');
  output.appendLine(`Created starter policy: ${policyPath}`);
  vscode.window.showInformationMessage(`Created starter policy: ${relativeToWorkspace(policyPath)}`);
}

async function validatePolicyCommand(output: vscode.OutputChannel): Promise<void> {
  const result = await validatePolicy();

  output.show(true);
  output.appendLine('Runtime Tool Authorization policy validation');
  output.appendLine('------------------------------------------------');

  if (result.ok) {
    output.appendLine('PASS: policy shape is valid for developer-preview usage.');
    vscode.window.showInformationMessage('Runtime Tool Auth policy validation passed.');
    return;
  }

  output.appendLine('FAIL: policy shape is invalid.');
  for (const error of result.errors) {
    output.appendLine(`- ${error}`);
  }

  vscode.window.showErrorMessage(`Runtime Tool Auth policy validation failed: ${result.errors[0]}`);
}

async function previewAuthorizedTools(output: vscode.OutputChannel): Promise<void> {
  const result = await validatePolicy();

  if (!result.ok || !result.policy?.policies) {
    await validatePolicyCommand(output);
    return;
  }

  output.show(true);
  output.appendLine('Runtime Tool Authorization policy preview');
  output.appendLine('-----------------------------------------');

  for (const [toolName, config] of Object.entries(result.policy.policies)) {
    output.appendLine(`\nTool: ${toolName}`);
    if (isRecord(config)) {
      const allowedPlans = Array.isArray(config.allowed_plans) ? config.allowed_plans.join(', ') : 'not specified';
      const permissions = Array.isArray(config.required_permissions) ? config.required_permissions.join(', ') : 'none';
      output.appendLine(`  allowed_plans: ${allowedPlans}`);
      output.appendLine(`  required_permissions: ${permissions}`);
    } else {
      output.appendLine('  configuration: invalid or unsupported shape');
    }
  }
}

function runDemo(): void {
  const workspaceRoot = getWorkspaceRoot();
  if (!workspaceRoot) {
    return;
  }

  const config = vscode.workspace.getConfiguration('runtimeToolAuth');
  const pythonCommand = config.get<string>('pythonCommand') ?? 'python';
  const terminal = vscode.window.createTerminal({
    name: 'Runtime Tool Auth Demo',
    cwd: workspaceRoot
  });

  terminal.show(true);
  terminal.sendText(`${pythonCommand} examples/basic_agent/run_example.py`);
}

async function openAuditViewer(context: vscode.ExtensionContext): Promise<void> {
  const auditPath = getWorkspacePath('auditPath');

  let body: string;
  try {
    const raw = await fs.readFile(auditPath, 'utf8');
    body = prettyJson(raw);
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    body = `Audit file not found or unreadable: ${relativeToWorkspace(auditPath)}\n\n${message}`;
  }

  const panel = vscode.window.createWebviewPanel(
    'runtimeToolAuthAuditViewer',
    'Runtime Tool Auth Audit Viewer',
    vscode.ViewColumn.One,
    { enableScripts: false }
  );

  panel.webview.html = renderAuditHtml(body, context.extensionUri);
}

async function validatePolicy(): Promise<PolicyValidationResult> {
  const policyPath = getWorkspacePath('policyPath');
  const errors: string[] = [];

  let parsed: unknown;
  try {
    const raw = await fs.readFile(policyPath, 'utf8');
    parsed = JSON.parse(raw);
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    return { ok: false, errors: [`Unable to read or parse ${relativeToWorkspace(policyPath)}: ${message}`] };
  }

  if (!isRecord(parsed)) {
    return { ok: false, errors: ['Policy root must be a JSON object.'] };
  }

  if (typeof parsed.version !== 'number') {
    errors.push('Policy must include numeric `version`.');
  }

  if (typeof parsed.fallback_tool_name !== 'string' || parsed.fallback_tool_name.length === 0) {
    errors.push('Policy must include non-empty string `fallback_tool_name`.');
  }

  if (!isRecord(parsed.policies)) {
    errors.push('Policy must include object `policies`.');
  }

  return {
    ok: errors.length === 0,
    errors,
    policy: parsed as RuntimePolicy
  };
}

function getWorkspaceRoot(): string | undefined {
  const folder = vscode.workspace.workspaceFolders?.[0];
  if (!folder) {
    vscode.window.showErrorMessage('Open a workspace folder before using Runtime Tool Authorization.');
    return undefined;
  }

  return folder.uri.fsPath;
}

function getWorkspacePath(configKey: 'policyPath' | 'auditPath'): string {
  const workspaceRoot = getWorkspaceRoot();
  if (!workspaceRoot) {
    throw new Error('Workspace folder is required.');
  }

  const config = vscode.workspace.getConfiguration('runtimeToolAuth');
  const configuredPath = config.get<string>(configKey) ?? (configKey === 'policyPath' ? 'tool_policies.json' : 'runtime_audit_export.json');
  return path.resolve(workspaceRoot, configuredPath);
}

function relativeToWorkspace(absolutePath: string): string {
  const workspaceRoot = getWorkspaceRoot();
  if (!workspaceRoot) {
    return absolutePath;
  }

  return path.relative(workspaceRoot, absolutePath);
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value);
}

function prettyJson(raw: string): string {
  try {
    return JSON.stringify(JSON.parse(raw), null, 2);
  } catch {
    return raw;
  }
}

function renderAuditHtml(body: string, extensionUri: vscode.Uri): string {
  const escaped = escapeHtml(body);
  const nonce = Buffer.from(extensionUri.toString()).toString('base64').slice(0, 12);

  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'nonce-${nonce}';" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Runtime Tool Auth Audit Viewer</title>
  <style nonce="${nonce}">
    body {
      font-family: var(--vscode-editor-font-family);
      color: var(--vscode-editor-foreground);
      background: var(--vscode-editor-background);
      padding: 1rem;
    }
    pre {
      white-space: pre-wrap;
      word-break: break-word;
      border: 1px solid var(--vscode-panel-border);
      padding: 1rem;
      border-radius: 6px;
    }
  </style>
</head>
<body>
  <h1>Runtime Tool Auth Audit Viewer</h1>
  <pre>${escaped}</pre>
</body>
</html>`;
}

function escapeHtml(value: string): string {
  return value
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}
