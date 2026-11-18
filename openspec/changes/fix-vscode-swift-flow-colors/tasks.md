# Tasks

## 1. Implementation and verification

- [x] 1.1 Check shared Swift scopes, add the narrow rules, regenerate the theme, and verify the focused test fails before and passes afterward.
- [x] 1.2 Compare the existing Swift fixture with the shipped TextMate engine and the editor inspector where available. Record controls and verification context.
- [x] 1.3 Run project checks and independent review, then prepare the PR into dev.

## Verification

With the rebuilt VSIX in the VS Code 1.146.0 test profile, the inspector reported `#D7829B` for `if` (28:10), `throw` (29:14), and `return` (31:10) on the [Swift fixture](../../../previews/vscode/swift/README.md). The same positions had used `#CAA1DE`. The inspector reported lilac for `throws` (27:26) and `any` (45:25).

The shipped TextMate engine also verified that generic `where`, enum `case`, `throws`, `rethrows`, `any`, and opaque `some` retain lilac. The new selectors also cover other Swift tokens that the grammar assigns to these same control scopes, such as `try` and switch `case`.
