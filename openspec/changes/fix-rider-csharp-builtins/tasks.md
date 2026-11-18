# Tasks

## 1. Focused implementation

- [x] 1.1 From updated dev after Islands integration, add the exact C# builtin external-key override, regenerate the scheme, and add a regression assertion for primitive `D8B981`, unaffected keywords/types and every existing shared attribute; verify determinism, relevant unit tests and generator checks, and document the key and scope.
- [x] 1.2 Add the dedicated alias/negative-control fixture and disposable project instructions described in design.md; verify valid source/project loading with an installed SDK and document the selected version without executing the fixture.

## 2. Native acceptance

- [x] 2.1 Independently review the code and rebuilt/checkable JAR before installation; in the isolated Rider profile record before/after alias declaration/use categories and unaffected keyword, var, identifier and named-type controls using native color inspection, package hash/build/SDK and compact evidence; verify successful project loading and effective approved colors without changing host preferences.

## 3. Integration

- [x] 3.1 Run all unit tests/hooks, palette validation, VS Code/JetBrains editor/UI generator checks, package consistency check and strict OpenSpec validation; confirm palettes, UI JSON and VS Code artifact unchanged, obtain independent final review and open the implementation PR into dev.

## Workflow follow-up

- Archive after review and integration. Java primitives and Kotlin classifications are separate small changes; do not start Zed ahead of the language review queue.
