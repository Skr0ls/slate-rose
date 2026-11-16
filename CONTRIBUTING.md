# Contributing

Keep changes small and reviewable. A feature should have a clear scope and
acceptance criteria that can be completed in one pull request. The approved
palette is immutable unless the project owner explicitly requests a change.
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

Install the hooks and run them across the repository:

```sh
uvx --from pre-commit==4.7.0 pre-commit install
uvx --from pre-commit==4.7.0 pre-commit run --all-files
```

Python Ruff checks, formatting, and semantic tests will arrive with the first
Python feature. No CI workflow or automatic publishing is configured yet.
