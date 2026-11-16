# Tasks

## 1. Palette-derived mappings

- [x] 1.1 Implement the approved opaque workbench mappings and explicit alpha overlays, regenerate output and document every emitted UI key/opacity against current official docs; verify palette bytes and syntax maps remain unchanged and all keys are supported by the package minimum host or explicitly resolve compatibility.
- [x] 1.2 Add focused emitted-output regressions for state distinctions, overlay RGB/alpha constraints and syntax preservation; run tests and deterministic generator build/check, and update installation/status docs without claiming owner acceptance.

## 2. Installed UI review

- [x] 2.1 Build fixed-metadata VSIX twice, verify byte identity, inspect package and install in an isolated profile; record generated, packaged and installed theme identity and host version.
- [x] 2.2 Inspect installed sidebar/panel/tabs, active/inactive selection and focus, input/hover/completion, scrollbar hover, search, diagnostics and diff states; save representative native screenshots and an honest state matrix with contrast observations, native chrome preservation and remaining unreviewed behavior.

## 3. Integration

- [x] 3.1 Run validator, generator build/check, unit tests, hooks, strict OpenSpec validation and VSIX checks; confirm palette and syntax preservation and clean generated output.
- [x] 3.2 Obtain independent read-only review of implementation and native evidence, resolve findings and re-review meaningful fixes; verify task completion accurately reflects results.

## 4. Modern UI framing correction

- [x] 4.1 Add the approved Modern UI shell/frame and custom title-bar color mappings with focused emitted-output regressions and exact key/version documentation; verify unchanged palette, syntax and unrelated UI mappings against the first workbench commit.
- [x] 4.2 Rebuild and install the corrected VSIX, verify repeated package identity and installed theme bytes, and retain native Modern UI active/inactive window framing evidence with updated hashes and honest platform/version limits.
- [x] 4.3 Run integration checks and independent read-only review of the correction, resolve findings, and verify the complete checklist and review documents reflect final artifacts.

## Workflow follow-up

- Open a small PR into dev; do not merge or publish automatically.
- Owner acceptance and merge precede archive with durable capability specs retained.
- Keep terminal ANSI design as a separate backlog item.
