# Design

## Context

Only README.md, AGENTS.md and palette/colors.json exist as project inputs; there is no application architecture to preserve. See proposal.md for motivation. OpenSpec tracks changes locally, with Codex workflows installed under .agents/skills/.

## Goals / Non-Goals

**Goals:** A small shared generator, explicit host mappings and locally reviewable output. Keep editor interface conventions intact.

**Non-Goals:** A general theme framework, runtime extension logic, new palette values, full UI design or automated publication in this change.

## Decisions

The owner approved the monorepository layout and Python generator on 2026-11-16. The project uses the MIT license; include its notice in distributed host packages.

### One source repository with host packages

Retain palette/, generators/, fixtures/ and previews/ from the README. Use packages/vscode/, packages/jetbrains/ and packages/zed/ for each host's manifest and generated distributable resources; create directories only when their adapter is implemented. Generated resources live inside their host packages instead of a separate top-level themes/ directory.

Separate repositories would require palette synchronization and coordinated changes. A monorepository lets a single review cover shared input and host-specific consequences. Avoid workspace orchestration frameworks until needed.

### Shared Python generator

Use Python with the standard library, explicit mapping tables and full type hints. It can emit both JSON and XML without requiring three implementation languages. TypeScript is a viable alternative but adds a Node toolchain for the shared generator; Kotlin and Rust are unnecessary for declarative theme resources. Host packaging tools remain host-specific.

Generation must validate before writing, use fixed formatting and ordering, and avoid timestamps or machine-dependent paths. Keep shared validation independent of host-specific scope mappings. Use a separate read-only check mode for stale output detection.

### Declarative host artifacts

- VS Code: theme JSON plus package.json using contributes.themes; no extension activation code. First target only.
- JetBrains later: editor scheme XML/.icls, .theme.json and META-INF/plugin.xml; Gradle Kotlin DSL can package resources without Kotlin runtime source.
- Zed later: themes/*.json plus extension.toml; no Rust code for a theme-only extension. The official registry supports a monorepository subdirectory via its path field.

Official references checked on 2026-11-16:
- https://code.visualstudio.com/api/extension-guides/color-theme
- https://plugins.jetbrains.com/docs/intellij/theme-structure.html
- https://zed.dev/docs/extensions/themes
- https://zed.dev/docs/extensions/developing-extensions
- https://zed.dev/docs/extensions/publishing/publishing-guide

### Incremental delivery automation

Start with pinned Python quality tooling and minimal pull request checks using the same commands locally and in CI, before implementing the validator. Add meaningful validator/mapping checks, deterministic generation and manual IDE review as the implementation lands. A later CI change can build host packages as artifacts. Introduce separate release jobs when each package is ready; avoid publishing on every push. VS Code and JetBrains publication have separate credentials and release outcomes; Zed publication uses a registry PR and review. No atomic cross-store release is assumed.

## Risks / Trade-offs

- Language providers classify symbols differently → inspect fixtures with the actual installed language extensions and record coverage.
- The 24-token palette lacks some editor states → reuse approved tokens provisionally, document mappings and seek approval for any new colors.
- Shared source can affect multiple hosts → validate every implemented adapter when shared inputs change.
- Store requirements evolve → recheck official publishing requirements when each release adapter is implemented.

## Migration Plan

Implement the validator and VS Code adapter, regenerate artifacts and review local installation. There is no existing implementation to migrate. Roll back a generated package by restoring its last reviewed source and regenerating. Keep marketplace publication outside this first change.
