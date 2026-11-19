# Planning and Backlog

The approved baseline is one repository, a shared Python generator, separate host packages and the MIT license. Palette values remain frozen in palette/colors.json.

## Current work

Next is [the first JetBrains Marketplace submission](#6-jetbrains-marketplace).
Slate Rose is available in [GitHub Releases](https://github.com/Skr0ls/slate-rose/releases)
and in the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=skr0ls.slate-rose),
where `0.3.1` shipped through
[Trusted Publishing](changes/publish-vscode-marketplace/tasks.md#verification).
The [repository cleanup checklist](changes/clean-up-repository/tasks.md) records
the completed archive and documentation work.

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

The [editor scheme](changes/archive/2026-11-19-add-jetbrains-editor-scheme/tasks.md)
was imported in Rider and IntelliJ IDEA. The separate
[Islands shell review](../previews/jetbrains/islands/README.md) records the
bundled UI theme in Rider. The [language backlog](language-validation-backlog.md)
tracks focused syntax reviews and remaining gaps.

- [x] Generate an editor scheme and Islands UI resources from the approved mappings.
- [x] Package the standalone MIT plugin, document installation, and verify local plugin installation in Rider.
- [x] Validate generated JetBrains output and package the plugin in CI.
- [ ] Verify the full plugin on the IDE builds claimed for Marketplace. Reuse the Rider evidence and check the packaged theme on IntelliJ IDEA where it will be listed as compatible.

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
- [x] Document the [release version policy](../docs/releasing.md#release-versioning) and per-editor package versions.
- [x] Document installation from released artifacts for all three editors. See the [installation index](../README.md#installation).
- [x] Publish a verified GitHub Release VSIX to the VS Code Marketplace using Trusted Publishing. See the [publication evidence](changes/publish-vscode-marketplace/tasks.md#verification).
- [ ] Keep the semantic coverage and supported IDE builds aligned with the manifests and the [review evidence](../previews/README.md).

### 6. JetBrains Marketplace

Use `prepare-jetbrains-marketplace` for the first submission. Start from
the [published plugin package](https://github.com/Skr0ls/slate-rose/releases/tag/v0.1.0-preview.2)
and the [JetBrains approval criteria](https://plugins.jetbrains.com/docs/marketplace/jetbrains-marketplace-approval-guidelines.html).

- [ ] Confirm the maintainer can select the intended [Vendor profile](https://plugins.jetbrains.com/docs/marketplace/organizations.html) and that its contact and website are current.
- [ ] Prepare the listing for `com.github.skr0ls.slaterose`. Include the English description, change notes, MIT license and source links, a 40 × 40 SVG logo, and representative theme screenshots.
- [ ] Verify the submission package format and compatibility with Plugin Verifier for the intended IDE builds. Use the published package if it meets the criteria. Use a new Quality build if packaging changes are required.
- [ ] Hand off the verified package and listing to the maintainer for the [first upload](https://plugins.jetbrains.com/docs/marketplace/uploading-a-new-plugin.html). Close this item once the listing is approved and installation from Marketplace is verified.
- [ ] After the first listing is live, add a separately triggered workflow for verified JetBrains updates.

### 7. Zed extension registry

- [ ] After the first JetBrains submission, prepare the Zed registry entry using the monorepository path `packages/zed`. Close this item once the registry accepts the extension and its published version is installable.

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
