# Fixture review

The [JetBrains setup](jetbrains/README.md) reuses the C# example in a minimal
project and adds `LabelRenderer.java`; its [native review](../previews/jetbrains/editor/README.md)
records the initial Rider and IntelliJ observations.

Open each `showcase` file in VS Code with its relevant language provider. These
are examples for visual review. The [review record](../previews/vscode/README.md)
shows observed rendering for one set of providers; classifications can vary.

The web fixtures use the `javascript`, `javascriptreact`, and `typescriptreact`
language modes for `.js`, `.jsx`, and `.tsx`, respectively. They compare
component and intrinsic tags, attributes, props, and embedded expressions. The
TSX fixture declares a minimal local `JSX` namespace; no React dependency is
needed for the examples. Provider context and actual review results are recorded
separately in the web review evidence.

For isolated language-service projects, copy each fixture into its own directory
and add a configuration containing only that file. Use `target: "ES2022"` in
each project; set `checkJs: false` for both JavaScript projects and
`jsx: "preserve"` for JSX and TSX. Use `jsconfig.json` for JavaScript and JSX,
and `tsconfig.json` with `noEmit: true` for TSX. Separate projects avoid global
declaration collisions between the examples.

| Example | Intended palette role |
| --- | --- |
| `LabelRenderer` | Type (sand) |
| PHP `string`, `int` | Primitive type (sand) |
| Ruby `ArgumentError` | Named type (sand) |
| PHP `$this->prefix`; Ruby `@prefix` | Field (rose) |
| PHP `self::MaxLabels`; Ruby `MAX_LABELS` | Named constant (rose) |
| PHP `throw`; Ruby `raise`, `return` | Flow control (coral), where distinguishable |
| `render`, `RenderAsync` | Function (blue) |
| `prefix`, `prefix_`, `Prefix` | Field or property (rose) |
| `class`, `private`, `const`, `if` | Keyword or declaration (lilac) |
| `return`, `throw`, `await` | Flow control (coral) |
| `"too many labels"`, `3` | String (green), number (amber) |
| `MAX_LABELS`, `MaxLabels`, `max_labels` | Named constant (rose) |
| `preview`, `Preview` | Namespace (rose) |
| `[[nodiscard]]`, `[Description]`, `@describe`, `@dataclass` | Attribute (lilac) |
| `label`, `count`, `result` | Parameter or variable (foreground) |

The PHP and Ruby fixtures use the `php` and `ruby` language modes. They are
standalone visual examples and do not require a framework. Their [review record](../previews/vscode/php-ruby/README.md) identifies the
actual grammar and semantic provider context and distinguishes the intended
roles above from observed colors.

Not every syntax category is present in every language. See the
[VS Code mappings](../docs/vscode-mappings.md) for fallback and provider limits.
