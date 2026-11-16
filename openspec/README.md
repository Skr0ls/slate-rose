# Planning and Backlog

The approved baseline is one repository, a shared Python generator, separate host packages and the MIT license. Palette values remain frozen in palette/colors.json.

## Current change

[add-vscode-editor-theme](changes/add-vscode-editor-theme/proposal.md) has a complete proposal, design, specifications and [implementation checklist](changes/add-vscode-editor-theme/tasks.md). Continue implementation with `$openspec-apply-change add-vscode-editor-theme` in Codex. Tasks are checked off only after their stated verification is complete.

The [delivery plan](delivery-plan.md) defines five stages: Python tooling, palette validation, VS Code generation, local packaging and visual acceptance. Visual review was delivered as a follow-up commit in the still-open package PR 4; a separate PR 5 branch is not needed. [CONTRIBUTING.md](../CONTRIBUTING.md) defines agent roles and branch/review rules.

## Follow-up backlog

These are queued work items, not active or approved implementation specifications. Create a dedicated OpenSpec change before starting each item, using the completed adapter's evidence to refine scope. The names below are reserved suggestions, not existing changes.

### 1. Basic continuous integration — `add-theme-ci`

Python quality tooling, palette validation and validator tests run in basic PR checks. Extend that baseline as each adapter lands.

- [x] Run generated-output checks on pull requests when generation is implemented. Stale artifacts fail CI.
- [ ] Build implemented host packages as downloadable CI artifacts. VS Code packaging is configured; local installation and license verification remain part of acceptance.

### 2. UI design — `define-workbench-states`

- [ ] Review cursor, active line, search, tabs, panels, menus, completion, focus and disabled states. Done when provisional mappings and any requested new colors have owner approval.
- [ ] Define diagnostic, Git/diff and terminal roles separately from approved syntax colors. Done when representative states have reviewed previews and contrast observations, with no automatic palette changes.
- [ ] Apply reviewed states to VS Code while preserving native layouts and interactions. Done when editor and surrounding UI are reviewed together.

### 3. JetBrains — `add-jetbrains-theme`

- [ ] Generate an editor color scheme and minimal UI theme resources from approved mappings. Done when they load in Rider and IntelliJ IDEA and language-specific differences are documented.
- [ ] Package a standalone theme plugin with MIT notice and installation instructions. Done when a local build installs successfully and fixtures are reviewed in the relevant IDEs.
- [ ] Add host validation and packaging to CI. Done when shared-input changes also validate the JetBrains output.

### 4. Zed — `add-zed-theme`

- [ ] Generate native theme JSON and extension.toml using the current official schema. Done when schema checks pass and the theme installs locally.
- [ ] Review syntax, completion, search, tabs and panels while preserving Zed's native UI character. Done when screenshots and the host coverage table record observed results and limitations.
- [ ] Add host validation and packaging to CI. Done when shared-input changes also validate Zed output.

### Language validation

- [ ] Work through the [language validation backlog](language-validation-backlog.md) in small, separately scoped changes. Done when each selected batch has the recorded review evidence and limitations described there.

### 5. Release preparation — `prepare-theme-releases`

- [ ] Choose package IDs, publisher identity, supported editor versions and release version policy. Done when manifests, compatibility notes and changelogs agree.
- [ ] Add installation guides, screenshots and a semantic-coverage comparison for every supported host. Done when a reviewer can install the artifacts from the documentation.
- [ ] Configure separately triggered VS Code and JetBrains publication jobs when publisher accounts are ready. Done when credentials are scoped to their host and a reviewed release can be published without rebuilding different inputs.
- [ ] Prepare Zed registry submission using the monorepository package path. Done when the registry accepts the extension and its published version is installable.

### Later candidates

- Visual Studio for Windows: investigate the current native distribution format before proposing an adapter.
- Neovim: optional adapter after the three primary hosts are stable.

## Local OpenSpec commands

```sh
openspec list
openspec status --change add-vscode-editor-theme
openspec validate add-vscode-editor-theme --strict
```

OpenSpec CLI must be available in the active PATH. Repository-local workflows are versioned under .agents/skills/.
