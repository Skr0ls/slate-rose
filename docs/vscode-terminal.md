# VS Code terminal colors

The owner approved the separate ANSI design; native terminal implementation acceptance remains pending. The sixteen values are stored unchanged in `palette/terminal.json`, independently of host-specific mappings so later Zed and JetBrains adapters can reuse the source. The existing syntax and UI palette remains separate. The [native terminal review](../previews/vscode/terminal/README.md) records observed states and limitations.

| ANSI key suffix | Normal | Bright |
| --- | --- | --- |
| Black | #2B323E | #8992A1 |
| Red | #E47691 | #F19DB0 |
| Green | #A9CE91 | #C1DFA9 |
| Yellow | #D8B981 | #E0C38C |
| Blue | #8CC6F1 | #ACD7F5 |
| Magenta | #CAA1DE | #DEB9EC |
| Cyan | #8FCBC5 | #A9E0D9 |
| White | #D1D4DC | #EFF1F5 |

Keys are `terminal.ansi` followed by the suffix, with `Bright` before the suffix for bright colors.

| VS Code key | Core token | Alpha |
| --- | --- | --- |
| `terminal.background` | `bg` | opaque |
| `terminal.foreground` | `fg` | opaque |
| `terminalCursor.foreground` | `accent` | opaque |
| `terminalCursor.background` | `bg` | opaque |
| `terminal.border` | `surface2` | opaque |
| `terminal.selectionBackground` | `selection` | opaque |
| `terminal.inactiveSelectionBackground` | `selection` | `80` |
| `terminal.findMatchBackground` | `accent` | `33` |
| `terminal.findMatchBorder` | `accent` | opaque |
| `terminal.findMatchHighlightBackground` | `accent` | `1A` |

All 26 keys are registered by the [VS Code 1.143.0 terminal color registry](https://github.com/microsoft/vscode/blob/1.143.0/src/vs/workbench/contrib/terminal/common/terminalColorRegistry.ts), the package's minimum host. The sixteen ANSI names are registered through its ANSI color map; the other ten keys are direct registrations. This does not establish native rendering coverage on every supported version.

The theme leaves selection foreground and terminal settings to the host. VS Code can adjust low-contrast text through `terminal.integrated.minimumContrastRatio`; normal black on the background is particularly low contrast. Bold text can use bright colors depending on `terminal.integrated.drawBoldTextInBrightColors`. Thus displayed pixels can differ from configured RGB values. The theme does not override these preferences or cursor style. See the official [terminal color reference](https://code.visualstudio.com/api/references/theme-color#integrated-terminal-colors), [appearance documentation](https://code.visualstudio.com/docs/terminal/appearance), and [Pseudoterminal API](https://code.visualstudio.com/api/references/vscode-api#Pseudoterminal).
