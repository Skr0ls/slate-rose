# VS Code mapping and limitations

The generated JSON uses the [VS Code theme schema](https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/workbench/services/themes/common/colorThemeSchema.ts), [editor color keys](https://code.visualstudio.com/api/references/theme-color), and [semantic highlighting](https://raw.githubusercontent.com/microsoft/vscode-docs/main/api/language-extensions/semantic-highlight-guide.md). Semantic tokens overlay TextMate grammar colors. Provider classifications vary, so the mappings do not promise parity between languages or providers. The [fixture review](../previews/vscode/README.md) records observed rendering and its limits. A local VSIX can be built and installed using the [instructions](../README.md#local-vs-code-installation).

Local verification on VS Code 1.143.1 arm64 confirmed VSIX installation and Slate Rose selection using the official VS Code API; a native theme export matched all 10 configured editor colors. The four standalone fixtures were subsequently reviewed with the providers and screenshots listed in the [visual review](../previews/vscode/README.md). Owner acceptance and broader provider behavior remain unverified.

| Role | Semantic token types | TextMate scopes |
| --- | --- | --- |
| Type | type, class, enum, struct, typeParameter; interface uses interface | entity.name.type, support.type |
| Function | function, method | entity.name.function, support.function |
| Property | property, event | specific variable and entity property scopes, including C# fields |
| Variable / parameter | variable / parameter | variable.other.readwrite, entity.name.variable, variable.other.constant / variable.parameter, entity.name.variable.parameter |
| Namespace | namespace | entity.name.namespace, entity.name.type.namespace, entity.name.type.module |
| Constant | enumMember | variable.other.constant.cs, variable.other.enummember, entity.name.variable.enum-member, constant.other |
| Attribute | decorator | entity.name.function.decorator, entity.other.attribute-name, support.other.attribute |
| Comment / string / number | comment / string, regexp / number | comment / string / constant.numeric |
| Operator | operator | keyword.operator |
| Declaration | — | keyword, storage |
| Flow | — | specific keyword.control flow scopes and C# await expression scope |
| Primitive | — | specific primitive scopes and C# keyword.type |
| Punctuation | — | punctuation |

There is no semantic keyword override: generic keyword tokens cannot distinguish declarations from flow control. Providers can still override lexical distinctions. No declaration or readonly modifier override is applied: local variables stay quiet and readonly fields classified as properties stay rose. Default-library types such as Task and Guid are not treated as primitives. Named constants outside reliably distinguished grammar or provider categories may remain quiet. TypeScript const bindings remain quiet in lexical fallback; the specific `variable.other.constant.object.property` scope colors an intermediate property such as `obj.CONFIG.value`, while a root such as `CONFIG.value` stays quiet. Primitive recognition is limited to explicit lexical scopes; providers can obscure it. In the reviewed C# fixture, the semantic `keyword` overlay colors `string` lilac even though its `keyword.type.string.cs` TextMate scope would match the primitive rule; the [review](../previews/vscode/README.md) records the inspection. Broad `storage.type` remains a declaration, and broad `keyword.control` remains a keyword.

The lexical mappings were informed by the official [C++](https://raw.githubusercontent.com/microsoft/vscode/main/extensions/cpp/syntaxes/cpp.tmLanguage.json), [C#](https://raw.githubusercontent.com/microsoft/vscode/main/extensions/csharp/syntaxes/csharp.tmLanguage.json), [TypeScript](https://raw.githubusercontent.com/microsoft/vscode/main/extensions/typescript-basics/syntaxes/TypeScript.tmLanguage.json), and [Python](https://raw.githubusercontent.com/microsoft/vscode/main/extensions/python/syntaxes/MagicPython.tmLanguage.json) grammars. The exact selectors are in the generator.

The JavaScript, JSX, and TSX grammars group `try`, `catch`, `finally`, and `throw` under `keyword.control.trycatch`. Language-scoped lexical rules color that group as flow control in those modes; the group cannot distinguish `throw` from the other three keywords. The [web review](../previews/vscode/web/README.md) records the observed scopes and provider limitations.

The editor background, foreground and selection use their corresponding approved tokens. These remaining editor colors reuse existing palette tokens provisionally:

| VS Code key | Palette token |
| --- | --- |
| editorCursor.foreground | accent |
| editorLineNumber.foreground | muted |
| editorLineNumber.activeForeground | fg |
| editor.lineHighlightBackground | surface |
| editor.findMatchBorder | accent |
| editorError.foreground | error |
| editorWarning.foreground | warning |

Bracket pair colors are not configured by the theme, so native VS Code defaults remain visible. Workbench colors also retain native defaults.
