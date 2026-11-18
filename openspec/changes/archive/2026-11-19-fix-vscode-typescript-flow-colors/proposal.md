# Proposal

## Why

The TypeScript baseline found that `if`, `for`, and `throw` use the generic keyword foreground in VS Code. They should use the approved control foreground.

## What Changes

Map the bundled TypeScript grammar scopes responsible for these three statements.

## Capabilities

### New Capabilities

- `vscode-typescript-flow-colors` assigns the control foreground to the observed TypeScript statement scopes.

### Modified Capabilities

None.

## Impact

VS Code generator, generated theme, and focused regression coverage.
