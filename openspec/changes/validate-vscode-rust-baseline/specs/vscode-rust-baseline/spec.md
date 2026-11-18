## ADDED Requirements

### Requirement: Record baseline Rust highlighting evidence

The project SHALL provide a Rust fixture and record lexical and native colors with the observed token categories.

#### Scenario: Inspect a Rust library fixture

- **WHEN** the fixture is opened with the bundled VS Code grammar and rust-analyzer in a minimal Cargo project
- **THEN** the review records the fixture, provider version, sampled categories and foregrounds
- **AND** the evidence distinguishes lexical behavior, semantic behavior and coverage limits

### Requirement: Distinguish Rust primitive types and semantic flow keywords

The VS Code theme SHALL assign the approved primitive foreground to the observed Rust builtin type categories and the approved control foreground to Rust keywords with the semantic `controlFlow` modifier.

#### Scenario: Color the fixture with rust-analyzer

- **WHEN** the provider assigns `builtinType` to a primitive or `keyword.controlFlow` to a Rust flow token
- **THEN** the theme renders the respective primitive sand or coral
- **AND** the unmodified `for` keyword in an impl declaration retains lilac

#### Scenario: Apply bundled lexical fallback

- **WHEN** the bundled grammar identifies a Rust primitive or numeric type scope
- **THEN** the theme renders it using the primitive foreground
- **AND** the shared lexical control scope retains its current behavior
