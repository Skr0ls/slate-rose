# VS Code PHP and Ruby review

This bounded review used VS Code 1.146.0 arm64 (commit `69047191fc427f2f92828279aae1d90d8eeda7ab`) and Slate Rose 0.3.0. The built-in `vscode.php`, `vscode.php-language-features`, and `vscode.ruby` extensions were version 10.0.0. The final screenshots show a standalone window in Restricted Mode with semantic highlighting enabled. They show lexical fallback in this context, not semantic color coverage.

The [PHP](../../../fixtures/showcase.php) and [Ruby](../../../fixtures/showcase.rb) fixtures were copied byte-for-byte to `/tmp/sr-web-context/javascript/php-ruby`. Their respective SHA-256 hashes were `839f69b839680bd83f271f65ce0c5807a67e27f40539b7fa964c48a91588601c` and `7de39a381cae4328bb24e771c84ea9c0d1db5c3d0e769c1ba4ba1ac22c3f0390`. The examples require no application framework.

| Language | Lexical result | Semantic result |
| --- | --- | --- |
| PHP (`php`) | Limited: class sand, method blue, namespace rose, field usage rose; declaration `$prefix` foreground. `return` coral; `if`, `for`, `string`, `int`, and `throw` lilac. | Unavailable in the selected built-in profile; semantic colors not reviewed. |
| Ruby (`ruby`) | Limited: class sand, method blue, instance fields rose, ordinary locals and parameters foreground. `MAX_LABELS` and `ArgumentError` references foreground; `raise` and `return` lilac. | Unavailable in the selected built-in profile; semantic colors not reviewed. |

The Ruby instance-field rule was added after initial inspection and verified in the final installed theme, including interpolation. PHP primitive and exception scopes and Ruby raise/return scopes combine different roles in the installed grammars; they retain their existing mappings. See [mapping limitations](../../../docs/vscode-mappings.md).

## Final installed inspections

Screenshots were captured after reinstalling the final artifact. Positions are line and column in the fixture; colors are the observed foreground for the inspected token.

| Screenshot | Inspected token and scope |
| --- | --- |
| [PHP overview](php-overview.png) | Fixture overview |
| [Ruby overview](ruby-overview.png) | Fixture overview |
| [PHP class](php-class-inspection.png) | `LabelRenderer` 6:10, `#E0C38C`, `entity.name.type.class.php` |
| [PHP primitive](php-primitive-inspection.png) | `string` 9:15, `#CAA1DE`, `keyword.other.type.php` |
| [PHP field](php-field-inspection.png) | `prefix` 13:18, `#E28DA4`, `variable.other.property.php` |
| [PHP throw](php-throw-inspection.png) | `throw` 19:16, `#CAA1DE`, `keyword.control.exception.php` |
| [Ruby field](ruby-field-inspection.png) | `prefix` 7:10, `#E28DA4`, `variable.other.readwrite.instance.ruby`; the `@` sigil stays quiet. |
| [Ruby raise](ruby-raise-inspection.png) | `raise` 12:12, `#CAA1DE`, `keyword.other.special-method.ruby` |
| [Ruby return](ruby-return-inspection.png) | `return` 20:10, `#CAA1DE`, `keyword.control.pseudo-method.ruby` |

In a separate extension development host with workspace `/tmp/sr-web-context/javascript`, the built-in PHP features extension was activated. The public `vscode.provideDocumentSemanticTokensLegend` and `vscode.provideDocumentSemanticTokens` commands returned undefined for both exact language modes after bounded retries. The [provider record](provider-results.json) captures the outcomes. This separate query does not infer provider availability from the screenshot window’s Restricted Mode. Third-party PHP and Ruby language-server coverage remains queued.

## Artifact and checks

The fixed-metadata VSIX was built twice with vsce 4.1.1 and the packages were byte-identical. VSIX SHA-256: `00ec5994f021c39c9a917f5471a395adb638161eb190b79722a7598e6ed07bc8`. Generated, packaged, and installed theme JSON SHA-256: `48b6557af9703584e6c15502aebe87a1bef0953218958a6979f7fe583f56665c`. Approved palette SHA-256: `9086de1f1a752b95db890fe531753e9ab7bfea05b0f0b6cf23de35f541a0581d`.

Palette validation, generator build and check, 17 unit tests, pre-commit hooks, strict OpenSpec validation, and the VSIX archive checker passed. Ruby 2.6.10 returned `Syntax OK` for `ruby -c`; PHP CLI was unavailable, so PHP lint was not run. Screenshots are manual review evidence, not automated tests. Workbench and bracket colors retain VS Code defaults.
