# Tasks

## 1. Standalone editor adapter

- [x] 1.1 Implement the documented XML mappings and generated `.icls`; verify parsed keys, palette-only values, XML escaping and deterministic bytes in focused tests; document import steps and inherited/native-review limitations.
- [x] 1.2 Add host-specific CLI build/check and CI consistency check; verify repeated build, read-only stale/missing checks, invalid-input failure and palette alias protections; document runnable commands and update the backlog link without closing broader JetBrains acceptance.

## 2. Integration verification

- [x] 2.1 Run the complete tests, hooks, both host checks and strict OpenSpec validation; confirm palettes and VS Code output are byte-identical to `origin/dev`, then obtain independent review.

## Workflow follow-up

- Open a small PR into `dev`; native Rider/IntelliJ fixture review and any language-specific adjustments are the next separate slice.
