# Proposal

## Why

The owner accepted the VS Code workbench appearance and approved a separate sixteen-color ANSI proposal. The integrated terminal currently inherits host ANSI defaults, which do not form a complete Slate Rose terminal palette.

## What Changes

- Store the approved ANSI values in a separate validated terminal palette; preserve the existing 24-token syntax/UI palette byte-for-byte.
- Generate the sixteen native ANSI keys plus terminal background, text, cursor, selection and search colors using supported VS Code keys.
- Validate both source palettes before generation, preserve deterministic output and existing CLI behavior, and prevent outputs from overwriting either input.
- Review controlled ANSI foreground/background, normal/bright, bold, selection and search output in a real local terminal view; record host contrast adjustment rather than overriding user settings.
- Preserve the accepted workbench and syntax; update documentation and record owner approval accurately.

## Capabilities

### New Capabilities

- `vscode-terminal-colors`: Validated ANSI source values and reproducible VS Code integrated terminal colors and review evidence.

### Modified Capabilities

None. The existing syntax/UI palette contract remains unchanged.

## Impact

Shared palette loading, CLI validation/build/check, VS Code mappings, generated theme, focused tests, documentation and terminal review evidence. No third-party dependencies, shell/profile modifications, terminal behavior overrides, additional editors or publishing. Branch feature/vscode-terminal-colors is temporarily stacked on accepted workbench commit b4bd009; retarget/rebase to dev after that branch lands.
