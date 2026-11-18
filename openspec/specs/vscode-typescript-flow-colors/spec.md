# vscode-typescript-flow-colors Specification

## Purpose

Define how VS Code colors TypeScript control statements.

## Requirements

### Requirement: TypeScript statements use the control foreground

The VS Code theme SHALL assign the approved control foreground to the bundled TypeScript conditional, loop, and exception statement scopes.

#### Scenario: TypeScript fixture statements

- **WHEN** the bundled grammar classifies `if`, `for`, and `throw` in the TypeScript fixture
- **THEN** their foreground is coral
- **AND** declaration keywords keep the lilac foreground
- **AND** existing control mappings for other languages remain in effect
