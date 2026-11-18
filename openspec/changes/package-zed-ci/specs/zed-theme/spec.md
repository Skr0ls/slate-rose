## ADDED Requirements

### Requirement: Deliver a validated Zed package in CI

The Quality workflow SHALL validate generated Zed JSON against the official
theme schema and upload a downloadable development extension after successful
validation.

#### Scenario: Download the CI artifact

- **WHEN** the Zed packaging job succeeds
- **THEN** the artifact contains `extension.toml`, `LICENSE`, `README.md`, and `themes/slate-rose.json`
- **AND** the installation guide explains how to select the extracted directory in Zed
