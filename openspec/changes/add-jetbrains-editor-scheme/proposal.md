# Proposal

## Why

VS Code is implemented; JetBrains is the next adapter in the backlog. A standalone editor scheme provides a small, reviewable first step before UI and plugin packaging.

## What Changes

- Generate an importable `.icls` file using approved colors and IntelliJ Language Defaults.
- Add `build jetbrains` and read-only `check jetbrains`, preserving existing commands.
- Document import steps, fallback limitations and the separate native review follow-up.

## Capabilities

### New Capabilities

- `jetbrains-editor-scheme`: deterministic editor scheme generation and consistency checks.

### Modified Capabilities

None.

## Impact

Adds a small Python adapter, generated scheme, focused tests, one CI check and brief documentation. No UI theme, Kotlin plugin, terminal mapping, language-specific overrides, native acceptance or publication in this slice. Both approved palette sources and VS Code output remain unchanged.
