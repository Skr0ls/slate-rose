# Proposal

## Why

Slate Rose currently colors editor content while most surrounding VS Code UI inherits default colors. The owner approved extending the existing palette across UI states so the editor and workbench feel coherent without changing native interactions.

## What Changes

- Generate approved workbench surface, tab, sidebar, panel, input, popup, focus, selection, search, scrollbar, diagnostic and diff colors.
- Derive transparent overlays only from existing palette RGB values; preserve palette bytes and syntax mappings.
- Retain operating-system window decorations and user title-bar settings. Do not force a custom title bar or inject CSS.
- Record local installed-theme UI review, reproducible package checks and mapping limitations.
- Keep terminal ANSI colors as a separate follow-up; terminal UI surfaces may follow panel colors.

## Capabilities

### New Capabilities

- `vscode-workbench-states`: Palette-derived workbench colors and observable UI state distinctions in VS Code.

### Modified Capabilities

None. Existing editor syntax behavior remains unchanged.

## Impact

VS Code generator, generated theme, focused generator tests, mapping/install documentation and native preview evidence. No runtime extension code, dependencies, other editor adapters, marketplace publishing or settings changes for users.
