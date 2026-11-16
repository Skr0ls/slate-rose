const vscode = require('vscode');
const fs = require('fs');

function display() {
  const reset = '\x1b[0m';
  const names = ['Black', 'Red', 'Green', 'Yellow', 'Blue', 'Magenta', 'Cyan', 'White'];
  const lines = [
    'SLATE ROSE / INTEGRATED TERMINAL',
    'Controlled PTY display only; no shell process or fixture execution.',
    '',
    'NORMAL FOREGROUND            BRIGHT FOREGROUND            NORMAL BACKGROUND     BRIGHT BACKGROUND',
  ];
  names.forEach((name, index) => {
    const normal = `${name}  Aa / build 0123`.padEnd(29);
    const bright = `${name}  Aa / build 0123`.padEnd(29);
    const text = index === 0 ? 37 : 30;
    lines.push(`\x1b[${30 + index}m${normal}${reset}\x1b[${90 + index}m${bright}${reset}\x1b[${text};${40 + index}m ${name.padEnd(18)} ${reset}  \x1b[${text};${100 + index}m ${name.padEnd(18)} ${reset}`);
  });
  lines.push('', 'BOLD: normal ANSI inputs; effective bright-color preference is recorded.');
  lines.push(names.map((name, index) => `\x1b[1;${30 + index}m${name.padEnd(12)}${reset}`).join(''));
  lines.push('', '\x1b[7m REVERSE DEFAULT TEXT \x1b[0m  Default foreground / background restored.');
  lines.push('', 'Selection target: Slate Rose terminal selection remains readable.',
    'Search target: rose terminal match one.',
    'Search target: rose terminal match two.',
    '', 'Cursor ready> ');
  return lines.join('\r\n');
}

exports.activate = async function(context) {
  let terminal;
  function report() {
    const integrated = vscode.workspace.getConfiguration('terminal.integrated');
    fs.writeFileSync('/tmp/sr-term-state.json', JSON.stringify({
      hostVersion: vscode.version,
      reviewProfileStorage: context.globalStorageUri.fsPath,
      theme: vscode.workspace.getConfiguration('workbench').get('colorTheme'),
      customizations: vscode.workspace.getConfiguration('workbench').get('colorCustomizations'),
      modernUI: vscode.workspace.getConfiguration('workbench').get('experimental.modernUI'),
      titleBarStyle: vscode.workspace.getConfiguration('window').get('titleBarStyle'),
      trusted: vscode.workspace.isTrusted,
      windowFocused: vscode.window.state.focused,
      minimumContrastRatio: integrated.get('minimumContrastRatio'),
      drawBoldTextInBrightColors: integrated.get('drawBoldTextInBrightColors'),
      cursorStyle: integrated.get('cursorStyle'),
      cursorBlinking: integrated.get('cursorBlinking'),
      themePath: vscode.extensions.getExtension('skr0ls.slate-rose')?.extensionPath,
      display: 'review-only Pseudoterminal; no shell process'
    }, null, 2) + '\n');
  }
  function show() {
    if (!terminal) {
      const writer = new vscode.EventEmitter();
      context.subscriptions.push(writer);
      terminal = vscode.window.createTerminal({name: 'Slate Rose ANSI review', pty: {
        onDidWrite: writer.event,
        open() { writer.fire(display()); },
        close() {}
      }});
      context.subscriptions.push(terminal);
    }
    terminal.show();
    report();
  }
  context.subscriptions.push(vscode.commands.registerCommand('slateTerminal.show', show));
  async function exportTheme() {
    fs.writeFileSync('/tmp/sr-term-export-status.json', JSON.stringify({stage:'started'}));
    await vscode.commands.executeCommand('workbench.action.generateColorTheme');
    const document = vscode.window.activeTextEditor?.document;
    if (document) fs.writeFileSync('/tmp/sr-term-native-theme.jsonc', document.getText());
    report();
    fs.writeFileSync('/tmp/sr-term-export-status.json', JSON.stringify({stage:'complete',document:document?.uri.toString()}));
  }
  context.subscriptions.push(vscode.commands.registerCommand('slateTerminal.export', exportTheme));
  context.subscriptions.push(vscode.window.onDidChangeWindowState(report));
  const doc = await vscode.workspace.openTextDocument('/Users/skr0l/projects/open_src/slate_rose/palette/terminal.json');
  await vscode.window.showTextDocument(doc, {preview:false});
  show();
  if (fs.existsSync('/tmp/sr-term-export-once')) {
    fs.unlinkSync('/tmp/sr-term-export-once');
    try { await exportTheme(); }
    catch (error) { fs.writeFileSync('/tmp/sr-term-export-status.json', JSON.stringify({stage:'failed',error:String(error)})); }
  }
};
