# Fixture review

Open each `showcase` file in VS Code with its relevant language provider. These
are examples for visual review. The [review record](../previews/vscode/README.md)
shows observed rendering for one set of providers; classifications can vary.

| Example | Intended palette role |
| --- | --- |
| `LabelRenderer` | Type (sand) |
| `render`, `RenderAsync` | Function (blue) |
| `prefix`, `prefix_`, `Prefix` | Field or property (rose) |
| `class`, `private`, `const`, `if` | Keyword or declaration (lilac) |
| `return`, `throw`, `await` | Flow control (coral) |
| `"too many labels"`, `3` | String (green), number (amber) |
| `MAX_LABELS`, `MaxLabels`, `max_labels` | Named constant (rose) |
| `preview`, `Preview` | Namespace (rose) |
| `[[nodiscard]]`, `[Description]`, `@describe`, `@dataclass` | Attribute (lilac) |
| `label`, `count`, `result` | Parameter or variable (foreground) |

Not every syntax category is present in every language. See the
[VS Code mappings](../docs/vscode-mappings.md) for fallback and provider limits.
