# VS Code Python baseline

**Limited** for the sampled dataclass field, with lexical and semantic evidence
recorded below. A byte-identical copy of [`fixtures/showcase.py`](../../../fixtures/showcase.py)
was inspected in an isolated VS Code 1.146.0 profile on macOS arm64. The
language ID was `python`, with Microsoft Python 2026.10.0 and Pylance 2026.4.1.
VS Code selected Homebrew Python 3.15.0. The test folder had no Python project
configuration. Slate Rose 0.3.0 was installed from a VSIX, and its theme JSON
matched the checked-in artifact at commit `766483d`. The fixture was not
executed.

Lexical colors were checked with the shipped TextMate engine and bundled
MagicPython grammar. Native colors and semantic types came from
**Developer: Inspect Editor Tokens and Scopes** with Pylance active.
Coordinates are inspector positions. A dash indicates that the inspector
showed no semantic token.

| Token | TextMate scope | Lexical | Semantic type | Effective |
| --- | --- | --- | --- | --- |
| `class` (9:3) | `storage.type.class.python` | `#CAA1DE` | — | `#CAA1DE` |
| `str` (10:14) | `support.type.python` | `#D8B981` | `class` | `#E0C38C` |
| `render` (12:10) | `entity.name.function.python` | `#8CC6F1` | `method` | `#8CC6F1` |
| `dataclass` (8:3) | `entity.name.function.decorator.python` | `#CAA1DE` | `function` | `#8CC6F1` |
| `prefix` declaration (10:6) | `source.python` | editor foreground | `variable` | `#D1D4DC` |
| `self.prefix` member (15:29) | `meta.attribute.python` inside `meta.member.access.python` | editor foreground | `variable` | `#D1D4DC` |
| `MAX_LABELS` (5:3, 13:22) | `constant.other.caps.python` | `#D99AAB` | `variable` (reference has `readonly`) | `#D1D4DC` |
| `if`, `raise`, `for`, `return` (13:10, 14:14, 16:10, 18:10) | `keyword.control.flow.python` | `#D7829B` | — | `#D7829B` |

The sampled field receives the ordinary variable color at declaration and
access. The member-access scope identifies attribute syntax, which also
covers other member accesses. The declaration has only the
root lexical scope. The generic variable rule keeps the constant quiet. The
sampled built-in type stays sand through the semantic class color.

The effective field, decorator, and constant colors agree with the
[initial review](../README.md) and its [historical Python screenshot](../python.png).
The evidence supports retaining current
mappings for this fixture. Other providers, projects, and field forms remain
unverified.
