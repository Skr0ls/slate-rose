# Tasks

## 1. UI resources and local package

- [x] 1.1 Generate the approved 16-key Islands shell and add the independent CLI target; verify roles, deterministic output, invalid inputs, alias guards and read-only checks with focused tests and document scope/commands.
- [x] 1.2 Add the resource-only descriptor and deterministic JAR build/check, license and CI artifact; verify resource references, stale/invalid-source failure before writes, input alias protection and byte-identical repeated packaging; document disk installation.

## 2. Native Rider verification

- [ ] 2.1 After code review, install/select the concrete package in the isolated Rider test context and record representative active/inactive shell framing and tabs with package hash/version and limitations; preserve native layout and preferences.

  Installation and editor/tool-window focus evidence are recorded in
  [the partial Rider review](../../../previews/jetbrains/islands/README.md).
  Whole-window inactivity remains unverified.

## 3. Integration

- [x] 3.1 Run all tests/hooks, three generator checks, package check and strict OpenSpec validation; confirm both palettes and existing generated editor artifacts unchanged, obtain independent final review and open a small PR into dev.

## Workflow follow-up

- UI controls/menus and semantic fixes remain separate changes. Archive after review and integration.
