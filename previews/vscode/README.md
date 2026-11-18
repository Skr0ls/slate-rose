# VS Code fixture review

On 2026-11-16, the four standalone fixtures were reviewed in VS Code 1.143.1 arm64 on macOS, using Slate Rose 0.3.0 in an isolated temporary profile. No project, TypeScript configuration, or C++ compile database was opened. These observations cover the pictured examples, not every token or provider configuration. Owner acceptance remains pending.

| Fixture | Provider and context | Screenshot |
| --- | --- | --- |
| Python | ms-python.python 2026.10.0 and vscode-pylance 2026.4.1 | [Python](python.png) |
| TypeScript | Built-in tsserver 6.0.3; no tsconfig or opened folders | [TypeScript](typescript.png) |
| C++ | ms-vscode.cpptools 1.35.6; IntelliSense Ready | [C++](cpp.png) |
| C# | ms-dotnettools.csharp 2.160.4 and vscode-dotnet-runtime 3.2.0; Miscellaneous Files (not all features available) | [C#](csharp.png), [top of file](csharp-top.png) |

In the C++, TypeScript, and C# examples, named types appeared sand, functions blue, and fields rose. In Python, `prefix` appeared in the ordinary foreground, `@dataclass` blue, and `MAX_LABELS` in the ordinary foreground. In TypeScript, `@describe` appeared blue and the `MAX_LABELS` const binding in the ordinary foreground. In C#, primitive `int` and `string`, and flow keywords `await`, `throw`, and `return`, appeared lilac; `MaxLabels` appeared in the ordinary foreground and `Description` sand.

Developer: Inspect Editor Tokens and Scopes at C# line 11, column 23 identified `string` as semantic token type `keyword`, with foreground `#CAA1DE` from fallback `keyword.cs` to the generic lexical keyword/storage rule. Its actual TextMate scope `keyword.type.string.cs` in `source.cs` would match `source.cs keyword.type` and produce `#D8B981`; the semantic overlay obscures that primitive distinction. On 2026-11-16, the owner chose to retain semantic highlighting and document this limitation. No special workaround was applied. Provider classifications can differ in other contexts.

Native bracket pair colors were visible because the theme does not configure them; workbench colors also retain native defaults. Screenshots are unedited full surfaces and include blank white areas. Full semantic correctness, cross-provider parity, and unpictured token behavior were not established.

## Build verification

A clean temporary output directory was used for validation, theme generation, and packaging. The checked-in theme and approved palette were unchanged; a separately generated theme matched byte for byte. All 15 unit tests and all pre-commit hooks passed. Two VSIX builds were byte-identical, and both passed the package checker. Their SHA-256 was `060002b113301a953b9ffb4e332c894a30ff56dab5e262520444e9492056ec4c`. Python 3.14.3 and Node 26.13.0 were used.

The checks follow the [development](../../README.md#development), [contribution](../../CONTRIBUTING.md#local-checks), and [local installation](../../README.md#local-vs-code-installation) instructions. For the reproducibility check, package twice from `packages/vscode` with `SOURCE_DATE_EPOCH=1794787200 TZ=UTC npx --yes @vscode/vsce@4.1.1 package --no-dependencies --out <fresh-output-path>`, run `python scripts/check_vsix.py` on each archive from the repository root, and compare the archives byte for byte.
