# Design

## Context

The CLI currently builds/checks VS Code through one adapter and validates two immutable palette sources. See proposal.md for this slice's scope.

## Goals / Non-Goals

Keep the existing CLI and Python standard-library approach. Do not introduce an adapter framework or copy bundled theme assets.

## Decisions

- Add `generators/jetbrains` with an explicit key-to-token map and ElementTree XML serialization. Stable insertion order, LF and a final newline make output reproducible and escape palette metadata safely. A template/string replacement would need manual XML escaping.
- Emit `packages/jetbrains/colors/Slate Rose.icls`, scheme version `142`, parent `Darcula`, following the [official format example](https://blog.jetbrains.com/platform/2017/12/export-intellij-editor-themes-as-plugins/). Define TEXT foreground/background and shared [DefaultLanguageHighlighterColors](https://github.com/JetBrains/intellij-community/blob/master/platform/core-api/src/com/intellij/openapi/editor/DefaultLanguageHighlighterColors.java): CLASS_NAME, CLASS_REFERENCE, INTERFACE_NAME -> type/interface; FUNCTION_DECLARATION, FUNCTION_CALL, INSTANCE_METHOD, STATIC_METHOD -> func; INSTANCE_FIELD, STATIC_FIELD -> property; IDENTIFIER, LOCAL_VARIABLE -> variable; PARAMETER -> parameter; KEYWORD -> keyword; STRING -> string; NUMBER -> number; CONSTANT -> constant; METADATA -> attribute; LINE_COMMENT, BLOCK_COMMENT, DOC_COMMENT -> muted; OPERATION_SIGN -> operator. Each name has the `DEFAULT_` prefix.
- Use [EditorColors](https://github.com/JetBrains/intellij-community/blob/master/platform/editor-ui-api/src/com/intellij/openapi/editor/colors/EditorColors.java) keys CARET_COLOR -> accent, CARET_ROW_COLOR -> surface, LINE_NUMBERS_COLOR -> muted, GUTTER_BACKGROUND and EDITOR_GUTTER_BACKGROUND -> bg, SELECTION_BACKGROUND -> selection. Other states inherit the host. Do not serialize font options or copy parent definitions.
- Select renderer/default output with a small explicit CLI branch, retaining validation and alias protections for both palettes. Keep `validate` and VS Code output unchanged. Add the JetBrains consistency command to the existing CI quality job.

## Risks / Trade-offs

- Language plugins can override Language Defaults -> describe the scheme as initial/unverified in native IDEs, with a dedicated Rider/IntelliJ review next.
- Generic defaults lack separate flow-control, primitive and namespace categories -> inherit the host classification; do not invent keys or claim coral control coverage.
- Darcula supplies unmapped styles/states -> document inheritance rather than claiming every rendered color comes from our palette.
- Native import and screenshots could enlarge this PR -> deliver generation/automated checks first; do not mark the broader JetBrains backlog complete.
