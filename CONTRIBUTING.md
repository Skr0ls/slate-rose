# Contributing

Keep changes small and reviewable. A feature should have a clear scope and
acceptance criteria that can be completed in one pull request. The approved
palette is immutable unless the project owner explicitly requests a change.
Split independent behaviors into separate pull requests, and start follow-up
work from the updated integration branch after its parent merges. Keep review
artifacts concise without imposing artificial line limits.
See [AGENTS.md](AGENTS.md) and the [design baseline](docs/design-baseline.md)
for project constraints.

## Git workflow

- `main` holds releases; `dev` is the integration branch.
- Create `feature/<small-scope>` from `dev` and open a pull request into
  `dev`.
- Create `release/*` from `dev`, open a pull request into `main`, and merge
  the release back into `dev`.
- Create a hotfix from `main` and merge it into both `main` and `dev`.
- The initial bootstrap may be committed directly to `main`; subsequent work
  uses feature pull requests. Publishing is never automatic.
- Rebase a small linear feature branch when it has no dependent branches; use
  a merge to preserve meaningful branch or integration history. After a remote
  rebase, start new features from the updated `origin/dev` without carrying
  pre-rebase commits forward.

## Collaboration and planning

The orchestrator decomposes OpenSpec work into tasks with acceptance criteria,
allowed files, non-goals, and verification. For a clear specification, use
`gpt-6.1-terra` at medium effort as executor; use `gpt-6.1-sol` at medium
effort if ambiguity persists. Resolve materially ambiguous requirements rather
than substituting a stronger model for a decision.

An independent reviewer works read-only, using `gpt-6.1-sol` at high effort by
default or medium for low-risk changes. The executor addresses findings; review
again after meaningful changes. The orchestrator integrates the result.

The active OpenSpec checklist is the source of truth for work. Issues are
optional and should not duplicate it as another task tracker. Archive completed
changes while retaining durable specifications. Delete obsolete archived plans
only in a separate, documented cleanup, without rewriting Git history.

## Local checks

Use Python 3.11 or newer for development; Python source must remain compatible
with 3.11. CI runs the checks with Python 3.11 and 3.14. Create a virtual environment,
install the pinned tools and hooks, and run the same checks as CI:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pre_commit install
python -m pre_commit run --all-files --show-diff-on-failure
python -m unittest discover -s tests -v
python -m generators validate
python -m generators check vscode
```

Run either Python hook separately when working on Python files:

```sh
python -m pre_commit run ruff-check --all-files
python -m pre_commit run ruff-format --all-files
```

The [local VSIX instructions](README.md#local-vs-code-installation) also describe
the package check. CI builds a downloadable VS Code artifact without publishing.

The formatter may modify files. Review and restage those changes, then rerun
the checks. Publishing is not automatic.
