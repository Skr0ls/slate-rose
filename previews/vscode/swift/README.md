# VS Code Swift type review

The bounded native review found built-in types in sand, while the inspected
flow-control keywords remained lilac and a generic declaration was foreground.
The latter two are candidates for separate mapping work.

The [fixture](../../../fixtures/swift/TypeRoles.swift) was copied unchanged into
a dependency-free SwiftPM library. Its SHA-256 is
`de2c116872c1c423e950532311386435a35cf4c0322453611d873b86b3f2aa14`.
Apple Swift 6.4 typechecked it offline with an explicit Command Line Tools SDK;
the fixture was not executed. Setup is in the [fixture instructions](../../../fixtures/swift/README.md).

The target environment is VS Code 1.146.0 (arm64, commit
`69047191fc427f2f92828279aae1d90d8eeda7ab`), built-in Swift grammar 10.0.0,
official Swift extension 2.18.0 and Apple Swift 6.4
(`swiftlang-6.4.0.34.1`, target `arm64-apple-macosx27.0.0`). The isolated profile
and extensions directory are under `/tmp`. The trusted disposable project showed
Swift 6.4.0, zero Problems, and selected SourceKit semantic tokens. Slate Rose
was selected in the isolated window; its editor background was `#191D25`.
The checked VSIX SHA-256 is `f1e3f3b52f58e213d16510e4e4f62853abba2c8c8fbc7fe6ad740d2dd19087e6`;
its theme matches generated JSON SHA-256
`e58481e490e2712fef1444f68066bf68f6cd98f00fd9e9d5ce32b9c5ade7c3e3`.

To reproduce, follow the [local VSIX packaging and installation guide](../../../packages/vscode/README.md#build-from-source)
using isolated user data `/tmp/sr-swift-code` and extensions `/tmp/sr-swift-extensions`,
then select Slate Rose. Open the disposable project described in the fixture instructions.
Use Go → Go to Line/Column for the positions below, then View → Command Palette →
Developer: Inspect Editor Tokens and Scopes. Do not use Cmd+Shift+A.

## Native inspection

Positions below are the cursor positions inside tokens. The inspector reports
the effective foreground and selected semantic category where present.
[Inspector capture](inspector.png) and [overview](overview.png) are unmodified.

| Role and position | Selected category or lexical scope | Foreground |
| --- | --- | --- |
| `Int` annotation 36:17 and initializer 36:23; `String` 37:17, `Bool` 38:19, `Float` 39:18 | `struct.defaultLibrary` (lexical `support.type.swift`) | `#E0C38C` |
| `Optional` 21:28 | `enum.defaultLibrary` | `#E0C38C` |
| `Count` declaration 13:12; use 17:17 | `entity.name.type.typealias.swift` without semantic token; `typeParameter` | `#E0C38C` |
| `Value` generic declaration 9:13; use 10:17 | `variable.language.generic-parameter.swift` without semantic token or matching theme selector; `typeParameter` | `#D1D4DC`; `#E0C38C` |
| `any` 45:25; opaque `some` 49:28 | `keyword.other.operator.type.existential.swift`; `keyword.other.operator.type.opaque.swift`, without semantic tokens | `#CAA1DE` |
| `Describable` 45:29; `Optional.some` 41:70 | `interface`; `enumMember.defaultLibrary` | `#E0C38C`; `#D99AAB` |
| `Item` initializer 40:13 | `struct`, overriding lexical `support.function.any-method.swift` (`#8CC6F1`) | `#E0C38C` |
| `enabled` reference 28:14; `explicitOptional` declaration 21:18 | `property`; enclosing `meta.*` only, without semantic token | `#E28DA4`; `#D1D4DC` |
| `struct` 15:2; `typealias` 13:2 | `storage.type.struct.swift`; `keyword.other.declaration-specifier.swift` | `#CAA1DE` |
| `if` 28:10; `throw` 29:14; `return` 31:10 | `keyword.control.branch.swift`; `keyword.control.exception.swift`; `keyword.control.transfer.swift`, without semantic tokens | `#CAA1DE` |

The `if`, `throw`, and `return` observations are narrow candidates for coral
flow-control mapping. The generic declaration is a separate candidate; the
property declaration is a bounded provider/grammar limitation. No mapping or
palette change was made here. Other positions and providers may differ.

## Lexical probe

The installed Swift TextMate grammar was tokenized separately with VS Code's
shipped TextMate 9.3.2 and Oniguruma 1.7.0. The table gives the innermost scope
at representative positions (line:column), not resolved theme colors.

| Fixture role | Examples | Innermost scope |
| --- | --- | --- |
| Built-in annotations and initializers | `Int` 36:16, 36:22; `String` 37:15, 37:24; `Bool` 38:18, 38:25; `Float` 39:17, 39:25 | `support.type.swift` |
| Optional and generic built-ins | `Int` 20:24; `Optional` 21:27; `Array` 22:18 | `support.type.swift` |
| Optional punctuation | `?` 20:27 | `keyword.operator.type.optional.swift` |
| Alias | `Count` declaration 13:11; use 17:16 | `entity.name.type.typealias.swift`; `meta.definition.type.body.swift` |
| User generic | `Box` declaration 9:8; annotation 23:16; initializer 42:47 | `entity.name.type.struct.swift`; `meta.definition.type.body.swift`; `meta.function-call.swift` |
| Protocol in existential and opaque contexts | `Describable` 45:28, 49:32 | `meta.parameter-clause.swift`; `meta.function-result.swift` |
| Contextual type words | `any` 45:24; `some` 49:27 | `keyword.other.operator.type.existential.swift`; `keyword.other.operator.type.opaque.swift` |
| Declaration controls | `let` 16:5, `var` 17:5, `typealias` 13:1; `struct` 15:1; `func` 27:5 | `keyword.other.declaration-specifier.swift`; `storage.type.struct.swift`; `storage.type.function.swift` |
| Flow controls | `if` 28:9; `throw` 29:13; `return` 31:9 | `keyword.control.branch.swift`; `keyword.control.exception.swift`; `keyword.control.transfer.swift` |

These scopes are lexical evidence for this fixture and grammar version only.
Semantic classifications and actual theme resolution require separate inspection:
VS Code can layer semantic highlighting over TextMate highlighting. See the
[VS Code semantic highlighting guide](https://code.visualstudio.com/api/language-extensions/semantic-highlight-guide),
the Swift language reference on [types](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/types/)
and [lexical structure](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/lexicalstructure/),
and the [Swift extension 2.18.0 release](https://github.com/swiftlang/vscode-swift/releases/tag/2.18.0).

## Direct semantic provider probe

A separate SourceKit-LSP request against the disposable project, with the SDK
explicitly supplied, returned 53 semantic tokens decoded using the provider's
advertised legend. These are provider results, not proof that VS Code selected
those tokens or colors. Representative categories are:

| Role | Provider classification |
| --- | --- |
| `Int`, `String`, `Bool`, `Float` annotations and initializers; `Array` | `struct.defaultLibrary` |
| `Optional` | `enum.defaultLibrary` |
| `Count` alias use and generic `Value` use | `typeParameter` |
| `Box` and `Item` references | `struct` |
| `Describable` references, including after `any` and `some` | `interface` |
| Property references; locals and parameters | `property`; `variable` |

Many declaration names did not receive a token in this response; this does not
prove they lack lexical scopes or that another provider context behaves the same.
