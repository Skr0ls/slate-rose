# Design

## Context

The VS Code generator produces deterministic JSON from lexical and semantic role mappings; semantic highlighting is enabled. Existing automated shape checks cannot establish what a running editor and its language service actually display. See the proposal and web-validation spec for scope and acceptance.

## Goals / Non-Goals

**Goals:** Make each reviewed layer reproducible, traceable to an installed artifact, and candid about provider limitations.

**Non-Goals:** Redesign the palette or broadly redesign mappings. Do not change existing OpenSpec checklists or declare the broader web-language batch complete.

## Decisions

1. **Wait for the package prerequisite.** PR 4 must be merged before creating an implementation branch from updated `origin/dev`; an open PR is insufficient. Do not carry historical pre-rebase commits forward. This ensures the installed artifact and acceptance process exist before review; cherry-picking a pending prerequisite would obscure its final identity.
2. **Review three independent fixtures.** Use `showcase.js`, `showcase.jsx`, and `showcase.tsx` in the exact modes `javascript`, `javascriptreact`, and `typescriptreact`. Exercise functions (blue), properties (rose), types where applicable (sand), declaration keywords (lilac), flow control including return, throw, and await (coral), strings (green), numbers (amber), and ordinary variables and constant bindings in the foreground. In member access, distinguish rose properties from quiet root variables and punctuation. Inspect component versus intrinsic JSX tags, attributes, props, and embedded expressions separately. Expect only distinctions the actual provider supports; avoid inventing colors or claiming a role where no distinction is available.
3. **Use minimal provider context.** Use the built-in JavaScript/TypeScript service and record the actual provider, version, host version, and workspace context. No React installation is required. If the service needs context, use only a minimal temporary JSX configuration and React stub or a local `declare JSX` namespace for TSX, recording exactly what was used. A guessed provider or ambiguous resolution cannot establish a semantic pass. A full application or dependency install would add unrelated variables.
4. **Compare artifact and review layers.** In an isolated profile install the locally built package, compare the installed theme JSON file byte for byte against the source-generated theme JSON, and record identity. This comparison concerns the installed file, not the editor's expanded active-theme export, which includes defaults. Review lexical results for every file and semantic results whenever the provider is available, using token inspection for problematic examples. Record a per-file, per-layer matrix and screenshots under `previews/vscode/web`; screenshots are manual evidence, not automated tests. This is stronger than assuming generated JSON matches installed behavior.
5. **Fix only demonstrated issues.** If inspection establishes a web-specific discrepancy, adjust only the relevant VS Code mapping and add a meaningful regression test. Rebuild and reinstall the corrected package, verify its installed JSON identity, repeat affected lexical and semantic inspections, and refresh screenshots and outcomes so evidence describes the final artifact. Do not introduce generic semantic keyword overrides or disable semantic highlighting globally. If no mapping changes, verify generation remains unchanged. Preserve the palette byte-for-byte in either case.

## Risks / Trade-offs

- Provider behavior or token distinctions can vary by host and context → record actual versions and evidence; label unresolved cases limited or blocked rather than passed.
- Fixture configuration can affect semantic resolution → record the precise minimal context and verify the actual language mode and provider.
- A narrowly scoped mapping can affect other languages → inspect the relevant mapping and add a regression test when it changes; avoid speculative redesign.

## Migration Plan

No deployed migration is required. Review and merge the small implementation change through the normal feature-to-dev workflow; revert its changes if necessary.
