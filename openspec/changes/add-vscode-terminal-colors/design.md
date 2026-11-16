# Design

## Context

See proposal.md for motivation. The owner approved the separate ANSI preview in conversation: "ok, looks ggood". This approval applies to the exact table below; the existing syntax/UI palette and accepted Modern UI remain unchanged. Base: b4bd009 on feature/vscode-workbench. Development is temporarily stacked so the local VSIX retains that accepted UI while GitHub is unavailable.

## Goals / Non-Goals

**Goals:** Strict reusable source validation, simple explicit host maps, failure before writing, native evidence with no shell dependencies, small independently reviewable terminal commit.

**Non-Goals:** New palette variants, inferred colors, extra ANSI colors beyond the approved sixteen, user settings/profile changes, shell integrations, other editors, marketplace publication or automatic merge.

## Decisions

1. Add `palette/terminal.json` using the existing `{name, version, colors}` shape, name Slate Rose Terminal and version 0.1. Logical tokens are snake_case; host ANSI identifiers remain explicit in the VS Code adapter. Freeze these approved values:

| Token | Normal | Bright token | Bright |
| --- | --- | --- | --- |
| black | #2B323E | bright_black | #8992A1 |
| red | #E47691 | bright_red | #F19DB0 |
| green | #A9CE91 | bright_green | #C1DFA9 |
| yellow | #D8B981 | bright_yellow | #E0C38C |
| blue | #8CC6F1 | bright_blue | #ACD7F5 |
| magenta | #CAA1DE | bright_magenta | #DEB9EC |
| cyan | #8FCBC5 | bright_cyan | #A9E0D9 |
| white | #D1D4DC | bright_white | #EFF1F5 |

2. Reuse the existing immutable Palette representation and strict JSON/metadata/hex validation via a small internal helper accepting an expected token set; retain `load_palette(path)` for its exact 24-token contract and add `load_terminal_palette(path)` for sixteen tokens. Do not add a general schema framework or duplicate the loader. A pure render function receives both validated palettes explicitly; it does not read files itself.
3. Default `validate`, `build vscode` and `check vscode` validate both inputs. Preserve existing positional core-palette validation and `--palette`/`--output`; add `--terminal-palette PATH` to all three commands. Report each validated source. Load and validate inputs before making output directories or writing. Output collision guards cover selected/canonical paths for both files, including samefile aliases. Existing non-terminal CLI semantics remain intact.
4. Add exactly sixteen native ANSI mappings and ten terminal UI colors: terminal.background=bg, terminal.foreground=fg, terminalCursor.foreground=accent, terminalCursor.background=bg, terminal.border=surface2, terminal.selectionBackground=selection, terminal.inactiveSelectionBackground=selection80, terminal.findMatchBackground=accent33, terminal.findMatchBorder=accent and terminal.findMatchHighlightBackground=accent1A. Do not set terminal.selectionForeground; preserve ANSI text and host contrast behavior. Keep all prior mappings unchanged.
5. Consult current official [theme colors](https://code.visualstudio.com/api/references/theme-color#integrated-terminal-colors), [terminal appearance](https://code.visualstudio.com/docs/terminal/appearance) and public [Pseudoterminal API](https://code.visualstudio.com/api/references/vscode-api#Pseudoterminal). Verify the keys in the supported minimum host. Review controlled normal/bright foregrounds, backgrounds, bold and reversed/default text, selection, cursor and find using a local review-only Pseudoterminal. The helper writes ANSI display bytes; no shell fixture is executed and the helper is absent from the VSIX.
6. Record effective minimumContrastRatio, drawBoldTextInBrightColors, cursor style and theme customization settings. The host may adjust low-contrast text (notably normal black on bg); document this separately from source values. Native export must match configured values, not assume every rendered pixel equals the source RGB. Do not ship settings to disable contrast adjustment.
7. Root owns OpenSpec checkboxes, native capture and integration. Terra medium implements a bounded contract; Sol high reviews code and final evidence read-only. Update the status docs to record that the owner accepted the workbench appearance and ANSI design while terminal implementation acceptance remains pending.

## Risks / Trade-offs

- Normal black has low contrast on the dark viewport → preserve the approved value, show foreground/background use and record host contrast behavior; do not promise accessibility of every ANSI foreground/background pair.
- Additional input can be overwritten accidentally → extend same-file/symlink/hard-link guards to both canonical and selected paths; negative CLI tests verify byte preservation and failure before directory creation.
- Stacked branch creates temporary Git dependency → keep terminal edits in a separate commit and review against b4bd009; land/rebase the workbench before retargeting the terminal PR to dev.

## Migration Plan

Build and install the final VSIX in an isolated profile. Record repeated fixed-metadata package identity and exact generated/packaged/installed theme equality. Existing users reinstall the package and retain their terminal settings. Rollback is reverting the terminal commit. Archive only after owner review and integration.
