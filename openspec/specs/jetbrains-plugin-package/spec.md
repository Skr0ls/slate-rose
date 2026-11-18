# jetbrains-plugin-package Specification

## Purpose

Provide a reproducible locally installable JetBrains theme package with consistent resource references and the MIT license.

## Requirements

### Requirement: Local resource-only package
The package SHALL contain a valid plugin descriptor, registered UI theme, unchanged generated editor scheme and root MIT license. All resource references SHALL resolve inside the JAR. It SHALL declare a minimum platform build and require no runtime plugin code or bundled third-party assets.

#### Scenario: Install from disk
- **WHEN** the package is installed in the reviewed Rider host
- **THEN** Slate Rose appears as a UI theme and can be selected with its associated editor scheme
- **AND** installation/version limits are documented without implying wider IDE acceptance or publication

### Requirement: Safe reproducible packaging
Packaging SHALL reject stale generated resources and invalid descriptor references before writing. Unchanged inputs SHALL produce identical JAR bytes with fixed metadata. Package checks SHALL be read-only and reject modified/stale archives. Build output SHALL not overwrite an input through direct paths or aliases.

#### Scenario: Verification and failure
- **WHEN** a source is stale, a reference is invalid, or output aliases an input
- **THEN** packaging fails without changing existing output or creating its parent
- **AND** a valid repeated package is byte-identical and passes the read-only check
