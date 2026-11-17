# Proposal

## Why

Java primitives currently appear as keywords in the initial IntelliJ review. Verify the host's actual lexical and semantic categories before promising a C#-style narrow override or expanding to other languages.

## What Changes

- Add a focused Java fixture for primitive declarations/usages, named and boxed types, and keyword controls.
- Record native category and appearance evidence on the existing isolated IntelliJ host, with its actual SDK, Java plugin and selected scheme.
- Document a supported narrow-selector candidate or a shared-category limitation; any mapping fix requires a separate change grounded in the findings.

## Capabilities

### New Capabilities

None. This is fixture and validation documentation work (`skip_specs: true`).

### Modified Capabilities

None. Existing theme behavior remains unchanged.

## Impact

Adds a small fixture under `fixtures/jetbrains/`, reproduction notes, compact evidence under `previews/jetbrains/java-primitives/` and a backlog link/status. No renderer, generated theme, palette, parser, runtime plugin or host preference changes. Execute from updated `dev` after C# PR #16 integrates; do not expand this review to Kotlin, Swift, VS Code or an IDE matrix.
