# zed-theme Specification

## Purpose

Define how Slate Rose is generated, validated, packaged, and installed as a Zed development extension.

## Requirements

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

### Requirement: Deliver a validated Zed package in CI

The Quality workflow SHALL validate generated Zed JSON against the official
theme schema and upload a downloadable development extension after successful
validation.

#### Scenario: Download the CI artifact

- **WHEN** the Zed packaging job succeeds
- **THEN** the artifact contains `extension.toml`, `LICENSE`, `README.md`, and `themes/slate-rose.json`
- **AND** the installation guide explains how to select the extracted directory in Zed
