# VS Code web syntax review

Manual review on 2026-11-16 used VS Code 1.146.0 arm64 (commit `69047191fc427f2f92828279aae1d90d8eeda7ab`), built-in `vscode.typescript-language-features` 10.0.0 and bundled TypeScript 6.0.3. The branch started at `86a8053f0d7e0c5238ebd891a130046b51394f5a`, after PR 4 merged. These screenshots are manual evidence, not automated tests; they do not establish coverage of other languages or React projects.

The corrected Slate Rose 0.3.0 package was installed in the isolated `/tmp/sr-web-verify` profile with extensions in `/tmp/sr-web-ext`, followed by **Developer: Reload Window**. After screenshots, the package README was updated and the package rebuilt twice with byte-identical results, then reinstalled. The final VSIX SHA-256 was `9b7309c5c9f940a348d08cc0536a962d015bb35c796bd3b77874e3a55390936d`; its packaged theme and the final installed theme both matched the generated theme byte-for-byte (SHA-256 `42e4b6a2a857035f573af16993edc9880a7c7ec7be6d4f2a4492eb39eeff3c8a`), unchanged from the screenshots. The approved palette remained unchanged (SHA-256 `9086de1f1a752b95db890fe531753e9ab7bfea05b0f0b6cf23de35f541a0581d`).

## Context and outcomes

The GUI opened copies of the three fixtures under `/tmp/sr-web-context/{javascript,jsx,tsx}`; each copy matched its repository source byte-for-byte. Lexical screenshots were taken in Restricted Mode with semantic highlighting disabled. Semantic screenshots were taken with semantic highlighting enabled after trusting only `/private/tmp/sr-web-context/javascript`. The GUI workspace was `javascript`; language status reported no jsconfig or tsconfig and that files were not part of the opened folders. Therefore the GUI frames are evidence from that reported context, not evidence that the configured projects below were active in the GUI.

| Fixture and mode | Lexical review | Semantic review |
| --- | --- | --- |
| JavaScript (`javascript`) | Limited: representative roles observed; constructor references are blue in lexical fallback. [Screenshot](javascript-lexical.png) | Passed for the representative sample; constructor references become sand. [Screenshot](javascript-semantic.png) |
| JSX (`javascriptreact`) | Limited: representative roles observed; component tag distinction is limited. [Screenshot](jsx-lexical.png) | Limited: representative sample observed; component tag distinction is not established. [Screenshot](jsx-semantic.png) |
| TSX (`typescriptreact`) | Limited: representative roles observed; component tag remains foreground. [Screenshot](tsx-lexical.png) | Limited: representative sample observed; component tag remains foreground without a semantic token. [Screenshot](tsx-semantic.png) |

In a separate native API probe, the workspace was `/tmp/sr-web-context`, with independent minimal configurations as described in the [fixture guide](../../../fixtures/README.md). No React dependency was installed. After tokens became available, the probe waited eight seconds per file before collecting diagnostics: JavaScript, JSX, and TSX returned 18, 19, and 31 semantic tokens respectively, with no diagnostics at collection time. The decoded [token data](semantic-tokens.json) records positions, classifications, and modifiers. A separate bundled TypeScript 6.0.3 compiler API check of the TSX project (`ES2022`, JSX preserve) returned zero diagnostics. This probe establishes token availability in the configured context, not visual acceptance there.

## Observations

The samples show `if` and `const` in lilac; `return`, `await`, and corrected `throw` in coral; ordinary variables and const bindings in foreground; and strings and numbers in their approved colors. Attributes are lilac and embedded properties are rose. Native bracket and workbench defaults remain visible.

- [JavaScript class inspection](javascript-class-inspection.png) shows semantic class declaration `LabelRenderer` in sand (`#E0C38C`); constructor references are blue lexically and sand semantically.
- [JSX function inspection](jsx-function-inspection.png) shows semantic function declaration `Label` in blue (`#8CC6F1`).
- [TSX interface inspection](tsx-interface-inspection.png) shows semantic interface declaration `LabelProps` in sand (`#E0C38C`).
- [TSX component inspection](tsx-component-inspection.png) shows `Label` at line 23, column 12 as `jsx-tags`, with no semantic token and no matching theme selector. Its `support.class.component.tsx` scope remains foreground (`#D1D4DC`); the enclosing scopes include `entity.name.tag.tsx` and `source.tsx`.

Initial manual inspection recorded `throw` in lilac (`#CAA1DE`). The installed grammars group `try`, `catch`, `finally`, and `throw` under `keyword.control.trycatch`. The correction scopes this group to JavaScript/JSX and TSX without changing TypeScript or C# mappings. The final [JSX throw inspection](jsx-throw-after.png) and [TSX throw inspection](tsx-throw-after.png) show the respective contextual selectors in coral (`#D7829B`). These captures show `throw` itself, at line 3, column 7 in JSX and line 15, column 7 in TSX.

The regression was observed failing before the correction; after correction, all 16 unit tests, palette validation, generator build and check, pre-commit hooks, and the real VSIX check passed. Strict OpenSpec validation also passed. These observations cover the fixtures and layers described above, not the broader web-language backlog.
