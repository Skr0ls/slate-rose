# Proposal

## Why

The original C# preview reported lilac flow keywords. The Microsoft C# provider exposes a distinct `controlKeyword` category for these words.

## What Changes

Map the C# semantic control keyword category to coral and verify the affected words in the existing fixture.

## Capabilities

### New Capabilities

- `vscode-csharp-flow-review` assigns the control foreground to C# semantic control keywords.

### Modified Capabilities

None.

## Impact

VS Code generator, generated theme, focused regression test, preview, and language backlog.
