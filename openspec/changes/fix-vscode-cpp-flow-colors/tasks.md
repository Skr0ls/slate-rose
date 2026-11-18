# Tasks

## 1. Implementation and verification

- [x] 1.1 Add and regenerate the two C++ selectors. Verify a focused regression test fails before the mapping and passes afterward.
- [x] 1.2 Compare effective TextMate colors with the shipped VS Code engine and inspect the changed tokens in the editor where available. Record the verification context and any outstanding native checks.
- [x] 1.3 Run required checks and independent review, then prepare the PR into dev.

## Verification

VS Code 1.146.0 reported `#D7829B` for `if` at 13:10 and `for` at 17:10 on the same C++ fixture and test profile used for the [baseline](../../../previews/vscode/cpp-baseline/README.md). Both tokens had previously used `#CAA1DE`. The shipped TextMate engine reproduced the change and preserved the sampled colors for `class`, `int`, `throw`, and `return`.
