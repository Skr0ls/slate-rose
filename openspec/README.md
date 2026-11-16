# Planning and Backlog

The approved baseline is one repository, a shared Python generator, separate host packages and the MIT license. Palette values remain frozen in palette/colors.json.

## Current change

[add-vscode-editor-theme](changes/add-vscode-editor-theme/proposal.md) has a complete proposal, design, specifications and [implementation checklist](changes/add-vscode-editor-theme/tasks.md). Start implementation with `$openspec-apply-change add-vscode-editor-theme` in Codex. Tasks are checked off only after their stated verification is complete.

The [delivery plan](delivery-plan.md) defines five small PRs: Python tooling, palette validation, VS Code generation, local packaging and visual acceptance. [CONTRIBUTING.md](../CONTRIBUTING.md) defines agent roles and branch/review rules.

## Follow-up backlog

These are queued work items, not active or approved implementation specifications. Create a dedicated OpenSpec change before starting each item, using the completed adapter's evidence to refine scope. The names below are reserved suggestions, not existing changes.

### 1. Basic continuous integration — `add-theme-ci`

Python quality tooling and basic PR checks are configured. Extend that baseline as each adapter lands.

- [ ] Run palette validation, meaningful tests and generated-output checks on pull requests. Done when valid changes pass and invalid inputs or stale artifacts fail CI.
- [ ] Build the implemented host packages as downloadable CI artifacts. Done when artifacts can be installed locally and contain their license notices; no marketplace credentials are needed.

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
