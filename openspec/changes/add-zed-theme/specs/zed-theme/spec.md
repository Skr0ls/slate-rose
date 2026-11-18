## ADDED Requirements

### Requirement: Build a Slate Rose Zed theme

The shared CLI SHALL generate and check a deterministic Zed theme JSON file from the approved palette.

#### Scenario: Build and check a native artifact

- **WHEN** a contributor runs the Zed build and check commands
- **THEN** the generated file matches the official v0.2.0 schema
- **AND** color mappings use the approved palette and documented capture names
- **AND** stale or missing output fails the check

### Requirement: Install a theme-only extension locally

The repository SHALL include a Zed extension manifest and documented local installation steps.

#### Scenario: Select the locally installed theme

- **WHEN** a contributor installs the package as a development extension in Zed
- **THEN** Slate Rose is listed as a selectable dark theme
- **AND** the editor shows the specified colors while undeclared shell styles use Zed's defaults
