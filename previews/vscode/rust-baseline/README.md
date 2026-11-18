# VS Code Rust baseline

**Semantic reviewed for the sampled roles.** The review used a byte-identical
copy of [`fixtures/showcase.rs`](../../../fixtures/showcase.rs) in VS Code
1.146.0 on macOS arm64, with language ID `rust`, rust-analyzer 0.3.3121
(server `946b80a756`), Rust 1.92.0 and Slate Rose 0.3.0. The temporary Cargo
project used edition 2021 and no external dependencies. The toolchain had
the `rust-src` component available during inspection. The fixture passed
`rustfmt --check` and `rustc --emit=metadata -Dwarnings` as a library.
The fixture was not executed.

The bundled `source.rust` TextMate grammar was replayed at baseline and
after the change. The native **Developer: Inspect Editor Tokens and Scopes**
command provided effective colors with rust-analyzer active.

| Token (line) | TextMate scope | Lexical before → after | Semantic category | Effective before → after |
| --- | --- | --- | --- | --- |
| `str` (6) | `entity.name.type.primitive.rust` | `#E0C38C` → `#D8B981` | `builtinType` | `#E0C38C` → `#D8B981` |
| `usize` (22) | `entity.name.type.numeric.rust` | `#E0C38C` → `#D8B981` | `builtinType` | `#E0C38C` → `#D8B981` |
| `if`, `return` (23–24) | `keyword.control.rust` | `#CAA1DE` → `#CAA1DE` | `keyword.controlFlow` | `#CAA1DE` → `#D7829B` |
| `for` in `impl` (10) | `keyword.control.rust` | `#CAA1DE` → `#CAA1DE` | `keyword` | `#CAA1DE` → `#CAA1DE` |

The updated inspector also confirmed `bool` as a sand `builtinType`.
The numeric TextMate scope includes type suffixes. A separate lexical
probe showed that `42usize` and `1.0f32` retain amber digits with a sand
suffix.

In the baseline inspector, the `Describe` trait was sand, `self.text`
was rose as a `property`, the `label_length!` macro name was blue,
and the `'a` lifetime was lilac. The field access lacks a distinguishing
lexical scope in this fixture and receives rose from the semantic provider.

The bundled grammar uses the same lexical control scope for `if` and the
`for` in an impl declaration. Semantic `keyword.controlFlow:rust`
separates the two here. With only the bundled grammar, the sampled flow
words still use lilac. This review covers the stated fixture and provider.
See the [rust-analyzer token tags and modifiers](https://rust-analyzer.github.io/book/features.html#semantic-syntax-highlighting).
