# Delivery Plan

This plan splits the current theme change into small PRs. The [change checklist](changes/add-vscode-editor-theme/tasks.md) remains the task source of truth; this document defines PR boundaries and executor handoffs. Follow [CONTRIBUTING.md](../CONTRIBUTING.md) for roles and Gitflow.

## Before every executor handoff

The orchestrator supplies the exact change requirements, checklist items, base branch, allowed files, non-goals, acceptance examples and verification commands. The executor reports the diff, checks run and unresolved limitations. The reviewer checks the resulting diff independently against that contract. Resolve material ambiguity before coding.

## PR 1 — Python quality tooling

- Branch: `feature/python-quality` from `dev`.
- Checklist: current change 1.4.
- Scope: development dependency configuration, Ruff lint/format hooks, a minimal PR CI job and contributor commands. Keep the generator itself standard-library-only.
- Acceptance: pinned tool versions; lint/format checks target actual Python files as they arrive; CI and local checks use the same configuration. Basic JSON/YAML and whitespace checks already exist in bootstrap.
- Verification: execute all configured checks; verify hook installation in a disposable clone. Do not invent production logic or empty test suites to make checks appear useful.
- Non-goals: palette validation, theme generation, marketplaces or release credentials.

## PR 2 — Palette validator

- Branch: `feature/palette-validation` from updated `dev`.
- Checklist: current change section 2 and the applicable build/check documentation in 1.3.
- Scope: shared palette loader/validator, CLI validation entry point, focused tests and usage documentation.
- Acceptance: canonical palette passes unchanged; malformed JSON, invalid metadata, missing/unknown/duplicate tokens and malformed hex fail with actionable messages and nonzero exit codes. Validate each case using a temporary input, never by modifying the approved palette.
- Verification: relevant tests, Ruff, hooks, documented CLI commands and before/after palette byte comparison.
- Non-goals: host-specific mappings or generated theme packages.

## PR 3 — VS Code generation

- Branch: `feature/vscode-generation` from updated `dev`.
- Checklist: current change 3.1–3.3 and related documentation in 1.3.
- Scope: explicit semantic/TextMate mappings, basic editor colors, generated JSON and deterministic build/check commands.
- Acceptance: documented official keys and approved palette references; semantic categories remain distinct where the host supports them; unavailable distinctions and provisional editor mappings are documented. No new palette colors.
- Verification: meaningful mapping assertions, byte-identical repeated builds, stale-output check failure without rewriting, invalid-input failure before writing, lint and hooks.
- Non-goals: marketplace packaging, full workbench or other editor adapters.

## PR 4 — Local VS Code package and fixtures

- Branch: `feature/vscode-package` from updated `dev`.
- Checklist: current change 3.4 and 4.1.
- Scope: extension manifest, local packaging instructions, MIT notice and four small original language fixtures.
- Acceptance: locally installable package with the correct license notice; fixtures exercise the required roles without unrelated application scaffolding.
- Verification: build and inspect the package, follow installation instructions, lint and hooks. Record actual IDE verification separately from automated artifact checks.
- Non-goals: publication or new colors.

## PR 5 — Visual acceptance

- Branch: `feature/vscode-visual-review` from updated `dev`.
- Checklist: current change 4.2–4.3.
- Scope: screenshots, language-provider/version notes, semantic coverage and minimal fixes demonstrated by fixture review.
- Acceptance: observed behavior is distinguished from unverified coverage; documented clean build/check flow passes; approved palette bytes remain unchanged.
- Verification: review real fixtures in VS Code and run the complete documented check flow. If the required IDE/provider is unavailable, keep that checklist item open and report the missing prerequisite.
- Non-goals: claiming full semantic parity based only on JSON validation.

## After acceptance

Archive the completed change and retain its durable capability specs. Create separate changes for full workbench design, JetBrains, Zed and release automation using the [backlog](README.md). Remove obsolete archived plans only in explicit cleanup PRs; preserve requirements, current guidance and useful attribution.
