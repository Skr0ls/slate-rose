# Tasks

## 1. Prerequisite and artifact

- [ ] 1.1 Verify PR 4 is merged, update `origin/dev`, and create the implementation branch from it without carrying pre-rebase commits; record the merged commit and branch base. An open PR does not satisfy this task.
- [ ] 1.2 Build and install the package in an isolated VS Code profile, compare its installed theme JSON file byte-for-byte with the source-generated theme JSON, and record artifact identity and comparison result.

## 2. Fixtures and review

- [ ] 2.1 Add the three small fixtures specified in the design and inspect each for the applicable roles and distinct JSX/TSX constructs; document any minimal provider context without requiring a React dependency.
- [ ] 2.2 Review lexical highlighting for each fixture in its exact language mode, inspect problematic scopes, and record observations and screenshots under `previews/vscode/web`.
- [ ] 2.3 Review semantic highlighting for each fixture when its built-in provider is available; record actual host and provider versions, language modes, project context, token observations, screenshots, and separate per-file lexical and semantic statuses, explicitly identifying any limitations or blocks.

## 3. Corrections and integration

- [ ] 3.1 If review proves a mapping issue in these syntaxes, make only the evidenced correction and add a meaningful regression test, then rebuild and reinstall the corrected package, verify its installed JSON identity, repeat affected lexical and semantic inspections, and refresh screenshots and outcomes to describe the final artifact; otherwise verify generated output is unchanged. Document unsupported distinctions and verify the approved palette is byte-identical.
- [ ] 3.2 Run the documented palette validator, VS Code build and check, unit tests, and pre-commit checks; if the package artifact changed, run the real package check and verify the packaged theme JSON remains byte-identical to the generated theme JSON. Record results and unresolved limitations without broader coverage claims.
- [ ] 3.3 Obtain independent read-only review under CONTRIBUTING.md, resolve findings and re-review meaningful changes; verify the final checklist and evidence reflect the actual results.
