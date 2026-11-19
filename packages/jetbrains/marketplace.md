# JetBrains Marketplace submission

| Field | Value |
| --- | --- |
| Name | Slate Rose |
| Plugin ID | `com.github.skr0ls.slaterose` |
| Version | `0.1.1` |
| Vendor | `Skr0ls` |
| Channel | Stable |
| Pricing | Free |
| Tags | Select the relevant theme tag offered by the upload form |
| Source | https://github.com/Skr0ls/slate-rose |
| License | [MIT](https://github.com/Skr0ls/slate-rose/blob/main/LICENSE) |
| Support | [GitHub Issues](https://github.com/Skr0ls/slate-rose/issues) |

## Description

Slate Rose is a dark theme for JetBrains IDEs. It pairs graphite editor
surfaces with sand types, blue functions, rose fields, lilac declarations,
and green strings. The Islands Dark theme also styles the window frame,
tool windows, tabs, and status bar.

Select **Slate Rose** under **Settings → Appearance & Behavior → Appearance**
after installing. Exact syntax colors depend on the IDE and language plugin.

## Change notes

First JetBrains Marketplace release. Includes the Slate Rose editor scheme,
Islands Dark UI colors, and the Slate Rose Marketplace icon.

## Screenshot

Use the [Rider screenshot](../../previews/jetbrains/csharp-builtins/after.png)
to show the bundled UI theme and C# highlighting. The original capture is
JPEG data. Upload it with a `.jpg` extension.

## Maintainer handoff

Build or check `dist/slate-rose-jetbrains.jar` using the
[package guide](README.md).

1. Open the [Marketplace upload form](https://plugins.jetbrains.com/docs/marketplace/uploading-a-new-plugin.html)
   and accept the Developer Agreement. Create the
   [Vendor profile](https://plugins.jetbrains.com/docs/marketplace/organizations.html)
   with public name `Skr0ls`, a working contact email and website, and the
   applicable trader status. Choose the Vendor ID carefully because it is permanent.
2. Select the `Skr0ls` Vendor, leave the channel field empty for Stable, and
   add the listing details and screenshot.
3. Submit the verified JAR for review. After approval, install Slate Rose
   from Marketplace and confirm that the theme appears in Appearance settings.

## Future updates

JetBrains documents authenticated updates through the
[plugin upload API](https://plugins.jetbrains.com/docs/marketplace/plugin-upload.html).
After the first listing is accepted, a maintainer can create the publishing
token under **My Tokens**.

| API field | Value |
| --- | --- |
| `xmlId` | `com.github.skr0ls.slaterose` |
| `file` | Verified `slate-rose-jetbrains.jar` |
| `channel` | Omit or leave empty for Stable |
