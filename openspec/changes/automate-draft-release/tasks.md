# Tasks

- [x] 1.1 Implement the manual draft workflow and document its use.
- [x] 1.2 Validate the workflow and its selection logic, obtain independent review, and prepare a PR into dev.

## Verification

The workflow passed actionlint and the GitHub Actions schema check. Local Git
and a mocked GitHub CLI exercised the main gate, tag ancestry, missing run,
asset validation, moved tag, existing draft, and normal draft arguments.
The live workflow can be dispatched once its definition reaches the default
branch and a release tag has a successful Quality run.
