# Tasks

- [x] 1.1 Implement the manual draft workflow and document its use.
- [x] 1.2 Validate the workflow and its selection logic, obtain independent review, and prepare a PR into dev.
- [x] 1.3 Verify the exact remote tag with Git, resolving annotated tags to their target commit. Check annotated, lightweight, missing, and moved tags.
- [ ] 1.4 Create a draft from the approved preview tag on GitHub and verify that its three attachments match the Quality bundle for that commit.

## Verification

The workflow passed actionlint and the GitHub Actions schema check. Local Git
and a mocked GitHub CLI exercised the main gate, tag ancestry, missing run,
asset validation, moved tag, existing draft, and normal draft arguments.
The preview dry-run verified the original bundle. The live draft step exposed
an HTTP 422 from the commit lookup for the annotated tag. Local Git tests
verified exact tag resolution for annotated and lightweight tags, rejected
missing and moved tags, and confirmed the existing-release guard.
