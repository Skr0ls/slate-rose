# Proposal

## Why

Slate Rose currently has an approved palette and design documentation but no installable theme. A small VS Code editor slice will establish reproducible generation and expose semantic highlighting limitations before adding JetBrains and Zed.

## What Changes

- Establish pinned Python quality tooling, Ruff hooks and minimal pull request checks before implementing the validator.
- Validate the approved palette and reject malformed or unknown tokens.
- Generate a VS Code editor theme with lexical and semantic mappings and basic editor colors.
- Add C++, C#, TypeScript and Python fixtures, local installation instructions and a deterministic check command.
- Use the approved lightweight monorepository layout with shared inputs, a Python generator and separate host packaging.
- Defer full workbench styling, new colors, other adapters and marketplace publishing.

## Capabilities

### New Capabilities

- `palette-validation`: Validate the canonical palette without modifying it.
- `vscode-editor-theme`: Generate and locally install a theme that preserves the approved semantic roles.

### Modified Capabilities

None. There are no existing specifications.

## Impact

Adds a shared validation/generation entry point, a VS Code adapter, generated artifacts and fixtures. The owner approved the Python generator and packaging layout described in design.md on 2026-11-16. The project uses the MIT license. No remote repositories or marketplace accounts are changed.
