# release-assets Specification

## Purpose

Define how validated Slate Rose packages are assembled for a GitHub release.

## Requirements

### Requirement: Assemble release assets from a single validated run

The Quality workflow SHALL provide a downloadable bundle from the verified
package artifacts in the same run.

#### Scenario: A successful package run

- **WHEN** the host package jobs succeed
- **THEN** the bundle contains `slate-rose.vsix`, `slate-rose-jetbrains.jar`, and `slate-rose-zed.zip`
- **AND** the Zed archive has deterministic bytes for identical inputs and preserves the extension directory layout

### Requirement: Describe release preparation

The repository SHALL document how to select a validated bundle and attach the
three assets to a reviewed GitHub Release draft.

#### Scenario: A maintainer prepares a release

- **WHEN** a maintainer downloads the bundle for the selected commit
- **THEN** the maintainer can identify each platform asset and its installation guide
