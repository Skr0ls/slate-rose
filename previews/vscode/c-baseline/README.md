# VS Code C baseline

**Limited** for flow-control color. This review used a byte-identical copy of
[`fixtures/showcase.c`](../../../fixtures/showcase.c) in VS Code 1.146.0 on
macOS arm64, with language ID `c` and Microsoft C/C++ 1.35.6. IntelliSense
reported Ready and Parsing Complete in an isolated profile with the
standalone file open in a test folder without a C build configuration.
The active Slate Rose 0.3.0 theme JSON matched the artifact at `f01f98a`.

Apple clang 21.0.0 accepted
`clang -std=c17 -Wall -Wextra -Werror -fsyntax-only fixtures/showcase.c`.
The sample was inspected without execution.

The lexical check used the shipped TextMate engine and the bundled
`cpp/syntaxes/c.tmLanguage.json` grammar for `source.c`. The native check used
**Developer: Inspect Editor Tokens and Scopes** at the listed editor
positions. A dash indicates no semantic token was shown.

| Token (position) | TextMate scope | Lexical | Semantic type | Effective |
| --- | --- | --- | --- | --- |
| `struct` (3:10) | `storage.type.struct.c` | `#CAA1DE` | — | `#CAA1DE` |
| `int` (4:6) | `storage.type.built-in.primitive.c` | `#D8B981` | — | `#D8B981` |
| `Sample` type use (8:19) | `meta.function.definition.parameters.c` | `#D1D4DC` | `type` | `#E0C38C` |
| `sample_total` (8:6) | `entity.name.function.c` | `#8CC6F1` | `function` | `#8CC6F1` |
| `value` declaration (4:10) | `meta.block.c` | `#D1D4DC` | `property` | `#E28DA4` |
| `sample.value` member (12:30) | `variable.other.member.c` | `#D1D4DC` | `property` | `#E28DA4` |
| `SAMPLE_LIMIT` use (11:22) | `meta.parens.block.c` | `#D1D4DC` | `macro` | `#8CC6F1` |
| `for`, `if`, `return` (10:6, 11:10, 15:6) | `keyword.control.c` | `#CAA1DE` | — | `#CAA1DE` |

The C grammar assigns `keyword.control.c` to both the sampled flow keywords
and the `_Pragma` operator. IntelliSense supplied no narrower category for
these flow tokens. An override of the shared scope would also recolor
`_Pragma`, so this review retains the existing mapping. The sampled macro
use is blue through the provider's fallback to the preprocessor function
scope. Other toolchains, providers, and build configurations remain
unverified.
