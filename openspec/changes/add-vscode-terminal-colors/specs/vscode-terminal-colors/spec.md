# Spec Delta

## Purpose

Provide a separately approved and validated ANSI palette with reproducible VS Code terminal mappings while preserving the accepted editor and workbench appearance.

## ADDED Requirements

### Requirement: Separate approved ANSI source
The project SHALL store exactly sixteen approved normal/bright ANSI colors separately from the unchanged 24-token syntax/UI palette. Values SHALL match the owner-approved preview and SHALL NOT be automatically adjusted during validation or generation.

#### Scenario: Load approved sources
- **WHEN** the canonical syntax/UI and terminal palettes are loaded
- **THEN** each is read-only, has its documented token set and preserves every approved hex value

### Requirement: Strict terminal input validation
Validation SHALL reject unreadable sources, malformed JSON, duplicate fields, missing or unknown fields/tokens, invalid metadata and non-six-digit hex values with an actionable error and nonzero CLI status.

#### Scenario: Invalid terminal palette
- **WHEN** validation, build or check receives an invalid terminal source
- **THEN** it reports the failure without rewriting either source, creating output directories or changing an existing artifact

### Requirement: Native terminal color mappings
The generated VS Code theme SHALL emit all sixteen supported ANSI keys with exact approved values plus documented terminal background, text, cursor, selection and search colors derived from the syntax/UI palette. Existing syntax and non-terminal colors SHALL remain unchanged.

#### Scenario: Deterministic generation
- **WHEN** identical validated sources are generated repeatedly
- **THEN** the output bytes match, include every normal/bright ANSI mapping and retain the complete pre-terminal syntax/workbench payload

### Requirement: Protected inputs and read-only checks
Build and check SHALL reject output paths aliasing either selected or canonical palette, including symlinks and hard links. Check SHALL remain read-only and report missing or stale output without altering it.

#### Scenario: Output aliases terminal source
- **WHEN** build or check targets a path referring to a terminal palette input
- **THEN** it fails before writing and preserves the source bytes

### Requirement: Host behavior preservation
The theme SHALL NOT modify shell profiles, terminal settings, automatic contrast, bold/bright preferences or cursor style. Documentation SHALL distinguish configured RGB values from any host renderer adjustment.

#### Scenario: Inspect terminal with host preferences
- **WHEN** normal, bright and bold ANSI output is viewed in the installed theme
- **THEN** the recorded host preferences remain effective and any rendering limitations are documented without silently changing approved colors

### Requirement: Installed terminal review
Review evidence SHALL record host version, effective relevant settings, source/package/installed-theme identity and native foreground/background, normal/bright, bold, selection and search observations. Controlled display output SHALL be reproducible without executing fixture scripts or relying on shell configuration.

#### Scenario: Review local terminal package
- **WHEN** the final reproducible VSIX is installed in an isolated profile and display-only ANSI output is shown
- **THEN** screenshots and an evidence matrix identify the inspected states and limitations separately from automated checks and owner acceptance
