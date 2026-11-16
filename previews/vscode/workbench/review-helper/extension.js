const vscode = require('vscode');
const fs = require('fs');
const path = require('path');
const root = '/tmp/sr-web-context/javascript/ui-review';
exports.activate = async function(context) {
  const uri = vscode.Uri.file(path.join(root, 'workbench.ts'));
  const diagnostics = vscode.languages.createDiagnosticCollection('slate-rose-ui-review');
  context.subscriptions.push(diagnostics);
  const definitions = [
    [4, vscode.DiagnosticSeverity.Error, 'Review error: demonstrate error decoration'],
    [5, vscode.DiagnosticSeverity.Warning, 'Review warning: demonstrate warning decoration'],
    [6, vscode.DiagnosticSeverity.Information, 'Review information: demonstrate information decoration'],
    [7, vscode.DiagnosticSeverity.Hint, 'Review hint: demonstrate hint decoration']
  ];
  diagnostics.set(uri, definitions.map(([line, severity, message]) => {
    const item = new vscode.Diagnostic(new vscode.Range(line, 6, line, 12), message, severity);
    item.source = 'Slate Rose UI review (synthetic)';
    return item;
  }));
  context.subscriptions.push(vscode.languages.registerHoverProvider({language:'typescript'}, {
    provideHover() { return new vscode.Hover(new vscode.MarkdownString('**Slate Rose UI review**\n\nSynthetic hover content for foreground, background and border inspection.')); }
  }));
  async function editor() {
    const doc = await vscode.workspace.openTextDocument(uri);
    return await vscode.window.showTextDocument(doc, {preview:false});
  }
  context.subscriptions.push(vscode.commands.registerCommand('slateReview.overview', async () => {
    await vscode.window.showTextDocument(vscode.Uri.file(path.join(root,'reference.ts')), {preview:false});
    const view = await editor();
    view.selection = new vscode.Selection(10, 8, 10, 13);
    await vscode.commands.executeCommand('workbench.view.explorer');
    await vscode.commands.executeCommand('workbench.actions.view.problems');
    await vscode.commands.executeCommand('workbench.action.focusActiveEditorGroup');
  }));
  context.subscriptions.push(vscode.commands.registerCommand('slateReview.diff', async () => {
    await vscode.commands.executeCommand('vscode.diff', vscode.Uri.file(path.join(root,'before.ts')), vscode.Uri.file(path.join(root,'after.ts')), 'Slate Rose UI Review: before ↔ after', {preview:false});
  }));
  context.subscriptions.push(vscode.commands.registerCommand('slateReview.completion', async () => {
    const view = await editor();
    view.selection = new vscode.Selection(18, 7, 18, 7);
    view.revealRange(new vscode.Range(18,0,18,7));
    await vscode.commands.executeCommand('editor.action.triggerSuggest');
  }));
  context.subscriptions.push(vscode.commands.registerCommand('slateReview.hover', async () => {
    const view = await editor();
    view.selection = new vscode.Selection(10, 9, 10, 9);
    await vscode.commands.executeCommand('editor.action.showHover');
  }));
  context.subscriptions.push(vscode.commands.registerCommand('slateReview.exportTheme', async () => {
    await vscode.commands.executeCommand('workbench.action.generateColorTheme');
    const document = vscode.window.activeTextEditor?.document;
    if (document) fs.writeFileSync('/tmp/sr-ui-native-theme.jsonc', document.getText());
  }));
  function writeState() {
    fs.writeFileSync('/tmp/sr-ui-probe-state.json', JSON.stringify({
    version:vscode.version, trusted:vscode.workspace.isTrusted,
    theme:vscode.workspace.getConfiguration('workbench').get('colorTheme'),
    titleBarStyle:vscode.workspace.getConfiguration('window').get('titleBarStyle'),
    modernUI:vscode.workspace.getConfiguration('workbench').get('experimental.modernUI'),
    windowFocused:vscode.window.state.focused,
    colorCustomizations:vscode.workspace.getConfiguration('workbench').get('colorCustomizations'),
    extension:vscode.extensions.getExtension('skr0ls.slate-rose')?.extensionPath,
    fixture:uri.fsPath, diagnostics:definitions.length
    },null,2)+'\n');
  }
  context.subscriptions.push(vscode.window.onDidChangeWindowState(writeState));
  await editor();
  writeState();
};
