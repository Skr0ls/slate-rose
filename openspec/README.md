# Planning and Backlog

The approved baseline is one repository, a shared Python generator, separate host packages and the MIT license. Palette values remain frozen in palette/colors.json.

## Current change

[fix-rider-csharp-builtins](changes/fix-rider-csharp-builtins/tasks.md) tracks the focused alias mapping and native Rider review. The Islands shell and local package are integrated.

[validate-jetbrains-editor-scheme](changes/validate-jetbrains-editor-scheme/tasks.md) records bounded C# review on Rider and one Java import smoke check on IntelliJ. The [initial adapter](changes/add-jetbrains-editor-scheme/tasks.md) is integrated.

[add-vscode-terminal-colors](changes/add-vscode-terminal-colors/proposal.md) implements the owner-approved ANSI design. Workbench appearance is accepted; native terminal acceptance remains pending.

[add-vscode-editor-theme](changes/add-vscode-editor-theme/tasks.md) and [define-workbench-states](changes/define-workbench-states/tasks.md) retain completed implementation checklists. Archive completed changes after their review and integration requirements are satisfied. Tasks are checked off only after their stated verification is complete.

The [delivery plan](delivery-plan.md) defines five stages: Python tooling, palette validation, VS Code generation, local packaging and visual acceptance. Visual review was delivered as a follow-up commit in the still-open package PR 4; a separate PR 5 branch is not needed. [CONTRIBUTING.md](../CONTRIBUTING.md) defines agent roles and branch/review rules.

## Follow-up backlog

These are queued work items, not active or approved implementation specifications. Create a dedicated OpenSpec change before starting each item, using the completed adapter's evidence to refine scope. The names below are reserved suggestions, not existing changes.

### 1. Basic continuous integration — `add-theme-ci`

Python quality tooling, palette validation and validator tests run in basic PR checks. Extend that baseline as each adapter lands.

- [x] Run generated-output checks on pull requests when generation is implemented. Stale artifacts fail CI.
- [x] Build all three host packages as downloadable CI artifacts. See the [release bundle](../docs/releasing.md).

### 2. UI design — `define-workbench-states`

The [workbench change](changes/define-workbench-states/proposal.md) implements the accepted palette allocation; the [native review](../previews/vscode/workbench/README.md) records the tested workbench slice. Terminal ANSI is tracked in [add-vscode-terminal-colors](changes/add-vscode-terminal-colors/tasks.md). The broader checkboxes below retain remaining state coverage and terminal implementation acceptance.

- [ ] Review cursor, active line, search, tabs, panels, menus, completion, focus and disabled states. Done when provisional mappings and any requested new colors have owner approval.
- [ ] Define diagnostic, Git/diff and terminal roles separately from approved syntax colors. Done when representative states have reviewed previews and contrast observations, with no automatic palette changes.
- [ ] Apply reviewed states to VS Code while preserving native layouts and interactions. Done when editor and surrounding UI are reviewed together.

### 3. JetBrains — `add-jetbrains-theme`

The initial editor scheme is tracked in [add-jetbrains-editor-scheme](changes/add-jetbrains-editor-scheme/tasks.md); the broader acceptance below remains open.

The Islands UI plugin is integrated. The [focused C# review](../previews/jetbrains/csharp-builtins/README.md) records alias styling; Java, Kotlin and Swift reviews follow in the [language backlog](language-validation-backlog.md). Start each implementation from updated `dev` after its predecessor integrates.

- [ ] Generate an editor color scheme and minimal UI theme resources from approved mappings. Done when they load in Rider and IntelliJ IDEA and language-specific differences are documented.
- [ ] Package a standalone theme plugin with MIT notice and installation instructions. Done when a local build installs successfully and fixtures are reviewed in the relevant IDEs.
- [x] Validate generated JetBrains output and package the plugin in CI.

### 4. Zed — `add-zed-theme`

The [initial theme package](../packages/zed/README.md) is tracked in
[add-zed-theme](changes/add-zed-theme/tasks.md). Continue focused language
follow-ups from the [language backlog](language-validation-backlog.md) as
concrete mapping gaps arise.

- [x] Generate native theme JSON and provide an extension manifest. The official schema check and local install passed.
- [ ] Review syntax, completion, search, tabs and panels while preserving Zed's native UI character. Done when screenshots and the host coverage table record observed results and limitations.
- [x] Check generated Zed output for drift in the Quality workflow.
- [x] Validate the official schema in CI and upload the installable `slate-rose-zed` development extension artifact.

### Language validation

- [ ] Work through the [language validation backlog](language-validation-backlog.md) in small, separately scoped changes. Done when each selected batch has the recorded review evidence and limitations described there.

### 5. Release preparation — `prepare-theme-releases`

- [x] Assemble the three validated assets in one CI bundle and document draft releases. See [prepare-release-assets](changes/archive/2026-11-19-prepare-release-assets/tasks.md) and the [release guide](../docs/releasing.md).
- [ ] Verify a manual draft-release dispatch on `main` for an approved tag. The [workflow change](changes/automate-draft-release/tasks.md) documents the implementation.
- [ ] Choose package IDs, publisher identity, supported editor versions and release version policy. Done when manifests, compatibility notes and changelogs agree.
- [ ] Add installation guides, screenshots and a semantic-coverage comparison for every supported host. Done when a reviewer can install the artifacts from the documentation.
- [ ] Configure separately triggered VS Code and JetBrains publication jobs when publisher accounts are ready. Done when credentials are scoped to their host and a reviewed release can be published without rebuilding different inputs.
- [ ] Prepare Zed registry submission using the monorepository package path. Done when the registry accepts the extension and its published version is installable.

### Repository cleanup

- [ ] Archive completed OpenSpec changes in small batches. Preserve durable
  requirements and repair links to evidence and current checklists.
- [ ] Consolidate duplicated host instructions into the package guides and
  organize review evidence by editor. Keep extension paths stable for CI and
  marketplace submissions.

### Later candidates

- Xcode: investigate the native theme format, supported editor/UI surfaces and local installation before proposing a separate adapter.
- Visual Studio for Windows: investigate the current native distribution format before proposing an adapter.
- Neovim: optional adapter after the three primary hosts are stable.

## Local OpenSpec commands

```sh
openspec list
openspec status --change add-vscode-terminal-colors
openspec validate add-vscode-terminal-colors --strict
```

OpenSpec CLI must be available in the active PATH. Repository-local workflows are versioned under .agents/skills/.
