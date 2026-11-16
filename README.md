# Slate Rose

Slate Rose is an original dark color theme for VS Code, JetBrains IDEs, and Zed.

**Status:** The v0.2 Contrast design baseline is approved and palette validation
is available. There are no installable themes yet.

## Design

Slate Rose pairs cool graphite surfaces with muted, legible syntax colors:

- Sand for types and blue for functions.
- Rose for fields, lilac for declarations, and coral for flow control.
- Green for strings, with ordinary variables and punctuation kept quiet.

The approved [palette](palette/colors.json) is the source of truth. The
[design baseline](docs/design-baseline.md) records language examples, editor
targets, architecture, and outstanding UI design work.

## Editor support

The project plans separate adapters for VS Code, JetBrains IDEs, and Zed, with
Visual Studio investigated separately. VS Code is the first planned editor-only
implementation. Host-specific limitations and mappings will be documented as
each adapter is built.

## Development

With Python 3.11 or newer, validate the canonical palette and run the tests:

```sh
python -m generators validate
python -m unittest discover -s tests -v
```

Pass a path after `validate` to check another palette. The schema requires only
`name`, `version`, and `colors` at the root, with all 24 supported color tokens.
Validation reads the input without modifying it.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the workflow and local checks.
[OpenSpec](openspec/README.md) contains the backlog and specifications; the
first implementation checklist is
[add-vscode-editor-theme](openspec/changes/add-vscode-editor-theme/tasks.md).

## License

Slate Rose is licensed under the [MIT License](LICENSE).
