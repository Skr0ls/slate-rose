# jetbrains-editor-scheme Specification

## Purpose

Provide a reproducible JetBrains editor color scheme from the approved Slate Rose palette, with explicit boundaries for host verification.

## Requirements

### Requirement: Native editor scheme
The generator SHALL emit a standalone UTF-8 `.icls` scheme named Slate Rose, inheriting Darcula and using only approved core RGB values. It SHALL map shared language categories where IntelliJ exposes them, without changing fonts, IDE UI or terminal settings.

#### Scenario: Shared language roles
- **WHEN** the canonical palette is built for JetBrains
- **THEN** the XML defines sand classes/interfaces, blue functions/methods, rose fields, lilac keywords, green strings, amber numbers and foreground variables/parameters
- **AND** text background, cursor, current line, line numbers, gutter and selection use documented core palette roles

### Requirement: Safe deterministic commands
The CLI SHALL support `build jetbrains` and `check jetbrains`, with host-specific default output and existing palette/output options. Both palettes SHALL be validated before writing. Checks SHALL be read-only; stale or missing output and invalid inputs SHALL fail without modifying inputs or output. Existing VS Code commands SHALL retain their behavior.

#### Scenario: Reproduction and staleness
- **WHEN** unchanged inputs are built twice
- **THEN** output bytes are identical
- **AND** checking stale or missing output fails without writing

#### Scenario: Input protection
- **WHEN** a palette is invalid or the output aliases a selected or canonical palette, including by symlink or hardlink
- **THEN** the command fails before creating directories or modifying files

### Requirement: Honest support boundary
Documentation SHALL describe import instructions and distinguish generated XML checks from native Rider/IntelliJ acceptance. Unmapped categories and language overrides SHALL be documented as inherited, without claiming full semantic parity.

#### Scenario: Initial adapter delivery
- **WHEN** the first scheme is delivered
- **THEN** documentation links official format/key references and marks native language review, UI/plugin packaging and terminal mapping as follow-up work
