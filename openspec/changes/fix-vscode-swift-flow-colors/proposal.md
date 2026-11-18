# Proposal

## Why

The Swift review found that `if`, `throw`, and `return` fall back to the generic keyword color in VS Code. They should use the approved control foreground.

## What Changes

Map the observed Swift control scopes and verify nearby declaration and type-related keywords.

## Capabilities

### New Capabilities

- `vscode-swift-flow-colors` provides the control foreground for the observed Swift statements.

### Modified Capabilities

None.

## Impact

VS Code generator, generated theme, and focused regression coverage.
