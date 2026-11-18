# Tasks

- [x] 1.1 Add the schema and artifact job and document install from its download.
- [x] 1.2 Validate the workflow and schema locally, obtain independent review, and prepare the PR.
- [x] 1.3 Verify the CI artifact's installable directory layout and contents.

## Verification

The [first packaging run](https://github.com/Skr0ls/slate-rose/actions/runs/44398680619)
uploaded `slate-rose-zed`. The download contained exactly `extension.toml`,
`LICENSE`, `README.md`, and `themes/slate-rose.json`, with bytes matching
the checked-in package files.
