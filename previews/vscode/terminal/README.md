# VS Code terminal review

Native review on 2026-11-17 in VS Code 1.146.0 arm64 on macOS, commit `69047191fc427f2f92828279aae1d90d8eeda7ab`. The owner approved the [ANSI design preview](approved-design.png); terminal implementation acceptance remains pending. The host-independent [terminal source](../../../palette/terminal.json) can be reused by future adapters; this review establishes no terminal coverage for Zed, JetBrains or external terminal applications.

## Native states

| State | Evidence and observation |
| --- | --- |
| Sixteen ANSI foregrounds and backgrounds | [Overview](ansi-overview.png): eight normal and eight bright foreground samples, plus normal/bright background columns. Bright shades are lighter, while hue families remain consistent. |
| Bold, reverse and default text | [Overview](ansi-overview.png): the bold row sends normal ANSI inputs with SGR 1; the effective bright-color preference is true. Reverse default text has a light background and dark foreground; reset restores the default text/background. |
| Cursor | [Overview](ansi-overview.png): the actual host block cursor follows `Cursor ready>` in accent. Cursor style is block and blinking is false; the theme does not set these preferences. |
| Active selection | [Selection](selection-active.png): the selected sentence remains readable over the configured selection background. |
| Inactive selection | [Inactive selection](selection-inactive.png): the same selection is quieter after focus leaves the window; native window controls also show the inactive state. |
| Search and input focus | [Search](search.png): `rose` has four matches, with the current result shown as 2 of 4. Current and secondary results remain readable, and the Find input has a visible focus outline. |

The normal black foreground visibly becomes gray on the dark viewport, while its background swatch remains dark. This is consistent with the host's minimum contrast adjustment at 4.5; configured `terminal.ansiBlack` remains the approved `#2B323E`. These screenshots do not establish an exact pixel RGB for every glyph. The [native color export](native-colors.json) separately verifies configured values.

## Context and identity

Screenshots use the isolated named profile **Slate Rose Terminal Review**, in a no-folder Extension Development Host. Slate Rose was selected explicitly in that profile. The Terminal panel was maximized and the Activity Bar hidden for clear captures; these are review-profile presentation choices, not contributed settings. The ordinary workspace window remained open. Output comes from the retained [review helper](review-helper/extension.js) using the public Pseudoterminal API. It writes display-only ANSI bytes and starts no shell process.

The effective settings were minimumContrastRatio **4.5**, drawBoldTextInBrightColors **true**, cursorStyle **block**, cursorBlinking **false**, Modern UI **true**, and empty workbench color customizations. No shell profile, terminal contrast preference, bold preference or cursor preference was changed.

A separate isolated installation at `/tmp/sr-term-data` with extensions at `/tmp/sr-term-ext` supplied an automated native export through the public `workbench.action.generateColorTheme` command. Both this installation and the named profile's installed theme match generated and packaged theme bytes. [verification.json](verification.json) records the two contexts explicitly; a shared extension global-storage path is not used as proof of profile isolation.

- Core palette SHA-256: `9086de1f1a752b95db890fe531753e9ab7bfea05b0f0b6cf23de35f541a0581d`.
- Terminal palette SHA-256: `927c9765dc282e646f64ae7f5e0292c8be5ae75c9b1060653dc0ed2582e95c16`.
- Generated, packaged and installed theme SHA-256: `2a531cc63b31cb7c467569ec7cd86fd3e0034c7b8b2e8403d9061fec362ac63d`.
- Final VSIX SHA-256: `7c5d1264f7d1673368bd3758c7b60ff1aad0d9dd64af13d71b375abb7bdb18d2`.

Two final packages built with VSCE 4.1.1, `SOURCE_DATE_EPOCH=1794787200` and `TZ=UTC` were byte-identical. After capture, only the packaged README gained the review link; the final package was reinstalled and retains the same theme bytes. All **159** configured colors match native export case-insensitively; the retained excerpt lists the **26** terminal additions. Removing those additions reproduces the complete generated theme at workbench base `b4bd009`, and the original palette bytes are unchanged. The sixteen ANSI source values match the approved preview exactly.

The [mapping document](../../../docs/vscode-terminal.md) lists the keys and limitations. All 26 terminal keys were independently verified in the official VS Code 1.143.0 terminal color registry. This is source compatibility evidence, not native rendering review of older hosts.

## Reproduction

Build the [local VSIX](../../../README.md#local-vs-code-installation). Copy the helper's [manifest](review-helper/package.json) and `extension.js` into `/tmp/sr-term-probe`; adjust its read-only `terminal.json` path when the checkout is elsewhere. Create the named profile before installing into it:

```sh
code --profile "Slate Rose Terminal Review" --new-window
code --profile "Slate Rose Terminal Review" --install-extension dist/slate-rose.vsix --force
code --profile "Slate Rose Terminal Review" --extensionDevelopmentPath /tmp/sr-term-probe --new-window
```

Select Slate Rose in the review profile. Run **Slate Rose Terminal Review: Show ANSI**, maximize the panel and inspect the output. Drag across the selection sentence; move focus to another app to inspect the inactive selection. With terminal focus, use Find to search for `rose`. The helper writes effective settings to `/tmp/sr-term-state.json`. **Export Theme** writes `/tmp/sr-term-native-theme.jsonc`; creating `/tmp/sr-term-export-once` before launching an isolated host runs this export once automatically. The helper is review tooling and is absent from the declarative VSIX.

## Remaining coverage

This review uses controlled ANSI output rather than a shell, build tool or TUI application. Alternate shells, custom terminal fonts, non-default contrast or bold settings, 256-color/true-color application output, split terminal borders, Windows/Linux and other hosts remain unreviewed. The theme does not recolor applications that supply their own true-color RGB values. No claim is made that all ANSI foreground/background combinations have sufficient contrast. Owner implementation acceptance remains pending.
