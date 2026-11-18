# C++ baseline regression review

On 2026-11-18, a bounded lexical review used the unchanged `fixtures/showcase.cpp` and the installed VS Code 1.146.0 bundled C++ grammar (`cpp` language ID). The fixture SHA-256 was `8bdd277c9ddcd9c459e3a9702252cf034b9bdf4e260737df496823bc18ebccf2`; the checked-in generated theme SHA-256 was `e58481e490e2712fef1444f68066bf68f6cd98f00fd9e9d5ce32b9c5ade7c3e3`. Apple clang 21.0.0 accepted `clang++ -std=c++17 -fsyntax-only fixtures/showcase.cpp`; the fixture was not executed.

To reproduce the lexical probe, run VS Code's `Contents/MacOS/Code` as Node with `ELECTRON_RUN_AS_NODE=1`, load `vscode-textmate` and `vscode-oniguruma` from `Contents/Resources/app/node_modules.asar`, initialize the shipped `node_modules.asar.unpacked/vscode-oniguruma/release/onig.wasm`, and tokenize each fixture line in order with `source.cpp` from `extensions/cpp/syntaxes/cpp.tmLanguage.json`, retaining the previous line's rule stack. Compare the scopes against `tokenColors` in the generated theme. This does not evaluate semantic overlays or native rendering.

| Fixture evidence (line) | Lexical scope and theme mapping |
| --- | --- |
| `LabelRenderer` class (8), `std::string` (12) | `entity.name.type` maps to sand |
| Constructor (10), `render` (12), `out_of_range` call (14) | `entity.name.function` maps to blue |
| `prefix_` declaration (24), use (16), initializer (10) | `variable.other.declare` and `variable.other.unknown` have no field-specific rule; initializer is `entity.name.function.call.initializer`, which maps to blue |
| `int` (6, 12, 17) | `storage.type.built-in.primitive` maps to primitive sand |
| `class`, `constexpr`, `public`, `const` (8, 6, 9, 12) | `storage` scopes map to lilac |
| `if`, `for` (13, 17); `throw`, `return` (14, 20) | `keyword.control.if` and `keyword.control.for` fall back to lilac; `keyword.control.throw` and `keyword.control.return` map to coral |
| `preview` namespace (5) | `entity.name.namespace` maps to namespace rose |
| `max_labels` (6, 13), `prefix` parameter (10) | `variable.other.unknown` has no specific theme rule; `variable.parameter` maps to foreground |
| String literal (14) | `string` maps to green |

The scope table alone does not establish effective colors. A separate native inspection used VS Code 1.146.0, Microsoft C/C++ 1.35.6, an isolated profile and extensions directory (`/tmp/sr-swift-code` and `/tmp/sr-swift-extensions`), and the active Slate Rose theme. IntelliSense reported Ready and Parsing Complete. The byte-identical fixture copy was opened at `/private/tmp/sr-web-context/javascript/slate-rose-cpp-baseline.cpp` in a previously trusted disposable JavaScript test folder, without a C++ build configuration. Use **View → Command Palette → Developer: Inspect Editor Tokens and Scopes** at the stated positions to inspect the effective results:

| Position and token | Native inspection |
| --- | --- |
| 8:9 `LabelRenderer`, 12:33 `render` | Semantic type `#E0C38C`; method `#8CC6F1` |
| 16:32 `prefix_` | Semantic property `#E28DA4` overrides the unknown lexical scope |
| 6:12 `int` | Lexical `#D8B981` |
| 13:10 `if`, 17:10 `for` | Lexical `#CAA1DE` |
| 14:14 `throw`, 20:11 `return` | Lexical `#D7829B` |
| 14:39 string | Lexical `#A9CE91` |

The unedited [native capture](native.png) shows the field inspector; its SHA-256 is `0fe986632873c5c3d655a9d9117210605115435f39f0fd223b76ce7609f1b247`. The `if` and `for` categories are candidates for separate review, not a mapping change. The historical [native review](../README.md) used VS Code 1.143.1 in a different context. Other fixtures, configurations, provider versions and hosts remain unverified.
