# VS Code mapping and limitations

The generated JSON uses the [VS Code theme schema](https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/workbench/services/themes/common/colorThemeSchema.ts), [editor color keys](https://code.visualstudio.com/api/references/theme-color), and [semantic highlighting](https://raw.githubusercontent.com/microsoft/vscode-docs/main/api/language-extensions/semantic-highlight-guide.md). Semantic tokens overlay TextMate grammar colors. Provider classifications vary, so the mappings do not promise parity between languages or providers. The [fixture review](../previews/vscode/README.md) records observed rendering and its limits. A local VSIX can be built and installed using the [instructions](../README.md#local-vs-code-installation).

Local verification on VS Code 1.143.1 arm64 confirmed VSIX installation and Slate Rose selection using the official VS Code API; a native theme export matched all 10 configured editor colors. The four standalone fixtures were subsequently reviewed with the providers and screenshots listed in the [visual review](../previews/vscode/README.md). Owner acceptance and broader provider behavior remain unverified.

| Role | Semantic token types | TextMate scopes |
| --- | --- | --- |
| Type | type, class, enum, struct, typeParameter; interface uses interface | entity.name.type, support.type |
| Function | function, method | entity.name.function, support.function |
| Property | property, event | specific variable and entity property scopes, including C# fields and Ruby instance variables |
| Variable / parameter | variable / parameter | variable.other.readwrite, entity.name.variable, variable.other.constant / variable.parameter, entity.name.variable.parameter |
| Namespace | namespace | entity.name.namespace, entity.name.type.namespace, entity.name.type.module |
| Constant | enumMember | variable.other.constant.cs, variable.other.enummember, entity.name.variable.enum-member, constant.other |
| Attribute | decorator | entity.name.function.decorator, entity.other.attribute-name, support.other.attribute |
| Comment / string / number | comment / string, regexp / number | comment / string / constant.numeric |
| Operator | operator | keyword.operator |
| Declaration | — | keyword, storage |
| Flow | `controlKeyword:csharp` | specific keyword.control flow scopes and C# await expression scope |
| Primitive | — | specific primitive scopes and C# keyword.type |
| Punctuation | — | punctuation |

The generic semantic `keyword` type has no override: generic keyword tokens cannot distinguish declarations from flow control. Providers can still override lexical distinctions. No declaration or readonly modifier override is applied: local variables stay quiet and readonly fields classified as properties stay rose. Default-library types such as Task and Guid are not treated as primitives. Named constants outside reliably distinguished grammar or provider categories may remain quiet. TypeScript const bindings remain quiet in lexical fallback; the specific `variable.other.constant.object.property` scope colors an intermediate property such as `obj.CONFIG.value`, while a root such as `CONFIG.value` stays quiet. Primitive recognition is limited to explicit lexical scopes; providers can obscure it. In the reviewed C# fixture, the semantic `keyword` overlay colors `string` lilac even though its `keyword.type.string.cs` TextMate scope would match the primitive rule; the [review](../previews/vscode/README.md) records the inspection. Broad `storage.type` remains a declaration, and broad `keyword.control` remains a keyword.

The lexical mappings were informed by the official [C++](https://raw.githubusercontent.com/microsoft/vscode/main/extensions/cpp/syntaxes/cpp.tmLanguage.json), [C#](https://raw.githubusercontent.com/microsoft/vscode/main/extensions/csharp/syntaxes/csharp.tmLanguage.json), [TypeScript](https://raw.githubusercontent.com/microsoft/vscode/main/extensions/typescript-basics/syntaxes/TypeScript.tmLanguage.json), and [Python](https://raw.githubusercontent.com/microsoft/vscode/main/extensions/python/syntaxes/MagicPython.tmLanguage.json) grammars. The exact selectors are in the generator.

The JavaScript, JSX, and TSX grammars group `try`, `catch`, `finally`, and `throw` under `keyword.control.trycatch`. Language-scoped lexical rules color that group as flow control in those modes; the group cannot distinguish `throw` from the other three keywords. The [web review](../previews/vscode/web/README.md) records the observed scopes and provider limitations.

Ruby instance variables use the language-scoped `source.ruby variable.other.readwrite.instance` property rule. Ordinary parameters and local variables retain the foreground role. The built-in Ruby grammar groups `return` with declarations and predicates, and groups `raise` with other special methods; those groups remain lilac. The PHP grammar groups primitive and pseudo-types, including PHPDoc `self` and `static`, under the same type scope, and its exception scope includes `exception` alongside control words. These mixed groups retain their existing mappings. The [PHP and Ruby review](../previews/vscode/php-ruby/README.md) records observed colors and provider limits.

The following provisional workbench and editor mappings use the approved palette. Every opaque key uses the token exactly; overlay keys append the indicated alpha byte. The [official color reference](https://code.visualstudio.com/api/references/theme-color) defines these keys and [theme guide](https://code.visualstudio.com/api/extension-guides/color-theme) describes workbench and syntax colors. All emitted keys are registered in the [VS Code 1.143.0 source](https://github.com/microsoft/vscode/tree/1.143.0/src) or its built-in Git extension, the minimum supported host; this source check is not a native rendering test. The [native workbench review](../previews/vscode/workbench/README.md) records representative states and limits; configured keys do not imply all host views have been inspected:

| VS Code key | Palette token | Alpha |
| --- | --- | --- |
| `modernUI.shellBackground` | `bg` | opaque |
| `modernUI.inactiveShellBackground` | `bg` | opaque |
| `titleBar.activeBackground` | `bg` | opaque |
| `titleBar.inactiveBackground` | `bg` | opaque |
| `titleBar.border` | `bg` | opaque |
| `titleBar.activeForeground` | `fg` | opaque |
| `titleBar.inactiveForeground` | `muted` | opaque |
| `surface.background` | `surface` | opaque |
| `surface.foreground` | `fg` | opaque |
| `surface.border` | `surface2` | opaque |
| `editor.border` | `surface2` | opaque |
| `modernPanel.border` | `surface2` | opaque |
| `modernActivityBar.border` | `surface2` | opaque |
| `activityBar.activeBorder` | `accent` | opaque |
| `activityBar.background` | `surface` | opaque |
| `activityBar.border` | `surface2` | opaque |
| `activityBar.foreground` | `fg` | opaque |
| `activityBar.inactiveForeground` | `muted` | opaque |
| `activityBarBadge.background` | `accent` | opaque |
| `activityBarBadge.foreground` | `bg` | opaque |
| `badge.background` | `accent` | opaque |
| `badge.foreground` | `bg` | opaque |
| `button.background` | `accent` | opaque |
| `button.foreground` | `bg` | opaque |
| `button.hoverBackground` | `func` | opaque |
| `descriptionForeground` | `muted` | opaque |
| `disabledForeground` | `muted` | opaque |
| `dropdown.background` | `surface2` | opaque |
| `dropdown.border` | `surface2` | opaque |
| `dropdown.foreground` | `fg` | opaque |
| `editor.background` | `bg` | opaque |
| `editor.findMatchBorder` | `accent` | opaque |
| `editor.foreground` | `fg` | opaque |
| `editor.lineHighlightBackground` | `surface` | opaque |
| `editor.selectionBackground` | `selection` | opaque |
| `editorCursor.foreground` | `accent` | opaque |
| `editorError.foreground` | `error` | opaque |
| `editorGroup.border` | `surface2` | opaque |
| `editorGroupHeader.tabsBackground` | `surface` | opaque |
| `editorGutter.addedBackground` | `string` | opaque |
| `editorGutter.deletedBackground` | `error` | opaque |
| `editorGutter.modifiedBackground` | `func` | opaque |
| `editorHint.foreground` | `muted` | opaque |
| `editorHoverWidget.background` | `surface2` | opaque |
| `editorHoverWidget.border` | `surface2` | opaque |
| `editorHoverWidget.foreground` | `fg` | opaque |
| `editorInfo.foreground` | `accent` | opaque |
| `editorLineNumber.activeForeground` | `fg` | opaque |
| `editorLineNumber.foreground` | `muted` | opaque |
| `editorSuggestWidget.background` | `surface2` | opaque |
| `editorSuggestWidget.border` | `surface2` | opaque |
| `editorSuggestWidget.foreground` | `fg` | opaque |
| `editorSuggestWidget.highlightForeground` | `accent` | opaque |
| `editorSuggestWidget.selectedBackground` | `selection` | opaque |
| `editorWarning.foreground` | `warning` | opaque |
| `editorWidget.background` | `surface2` | opaque |
| `editorWidget.border` | `surface2` | opaque |
| `editorWidget.foreground` | `fg` | opaque |
| `errorForeground` | `error` | opaque |
| `focusBorder` | `accent` | opaque |
| `foreground` | `fg` | opaque |
| `gitDecoration.addedResourceForeground` | `string` | opaque |
| `gitDecoration.deletedResourceForeground` | `error` | opaque |
| `gitDecoration.modifiedResourceForeground` | `func` | opaque |
| `icon.foreground` | `fg` | opaque |
| `input.background` | `surface2` | opaque |
| `input.border` | `surface2` | opaque |
| `input.foreground` | `fg` | opaque |
| `input.placeholderForeground` | `muted` | opaque |
| `inputOption.activeBorder` | `accent` | opaque |
| `inputValidation.errorBackground` | `surface2` | opaque |
| `inputValidation.errorBorder` | `error` | opaque |
| `inputValidation.infoBackground` | `surface2` | opaque |
| `inputValidation.infoBorder` | `accent` | opaque |
| `inputValidation.warningBackground` | `surface2` | opaque |
| `inputValidation.warningBorder` | `warning` | opaque |
| `list.activeSelectionBackground` | `selection` | opaque |
| `list.activeSelectionForeground` | `fg` | opaque |
| `list.focusOutline` | `accent` | opaque |
| `list.hoverBackground` | `surface2` | opaque |
| `list.hoverForeground` | `fg` | opaque |
| `list.inactiveFocusOutline` | `accent` | opaque |
| `list.inactiveSelectionBackground` | `selection` | opaque |
| `list.inactiveSelectionForeground` | `fg` | opaque |
| `menu.background` | `surface2` | opaque |
| `menu.foreground` | `fg` | opaque |
| `menu.selectionBackground` | `selection` | opaque |
| `menu.selectionBorder` | `accent` | opaque |
| `menu.selectionForeground` | `fg` | opaque |
| `menu.separatorBackground` | `surface` | opaque |
| `notificationCenterHeader.background` | `surface` | opaque |
| `notificationCenterHeader.foreground` | `fg` | opaque |
| `notifications.background` | `surface2` | opaque |
| `notifications.border` | `surface` | opaque |
| `notifications.foreground` | `fg` | opaque |
| `panel.background` | `surface` | opaque |
| `panel.border` | `surface2` | opaque |
| `panelTitle.activeBorder` | `accent` | opaque |
| `panelTitle.activeForeground` | `fg` | opaque |
| `panelTitle.inactiveForeground` | `muted` | opaque |
| `selection.background` | `selection` | opaque |
| `sideBar.background` | `surface` | opaque |
| `sideBar.border` | `surface2` | opaque |
| `sideBar.foreground` | `fg` | opaque |
| `sideBarSectionHeader.background` | `surface` | opaque |
| `sideBarSectionHeader.border` | `surface2` | opaque |
| `sideBarSectionHeader.foreground` | `fg` | opaque |
| `sideBarTitle.foreground` | `fg` | opaque |
| `statusBar.background` | `surface` | opaque |
| `statusBar.border` | `surface2` | opaque |
| `statusBar.debuggingBackground` | `surface2` | opaque |
| `statusBar.debuggingForeground` | `fg` | opaque |
| `statusBar.foreground` | `fg` | opaque |
| `statusBar.noFolderBackground` | `surface` | opaque |
| `tab.activeBackground` | `bg` | opaque |
| `tab.activeBorderTop` | `accent` | opaque |
| `tab.activeForeground` | `fg` | opaque |
| `tab.border` | `surface2` | opaque |
| `tab.inactiveBackground` | `surface` | opaque |
| `tab.inactiveForeground` | `muted` | opaque |
| `widget.border` | `surface2` | opaque |
| `diffEditor.insertedLineBackground` | `string` | `1A` |
| `diffEditor.insertedTextBackground` | `string` | `33` |
| `diffEditor.removedLineBackground` | `error` | `1A` |
| `diffEditor.removedTextBackground` | `error` | `33` |
| `editor.findMatchBackground` | `accent` | `33` |
| `editor.findMatchHighlightBackground` | `accent` | `1A` |
| `editor.inactiveSelectionBackground` | `selection` | `80` |
| `editor.wordHighlightBackground` | `accent` | `1A` |
| `editor.wordHighlightStrongBackground` | `accent` | `1A` |
| `scrollbarSlider.activeBackground` | `muted` | `77` |
| `scrollbarSlider.background` | `muted` | `33` |
| `scrollbarSlider.hoverBackground` | `muted` | `55` |

Bracket pair colors and OS window decorations are not configured. Terminal mappings are documented [separately](vscode-terminal.md). The theme colors supported custom title bars without changing the user’s title-bar style or window controls. [VS Code 1.146.0 Modern UI theming](https://raw.githubusercontent.com/microsoft/vscode/1.146.0/src/vs/workbench/contrib/modernUI/README.md) describes these experimental surfaces; they require a host build supporting Modern UI and the relevant setting. All 13 shell, frame and title-bar keys are registered in [VS Code 1.143.0](https://github.com/microsoft/vscode/blob/1.143.0/src/vs/workbench/common/theme.ts); registration does not guarantee the Modern UI layout is enabled or visually identical across hosts. Specialized views and host-dependent behavior remain unreviewed. Overlay colors composite with underlying content; the native review records observed search/diff text legibility and contrast limitations. No user settings or window layout are changed.
