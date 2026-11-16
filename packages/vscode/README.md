# Slate Rose

Slate Rose is a prototype dark editor theme. Install the local VSIX using
**Extensions: Install from VSIX...**, then choose **Preferences: Color Theme**
and select **Slate Rose**. The package targets VS Code 1.143 and newer; the
current compatibility review is limited to the 1.143 series.

The intended syntax roles are sand types, blue functions, rose fields, lilac
declarations, coral flow control and green strings. Language providers can
classify tokens differently. Four standalone fixtures were reviewed in VS Code
1.143.1 with specific providers; see the [review and limitations](https://github.com/Skr0ls/slate-rose/blob/dev/previews/vscode/README.md). Owner acceptance remains pending.

C# semantic keyword tokens can override the lexical primitive and flow colors;
the theme retains semantic highlighting without a generic keyword override,
which cannot distinguish those roles. Editor UI colors beyond the base palette
are provisional. This package is not published to the Marketplace.

Licensed under the MIT License; see the included LICENSE notice.
