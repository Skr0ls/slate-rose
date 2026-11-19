# Planning and Backlog

The approved baseline is one repository, a shared Python generator, separate host packages and the MIT license. Palette values remain frozen in palette/colors.json.

## Current work

The [repository cleanup checklist](changes/clean-up-repository/tasks.md) records
the archive and documentation work. The first preview is published. Native
terminal acceptance and marketplace preparation remain in the backlog.

## Earlier work

[fix-rider-csharp-builtins](changes/archive/2026-11-19-fix-rider-csharp-builtins/tasks.md) tracks the focused alias mapping and native Rider review. The Islands shell and local package are integrated.

[validate-jetbrains-editor-scheme](changes/archive/2026-11-19-validate-jetbrains-editor-scheme/tasks.md) records bounded C# review on Rider and one Java import smoke check on IntelliJ. The [initial adapter](changes/archive/2026-11-19-add-jetbrains-editor-scheme/tasks.md) is integrated.

[add-vscode-terminal-colors](changes/add-vscode-terminal-colors/proposal.md) implements the owner-approved ANSI design. Workbench appearance is accepted; native terminal acceptance remains pending.

The [initial VS Code editor change](changes/add-vscode-editor-theme/tasks.md) still awaits its recorded owner acceptance. The [workbench spec](specs/vscode-workbench-states/spec.md) preserves the accepted UI requirements.

The [delivery plan](delivery-plan.md) records the initial VS Code rollout.

## Follow-up backlog

These are queued work items, not active or approved implementation specifications. Create a dedicated OpenSpec change before starting each item, using the completed adapter's evidence to refine scope. The names below are reserved suggestions, not existing changes.

### 1. Basic continuous integration — `add-theme-ci`

Python quality tooling, palette validation and validator tests run in basic PR checks. Extend that baseline as each adapter lands.

- [x] Run generated-output checks on pull requests when generation is implemented. Stale artifacts fail CI.
- [x] Build all three host packages as downloadable CI artifacts. See the [release bundle](../docs/releasing.md).

### 2. UI design — `define-workbench-states`

The [workbench change](changes/archive/2026-11-19-define-workbench-states/proposal.md) implements the accepted palette allocation; the [native review](../previews/vscode/workbench/README.md) records the tested workbench slice. Terminal ANSI is tracked in [add-vscode-terminal-colors](changes/add-vscode-terminal-colors/tasks.md). The broader checkboxes below retain remaining state coverage and terminal implementation acceptance.

- [ ] Review cursor, active line, search, tabs, panels, menus, completion, focus and disabled states. Done when provisional mappings and any requested new colors have owner approval.
- [ ] Define diagnostic, Git/diff and terminal roles separately from approved syntax colors. Done when representative states have reviewed previews and contrast observations, with no automatic palette changes.
- [ ] Apply reviewed states to VS Code while preserving native layouts and interactions. Done when editor and surrounding UI are reviewed together.

### 3. JetBrains — `add-jetbrains-theme`

The initial editor scheme is tracked in [add-jetbrains-editor-scheme](changes/archive/2026-11-19-add-jetbrains-editor-scheme/tasks.md); the broader acceptance below remains open.

The Islands UI plugin is integrated. The [focused C# review](../previews/jetbrains/csharp-builtins/README.md) records alias styling; Java, Kotlin and Swift reviews follow in the [language backlog](language-validation-backlog.md). Start each implementation from updated `dev` after its predecessor integrates.

- [ ] Generate an editor color scheme and minimal UI theme resources from approved mappings. Done when they load in Rider and IntelliJ IDEA and language-specific differences are documented.
- [ ] Package a standalone theme plugin with MIT notice and installation instructions. Done when a local build installs successfully and fixtures are reviewed in the relevant IDEs.
- [x] Validate generated JetBrains output and package the plugin in CI.

### 4. Zed — `add-zed-theme`

The [Zed theme spec](specs/zed-theme/spec.md) covers the initial package and
its CI artifact. The [package guide](../packages/zed/README.md) records the
installation smoke test. Keep broader UI review and focused language
follow-ups in the backlog.

- [x] Generate native theme JSON and provide an extension manifest. The official schema check and local install passed.
- [ ] Review syntax, completion, search, tabs and panels while preserving Zed's native UI character. Done when screenshots and the host coverage table record observed results and limitations.
- [x] Check generated Zed output for drift in the Quality workflow.
- [x] Validate the official schema in CI and upload the installable `slate-rose-zed` development extension artifact.

### Language validation

- [ ] Work through the [language validation backlog](language-validation-backlog.md) in small, separately scoped changes. Done when each selected batch has the recorded review evidence and limitations described there.

### 5. Release preparation — `prepare-theme-releases`

- [x] Assemble the three validated assets in one CI bundle and document draft releases. See [prepare-release-assets](changes/archive/2026-11-19-prepare-release-assets/tasks.md) and the [release guide](../docs/releasing.md).
- [x] Verify a manual draft-release dispatch on `main` for an approved tag. The [workflow verification](changes/automate-draft-release/tasks.md#verification) records the draft and the published preview.
- [ ] Choose package IDs, publisher identity, supported editor versions and release version policy. Done when manifests, compatibility notes and changelogs agree.
- [ ] Add installation guides, screenshots and a semantic-coverage comparison for every supported host. Done when a reviewer can install the artifacts from the documentation.
- [x] Publish a verified GitHub Release VSIX to the VS Code Marketplace using Trusted Publishing. See the [publication evidence](changes/publish-vscode-marketplace/tasks.md#verification).
- [ ] Configure a separately triggered JetBrains publication job when the vendor account is ready. The job should publish the reviewed package from the release.
- [ ] Prepare Zed registry submission using the monorepository package path. Done when the registry accepts the extension and its published version is installable.

### Repository cleanup

Use the [cleanup checklist](changes/clean-up-repository/tasks.md) for progress.

- Archive changes by editor or capability after verifying checklist
  completion, integration, and acceptance for that change's scope. Sync
  requirements into main specs first, repair incoming and outgoing links,
  and keep outstanding acceptance in the active backlog. Each batch passes
  strict OpenSpec validation.
- Keep installation and build instructions in the package guides and
  index existing review evidence by editor. Done when those pages are
  reachable from the root README and package CI passes. Keep extension
  paths stable for CI and marketplace submissions.

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
