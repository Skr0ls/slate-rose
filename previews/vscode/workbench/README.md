# VS Code workbench review

Local native review on 2026-11-17, VS Code 1.146.0 arm64 on macOS, commit `69047191fc427f2f92828279aae1d90d8eeda7ab`. This review covers the installed workbench slice, not owner acceptance or universal host/provider support. [Mappings](../../../docs/vscode-mappings.md) list all 120 configured colors and alpha bytes.

## Package identity

[verification.json](verification.json) records exact identities and fixture hashes:

- Palette SHA-256: `9086de1f1a752b95db890fe531753e9ab7bfea05b0f0b6cf23de35f541a0581d`.
- Generated, packaged and installed theme SHA-256: `83066664dd580ad6ca14e9f03989d8404a2b9c1731f97e2065dfb3c964af2310`; bytes matched.
- VSIX SHA-256: `8daffc8033450cd4298f375fc516a5f85fa392ccb0d7913d01cb5dfcff8404e4`; two packages built with VSCE 4.1.1, `SOURCE_DATE_EPOCH=1794787200` and `TZ=UTC` matched byte-for-byte. After capture, the package README was updated with this review link; repackaging and reinstalling preserved identical theme bytes.
- Palette bytes and complete lexical/semantic payloads match the implementation base `8399f2cfd33328173906ee2a00145b15762d86bf`. PHP/Ruby PR 8 is independent of this branch.

The isolated profile was `/tmp/sr-ui-data`, extensions `/tmp/sr-ui-ext`, with Slate Rose selected and no `workbench.colorCustomizations`. Final screenshots show a no-folder Extension Development Host opening only local review files. The public API reported `isTrusted: true` for this empty workspace; no folder trust was granted or security protection disabled. The host's existing/default `window.titleBarStyle` was `custom`; the theme neither set it nor configured title-bar colors. Gray outer chrome, native traffic-light controls and host spacing remain visible.

## Observed states

| State | Evidence and result |
| --- | --- |
| Sidebar, Activity Bar, tabs, panel, status bar | [Overview](overview.png): surrounding surfaces, editor background and active/inactive tabs remain distinguishable; the active tab retains a darker background. This host's rounded tab/panel layout does not visibly present every configured indicator as a separate strip. |
| Active editor selection | [Active selection](selection-active.png): selected `value` on line 11 remains readable. |
| Inactive editor selection and input focus | [Inactive selection](selection-inactive.png): the same selection dims when the Problems filter receives focus; its accent input outline is visible. |
| Active and inactive list selection | [Active list](list-active.png), [inactive list](list-inactive.png): the warning row retains selection while keyboard focus moves to the editor; native outline treatment changes, with a dotted accent outline in the inactive capture. The identical list fills do not erase the host's focus distinction. |
| Search matches and focused input | [Search](search-focus.png): `label` shows current result 12 of 136, an accent border on the current match, quieter secondary highlights, and an outlined Find input. Text remains visible over both fills. |
| Error, warning, information and hint | [Overview](overview.png): synthetic error/warning/information squiggles and a subdued hint decoration are visible at lines 5–8. Problems lists three entries; the hint is not represented as a fourth problem row. These are controlled UI diagnostics, not language-provider validation. |
| Hover | [Hover](hover.png): synthetic Markdown content in the native hover widget remains readable against the raised surface. |
| Completion | [Completion](completion.png): native word suggestions, highlighted matching prefix and selected suggestion remain readable. This does not establish semantic completion-provider support. |
| Scrollbar hover | [Scrollbar](scrollbar-hover.png): the pointer is on the editor scrollbar thumb, which is more visible than its normal state in the overview. Drag/pressed appearance is configured but not separately captured. |
| Diff | [Diff](diff.png): native side-by-side comparison of the retained before/after fixtures shows red/rose removals and green additions, including stronger changed-text fills over quieter line fills. Both sides remain readable. |

Foreground contrast calculated from the unmodified palette is 11.39:1 on editor bg, 9.73:1 on surface, 8.70:1 on surface2 and 6.70:1 on selection. Muted text is 4.60:1 on surface and 4.11:1 on surface2; the latter is below 4.5:1 for normal-sized text. Surface/bg and surface2/surface are deliberately subtle at 1.17:1 and 1.12:1. Focus is carried by accent outlines and native state treatments rather than surface contrast alone. These calculations are observations, not a full accessibility certification; palette values were not automatically adjusted.

## Reproduction

Build and install the [local VSIX](../../../README.md#local-vs-code-installation). The retained [fixtures](fixtures/workbench.ts) are display-only and must not be executed. [Before](fixtures/before.ts), [after](fixtures/after.ts) and [reference](fixtures/reference.ts) supply the other tabs. The [review helper](review-helper/extension.js) registers controlled diagnostics, one synthetic hover, and commands that open native UI; it is review tooling and is not shipped in the VSIX.

To reproduce the exact paths, copy the four fixtures into `/tmp/sr-web-context/javascript/ui-review`, and copy the helper's [manifest](review-helper/package.json) and `extension.js` into `/tmp/sr-ui-probe`. Install the VSIX into an isolated extensions directory and open an empty development window:

```sh
code --user-data-dir /tmp/sr-ui-data --extensions-dir /tmp/sr-ui-ext --install-extension dist/slate-rose.vsix --force
code --user-data-dir /tmp/sr-ui-data --extensions-dir /tmp/sr-ui-ext --extensionDevelopmentPath /tmp/sr-ui-probe --new-window
```

Select Slate Rose if the profile is new. Run `Slate Rose Review: Overview`, `Hover`, `Completion` or `Diff` from the Command Palette. Search for `label`; compare editor selection while moving focus to the Problems filter, then compare the selected warning row while moving focus back to the editor. Hover the scrollbar with the long fixture open. No repository clone, language server, fixture execution, sign-in or folder trust is required. The helper writes a small identity report to `/tmp/sr-ui-probe-state.json`.

## Remaining coverage

Windows/Linux, older host rendering, inactive application windows, repository Git file decorations and gutters, debugger status, notifications, validation error popups, disabled controls and custom-rendered menus remain unreviewed natively. Their configured colors are checked in generated output only. Native macOS menus and window chrome retain host behavior. This is a representative state review, not inspection of every one of the 120 keys. Terminal ANSI colors, bracket rainbow redesign, specialized extension views and other editor adapters are separate work. Owner acceptance remains pending.
