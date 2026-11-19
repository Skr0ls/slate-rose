## Tasks

- [x] Implement and review a manual workflow with dry-run verification and isolated OIDC publishing.
- [x] Configure the GitHub environment and the Trusted Publishing policy for `skr0ls`.
- [x] Pass dry-run for the VSIX on the published `v0.1.0-preview.2` release.
- [x] Publish VS Code package `0.3.1` and verify the public listing.

## Verification

The [GitHub preview](https://github.com/Skr0ls/slate-rose/releases/tag/v0.1.0-preview.2)
is tagged at `68fa3fb`. The [dry-run](https://github.com/Skr0ls/slate-rose/actions/runs/44425173490)
compared its VSIX with the [Quality bundle](https://github.com/Skr0ls/slate-rose/actions/runs/44424897786)
and verified `skr0ls.slate-rose 0.3.1`.
SHA-256 `87f8aa7e2352ef9fb0156601b90653f4e4d540427a76eb1a263de775b7ce0219`.

The [publication workflow](https://github.com/Skr0ls/slate-rose/actions/runs/44425298472)
published the same package to the regular Marketplace channel using OIDC after
the publisher policy was registered. The public Marketplace download had the
same SHA-256 and contained the new icon and README.
The [public listing](https://marketplace.visualstudio.com/items?itemName=skr0ls.slate-rose)
shows version `0.3.1`, the updated README, and the workbench screenshot.
