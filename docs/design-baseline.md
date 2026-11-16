# Slate Rose

Slate Rose is an original cross-editor dark color theme for VS Code, JetBrains IDEs, and Zed.

**Status:** design baseline v0.2 (Contrast). Implementation not started.

**License:** [MIT](../LICENSE). Source repository: [Skr0ls/slate-rose](https://github.com/Skr0ls/slate-rose).

**Planning:** [OpenSpec backlog and workflow](../openspec/README.md). The first implementation checklist is [add-vscode-editor-theme](../openspec/changes/add-vscode-editor-theme/tasks.md).

## 1. Vision and non-negotiables

- Cool, dark graphite surfaces; muted yet legible syntax colors.
- Sand-yellow types, sky-blue functions, rose-colored fields, lilac declarations, green strings.
- Ordinary variables and punctuation should remain visually quiet.
- Preserve **the exact approved v0.2 colors** in [`palette/colors.json`](../palette/colors.json). This is the single source of truth; do not silently adjust values or introduce alternate palettes.
- Editor consistency matters more than forcing identical results where host APIs differ. Document differences honestly.
- No external artwork, fonts or source-code assets are required.

## 2. Approved color tokens

The approved palette and token values are maintained in [`palette/colors.json`](../palette/colors.json). Values are frozen until explicitly approved by the project owner.

## 3. Syntax rules

**C++ reference examples:** `float`, `char`, `unsigned int` → `primitive`; `font`, `context`, `character`, `glm::vec2` (type portion) → `type`; `get_context`, `get_char`, `push_instanced_rect_data` → `func`; `bearing`, `atlas_id`, `px_face_size`, `texture_id` → `property`; `class`, `struct`, `public`, `private`, `if` → `keyword`; `return` → `control`; quoted paths → `string`. Namespace/module portions can use `namespace`.

**C# reference examples:** `class`, `public`, `private`, `if` → `keyword`; `return`, `throw`, `await` → `control`; `UserService`, `Task`, `Guid` → `type` or `primitive` according to their actual semantic category; `IUserRepository` → `interface`; `GetUserAsync` → `func`; `_repository` → `property` (field); ordinary locals and parameters → `variable` and `parameter`.

**TypeScript/Python:** apply semantic roles, not hard-coded keyword-by-keyword substitutions. Decorators/attributes → `attribute` where available. Support fallback scopes where semantic tokens are missing.

**Precedence:** use host semantic classification where reliable, then lexical/TextMate/Tree-sitter fallback. Avoid blanket rules that recolor all identifiers or erase distinctions. Some editors cannot distinguish all categories; record such limitations.

## 4. Workbench and editor states still to design

The approved palette is complete **for its current 24 tokens**, but a production theme needs additional semantic design tokens. Do not invent final hex values without review. Candidate tokens:

- Editor: active/inactive line, caret, line numbers, gutter, indentation guides, bracket matching, search matches, word highlights, inlay hints, CodeLens, whitespace, links.
- UI: active/inactive tabs, sidebars, tree selections, toolbar, popups, menus, completion, hover, breadcrumbs, status bar, separators, focus, disabled text, scrollbars.
- Diagnostics: info, hint, deprecated, underlines, diagnostic backgrounds.
- Git/diff: added, modified, removed, conflicts, diff backgrounds.
- Terminal: ANSI normal/bright 16-color palette, terminal foreground/background/cursor/selection.

Derive *provisional* mappings from existing colors when possible and clearly mark them as provisional. Do not mutate `palette/colors.json` as a shortcut.

## 5. Target editors

1. **JetBrains** (Rider/IntelliJ and related): editor color scheme `.icls`; optional full UI theme plugin (`.theme.json` and plugin packaging). Some semantic categories are IDE/language dependent.
2. **VS Code**: color theme JSON with `colors`, `tokenColors`, and `semanticTokenColors`; package as an extension later.
3. **Zed**: native theme JSON according to the current supported schema; validate using Zed, not a guessed schema.
4. **Visual Studio** (Windows): separate adapter, investigate available theme/export/extension paths and limitations before implementing; do not confuse it with VS Code.
5. **Neovim** (optional later): Lua highlight groups, Tree-sitter and LSP semantic groups.

A host-specific adapter is allowed to map multiple semantic roles to the same host scope. Maintain an explicit coverage/limitations table.

## 6. Repository architecture

Approved on 2026-11-16: one source repository, a shared Python generator and separate host packages. Create adapter and package directories as their implementations land.

```text
slate-rose/
├── AGENTS.md
├── README.md
├── LICENSE                    # MIT
├── palette/
│   └── colors.json             # approved source of truth
├── generators/                # to be implemented
│   ├── jetbrains/
│   ├── vscode/
│   ├── zed/
│   └── visual-studio/
├── packages/                  # host manifests and generated theme resources
│   ├── vscode/
│   ├── jetbrains/
│   └── zed/
├── openspec/                  # specifications, change tasks and backlog
├── fixtures/                  # syntax samples for C++, C#, TS, Python
└── previews/                  # screenshots and comparison images
```

A small Python generator using the standard library will load and validate the palette, map semantic roles to host-specific keys, and emit reproducible artifacts into host packages. Separate **source tokens**, **semantic mappings**, and **generated theme output**. Prefer deterministic builds and simple validation tests. Generated theme resources are not hand-maintained. Host packaging tools remain separate from the shared generator.
