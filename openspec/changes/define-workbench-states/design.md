# Design

## Context

See proposal.md for motivation. The existing Python standard-library generator has ten editor colors and separate lexical and semantic maps. The owner approved the UI allocation in conversation on 2026-11-16. Implementation starts from origin/dev at 8399f2c, independently of PHP/Ruby PR 8.

## Goals / Non-Goals

**Goals:** Extend the existing explicit mapping approach; document every emitted UI key and derived opacity; validate emitted behavior and inspect installed native UI.

**Non-Goals:** Terminal ANSI, bracket rainbow redesign, OS title bars, custom CSS, layout changes, provider changes, palette changes, other host adapters or publication. Custom title-bar color keys can be omitted because this slice leaves window chrome to the host. No editor configuration is contributed by the package.

## Decisions

1. Use bg for editor and active tabs; surface for inactive tabs, Activity Bar, sidebars, panel and status bar; surface2 for raised widgets and hover. Use fg for text, muted for secondary/disabled text, selection for selections, accent for focus and active tab/panel indicators. Separators use surface2. This preserves restrained geometry while replacing unrelated defaults.
2. Keep opaque colors as token references. Add a separate explicit map of (token, alpha-byte) for overlays, rendered by appending alpha to validated six-digit palette hex. Avoid a general expression language. Existing syntax maps remain byte-for-byte unchanged. Tests must allow only palette RGB plus specifically documented alpha, never arbitrary new RGB values.
3. Search: accent at 0x33 current-match background, 0x1A other matches and word occurrences, accent border for current. Selection is selection; inactive selection uses selection at 0x80. Scrollbar uses muted at 0x33/0x55/0x77 normal/hover/active. Diff text uses string/error at 0x33; diff lines use string/error at 0x1A. These are palette-derived overlays, not new palette variants. Empty decoration borders are not forced; do not set both diff-text border and background.
4. Diagnostics use error/warning/accent/muted for error/warning/info/hint. Git add/modified/delete use string/func/error. No opaque diagnostic background. For buttons and badges on accent use bg text; input validation can use severity borders with neutral surface2 backgrounds. Keep focus visible in active and inactive list contexts.
5. Consult the current official [color reference](https://code.visualstudio.com/api/references/theme-color) and [theme guide](https://code.visualstudio.com/api/extension-guides/color-theme). Check every emitted key against documentation, and document version limitations rather than inventing unsupported keys. Version compatibility review includes the existing minimum host if supported keys are newer.
6. Root orchestrates an explicit Terra medium executor contract and independent Sol high read-only review. Root captures UI evidence in an isolated test profile. Reviewer checks the final generated artifact, documents and screenshots against this scope.

## Risks / Trade-offs

- Low surface contrast → preserve focus outlines and active indicators; record contrast observations without modifying palette values automatically.
- Inherited host components remain visible → enumerate configured families and leave specialized views as unreviewed, not universally supported.
- Inactive-window states and OS chrome vary → do not force title-bar settings; report actual reviewed platform.
- Overlay compositing changes visible colors → document alpha and inspect text over search/diff fills in the installed host.

## Migration Plan

Build and install a local VSIX in an isolated profile, verify exact generated/packaged/installed theme identity, review representative states and retain screenshots. Existing users reinstall the VSIX and select Slate Rose. Reverting the commit restores prior editor-only mapping. Owner acceptance and archive follow PR review and merge.
