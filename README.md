# Slate Rose

Slate Rose is a dark color theme for VS Code, JetBrains IDEs, and Zed. It uses
sand for types, blue for functions, rose for fields, lilac for declarations,
coral for flow control, and green for strings. Exact roles depend on the
editor and language provider.

## Installation

Download the three installable packages from
[GitHub Releases](https://github.com/Skr0ls/slate-rose/releases) or get
`slate-rose-release-assets` from a successful
[Quality workflow run](https://github.com/Skr0ls/slate-rose/actions/workflows/quality.yml).
GitHub requires sign-in for workflow downloads.

| Editor | File | Instructions |
| --- | --- | --- |
| VS Code | `slate-rose.vsix` | [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=skr0ls.slate-rose) · [Install from VSIX](packages/vscode/README.md#installation) |
| JetBrains IDEs | `slate-rose-jetbrains.jar` | [Install from disk or import the editor scheme](packages/jetbrains/README.md) |
| Zed | `slate-rose-zed.zip` | [Extract and install the development extension](packages/zed/README.md) |

## Development

The approved colors live in [palette](palette/). The Python
[generators](generators/) build the host-specific files in [packages](packages/).
[Fixtures](fixtures/) and [review evidence](previews/README.md) document examples
and observed editor behavior. See [Contributing](CONTRIBUTING.md) for development commands,
[OpenSpec](openspec/README.md) for the backlog, and the
[release guide](docs/releasing.md) for preparing a GitHub Release.

The [design baseline](docs/design-baseline.md) describes the palette roles and
host design. The [VS Code mappings](docs/vscode-mappings.md) and
[terminal notes](docs/vscode-terminal.md) record host-specific limits.

## License

Slate Rose is licensed under the [MIT License](LICENSE).
