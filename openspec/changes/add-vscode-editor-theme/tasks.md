# Tasks

## 1. Approved implementation baseline

- [x] 1.1 Record owner approval for the monorepository layout and Python generator in design.md; approved on 2026-11-16.
- [x] 1.2 Add the MIT license and document it in the README; verify LICENSE includes the copyright and permission notice.
- [ ] 1.3 Document implemented build/check entry points in the README; verify the commands run as written and paths match created files.
- [x] 1.4 Add pinned Python development tooling, Ruff lint/format hooks, and minimal pull request CI checks using the same local and CI commands; verify checks run on real files as they are added, without a fake test suite.

## 2. Palette validation

- [x] 2.1 Implement typed palette loading and validation with actionable errors; verify the canonical palette succeeds and malformed JSON, invalid metadata, missing/unknown/duplicate tokens and invalid hex fail.
- [x] 2.2 Add focused validator tests and command documentation; verify the tests pass and validation preserves the palette bytes.

## 3. VS Code generation

- [ ] 3.1 Implement explicit semantic and TextMate mappings using official VS Code documentation; verify representative roles use approved tokens and document unsupported distinctions alongside mappings.
- [ ] 3.2 Generate basic editor colors and document every provisional mapping; verify all keys are documented VS Code keys and no unapproved colors enter the output.
- [ ] 3.3 Implement deterministic build and read-only check commands; verify repeated output is byte-identical, stale output fails check mode without rewriting it, and invalid palettes fail before output is written.
- [ ] 3.4 Add a minimal declarative VS Code package with MIT metadata and license notice, plus local installation instructions; verify the built package contains the notice and Slate Rose is selectable in VS Code.

## 4. Cross-language acceptance

- [ ] 4.1 Add representative C++, C#, TypeScript and Python fixtures with documented expected roles; verify every fixture exposes types, functions, fields, declarations, flow control and literals.
- [ ] 4.2 Review fixtures in VS Code with relevant language providers and record provider versions, screenshots and coverage limitations; verify documentation distinguishes observed and unverified behavior.
- [ ] 4.3 Run the complete documented build/check flow from a clean output state; verify no palette changes and no unexplained generated diff remain.

## Workflow follow-up

- Archive after owner review and acceptance of the locally installable theme.
- Plan JetBrains, Zed, full workbench styling and release automation as separate changes after the first adapter is reviewed.
