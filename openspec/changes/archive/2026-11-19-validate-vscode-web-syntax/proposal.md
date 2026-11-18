# Proposal

## Why

The VS Code theme needs observable evidence for JavaScript, JSX, and TSX before their highlighting can be described as reviewed. A focused review can identify language-specific mapping problems while preserving the approved palette.

## What Changes

- Add three small syntax fixtures and review lexical and available semantic highlighting separately in VS Code.
- Record per-file evidence, provider and host versions, project context, screenshots, limitations, and any narrowly evidenced mapping fixes.
- Begin implementation only after the pending package and fixture acceptance prerequisite (PR 4) is merged, from updated `origin/dev`.
- Leave PHP, Ruby, other languages, workbench colors, other editor adapters, licensing, and marketplace publication outside this change.

## Capabilities

### New Capabilities

- `vscode-web-validation`: Evidence-based validation of VS Code highlighting for JavaScript, JSX, and TSX.

### Modified Capabilities

None.

## Impact

Fixtures, VS Code review evidence, and potentially the VS Code generator and its regression tests are affected. The review uses the built-in JavaScript and TypeScript service and a packaged local artifact; no React dependency is required. The approved palette remains unchanged.
