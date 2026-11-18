## ADDED Requirements

### Requirement: Record baseline Go highlighting evidence

The project SHALL provide a Go fixture and record sampled lexical and native foregrounds with the observed provider categories.

#### Scenario: Inspect a Go fixture with gopls

- **WHEN** a copy of the fixture is opened in VS Code in a minimal Go module
- **THEN** the review identifies the fixture, host, provider, token categories and foregrounds
- **AND** it records topical limitations and distinguishes lexical fallback from native semantic behavior

### Requirement: Go lexical roles use their palette foregrounds

The VS Code theme SHALL assign the approved primitive and control foregrounds to the observed Go lexical scopes.

#### Scenario: Inspect the Go fixture without a semantic overlay

- **WHEN** the bundled grammar assigns numeric, string or boolean builtin type scopes or the Go control scope
- **THEN** primitive types are sand and flow words are coral
- **AND** declaration keywords retain their lilac foreground
