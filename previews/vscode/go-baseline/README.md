# VS Code Go baseline

**Limited** for semantic flow-control color. The review used a byte-identical
copy of [`fixtures/showcase.go`](../../../fixtures/showcase.go) in a
dependency-free temporary module with a `go 1.26.0` directive. The host was
VS Code 1.146.0 on macOS arm64 with the Go extension 0.58.0, gopls 0.23.0,
Go 1.26.2, and Slate Rose 0.3.0. The fixture was formatted with `gofmt` and
compiled with `go tool compile` to a temporary file without execution.

The bundled `source.go` grammar was replayed using the shipped TextMate
engine against the original and updated themes. Native results came from
**Developer: Inspect Editor Tokens and Scopes**. The semantic run enabled
`gopls.semanticTokens` and `[go].editor.semanticHighlighting.enabled` in the
temporary workspace. The lexical run turned both off in that workspace.
See the [gopls settings reference](https://go.dev/gopls/settings#semantictokens-bool).

| Token (line) | TextMate scope | Lexical before | Lexical after |
| --- | --- | --- | --- |
| `int` (3) | `storage.type.numeric.go` | `#CAA1DE` | `#D8B981` |
| `string` (6) | `storage.type.string.go` | `#CAA1DE` | `#D8B981` |
| `bool` (7) | `storage.type.boolean.go` | `#CAA1DE` | `#D8B981` |
| `for`, `if`, `return` (11–13) | `keyword.control.go` | `#CAA1DE` | `#D7829B` |
| `type` (5) | `keyword.type.go` | `#CAA1DE` | `#CAA1DE` |

The native lexical inspection matched the updated column. The grammar also
uses the control scope for words such as `defer`, `range`, and `select`.
It assigns `import` a separate scope, which retained lilac in a lexical
control probe.

In the semantic run, `for`, `if`, and `return` remained lilac, and `string`
was sand (`#E0C38C`). gopls reported the same unmodified `keyword` category
for the sampled flow words and for declarations such as `type`. The
inspector showed the type parameter `T` in sand and the declaration `Name`
and access `Active` as rose `property` tokens. Without the semantic
overlay, `Name` retains rose through its lexical property scope, and
`Active` access uses the ordinary foreground through `variable.other.go`.
Other provider and project contexts remain unverified.
