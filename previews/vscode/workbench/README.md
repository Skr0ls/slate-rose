# VS Code workbench review

Local native review on 2026-11-17, VS Code 1.146.0 arm64 on macOS, commit `69047191fc427f2f92828279aae1d90d8eeda7ab`. This review covers representative states in the installed workbench slice. [Mappings](../../../docs/vscode-mappings.md) list all 133 configured colors and alpha bytes. The initial ten screenshots below retain the first workbench build; three framing screenshots document the subsequent owner-requested correction. Existing UI colors and syntax were unchanged by that correction.

## Initial review package identity

[verification.json](verification.json) records exact identities and fixture hashes:

- Palette SHA-256: `9086de1f1a752b95db890fe531753e9ab7bfea05b0f0b6cf23de35f541a0581d`.
- Generated, packaged and installed theme SHA-256: `83066664dd580ad6ca14e9f03989d8404a2b9c1731f97e2065dfb3c964af2310`; bytes matched.
- VSIX SHA-256: `8daffc8033450cd4298f375fc516a5f85fa392ccb0d7913d01cb5dfcff8404e4`; two packages built with VSCE 4.1.1, `SOURCE_DATE_EPOCH=1794787200` and `TZ=UTC` matched byte-for-byte. After capture, the package README was updated with this review link; repackaging and reinstalling preserved identical theme bytes.
- Palette bytes and complete lexical/semantic payloads match the implementation base `8399f2cfd33328173906ee2a00145b15762d86bf`. PHP/Ruby PR 8 is independent of this branch.

The isolated profile was `/tmp/sr-ui-data`, extensions `/tmp/sr-ui-ext`, with Slate Rose selected and no `workbench.colorCustomizations`. Screenshots show a no-folder Extension Development Host opening only local review files. The public API reported `isTrusted: true` for this empty workspace; no folder trust was granted or security protection disabled. The host's existing/default `window.titleBarStyle` was `custom`. The initial theme did not configure title-bar or Modern UI shell colors, leaving gray gutters and frame lines. Owner feedback identified that omission; the framing correction below replaces those colors while preserving native controls and spacing.

## Modern UI framing correction

The gray strips were themeable Modern UI shell surfaces. The [official 1.146.0 Modern UI documentation](https://github.com/microsoft/vscode/blob/1.146.0/src/vs/workbench/contrib/modernUI/README.md#colors) documents separate active/inactive shell colors and shared or region-specific frame borders. All 13 added keys are also registered in 1.143.0; layout availability remains build/configuration dependent.

| State | Corrected native evidence |
| --- | --- |
| Active window | [Active framing](framing-active.png): the title bar and shell gutters around the editor, Activity Bar and secondary sidebar use bg; frame contours use surface2. Native gaps, rounded corners and traffic-light controls remain. [API state](framing-active-state.json) confirms Modern UI enabled and window focused. |
| Inactive window | [Inactive framing](framing-inactive.png): the same shell stays dark after focus moves to Finder, with native inactive controls/text treatment. [API state](framing-inactive-state.json) confirms window focus false. |
| Sidebar and panel overview | [Corrected overview](framing-overview.png): the primary sidebar, editor and Problems panel retain the existing colors with subdued frame borders and bg gutters. |

[framing-native-colors.json](framing-native-colors.json) records the 13 added values from VS Code's native **Developer: Generate Color Theme From Current Settings** export, matching generated output case-insensitively. [framing-verification.json](framing-verification.json) records the final corrected package/theme identity, reproducible builds and the comparison against first workbench commit `a8f9cda`: palette, complete syntax payloads and every pre-existing UI value remain unchanged. Theme RGB values remain those in the approved palette; only native shell/frame colors were added. No layout, title-bar style, Modern UI or security setting was changed by the product.

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

Build and install the [local VSIX](../../../packages/vscode/README.md#build-from-source). The retained [fixtures](fixtures/workbench.ts) are display-only and must not be executed. [Before](fixtures/before.ts), [after](fixtures/after.ts) and [reference](fixtures/reference.ts) supply the other tabs. The [review helper](review-helper/extension.js) registers controlled diagnostics, one synthetic hover, and commands that open native UI; it is review tooling and is not shipped in the VSIX.

To reproduce the exact paths, copy the four fixtures into `/tmp/sr-web-context/javascript/ui-review`, and copy the helper's [manifest](review-helper/package.json) and `extension.js` into `/tmp/sr-ui-probe`. Install the VSIX into an isolated extensions directory and open an empty development window:

```sh
code --user-data-dir /tmp/sr-ui-data --extensions-dir /tmp/sr-ui-ext --install-extension dist/slate-rose.vsix --force
code --user-data-dir /tmp/sr-ui-data --extensions-dir /tmp/sr-ui-ext --extensionDevelopmentPath /tmp/sr-ui-probe --new-window
```

Select Slate Rose if the profile is new. Run `Slate Rose Review: Overview`, `Hover`, `Completion` or `Diff` from the Command Palette. Search for `label`; compare editor selection while moving focus to the Problems filter, then compare the selected warning row while moving focus back to the editor. Hover the scrollbar with the long fixture open. For framing, show the secondary sidebar and compare the window before and after focusing another app. The profile must already have Modern UI enabled; this review did not enable it or alter its geometry. The helper's added `Export Theme` command exports current native theme data to `/tmp/sr-ui-native-theme.jsonc`. No repository clone, language server, fixture execution, sign-in or folder trust is required. The helper writes an identity and window-focus report to `/tmp/sr-ui-probe-state.json`.

## Remaining coverage

Windows/Linux, older host rendering, repository Git file decorations and gutters, debugger status, notifications, validation error popups, disabled controls and custom-rendered menus remain unreviewed natively. Their configured colors are checked in generated output only. Native macOS controls and menus retain host behavior; custom title-bar and shell colors now follow the theme. This is a representative state review, not inspection of every one of the 133 keys. Terminal ANSI colors, bracket rainbow redesign, specialized extension views and other editor adapters are separate work. The owner accepted the workbench appearance. The coverage gaps above remain open.
