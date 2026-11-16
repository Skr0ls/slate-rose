# Spec Delta

## Purpose

Provide an installable VS Code editor theme that expresses Slate Rose semantic roles consistently and can be reproduced from the approved palette.

## ADDED Requirements

### Requirement: Preserve semantic roles
The theme SHALL map supported semantic tokens and lexical fallback scopes to approved roles: sand types, blue functions, rose fields, lilac declarations, control-colored flow keywords and green strings. Ordinary variables and parameters SHALL retain the approved foreground.

#### Scenario: Semantic highlighting is available
- **WHEN** the active language provider supplies supported semantic classifications
- **THEN** the theme applies the corresponding palette roles

#### Scenario: Semantic highlighting is unavailable
- **WHEN** only lexical classifications are available
- **THEN** supported fallback scopes are colored and distinctions that cannot be represented are documented

### Requirement: Deterministic generation and checks
Identical palette and mapping inputs SHALL produce byte-identical theme artifacts. A check command SHALL report invalid inputs or stale generated artifacts with a nonzero exit code without rewriting artifacts.

#### Scenario: Repeated build
- **WHEN** the generator runs twice with unchanged inputs
- **THEN** both outputs are byte-identical

#### Scenario: Stale output
- **WHEN** a checked-in artifact differs from the expected generated result
- **THEN** check mode fails and identifies the stale artifact

### Requirement: Local installation and visual review
The project SHALL provide a locally installable VS Code theme package, installation instructions and representative C++, C#, TypeScript and Python fixtures. Documentation SHALL distinguish verified behavior, provisional editor UI mappings and unverified language-specific coverage.

#### Scenario: Local review
- **WHEN** a reviewer follows the documented installation and fixture instructions
- **THEN** Slate Rose is selectable and the fixtures expose types, functions, fields, declarations, flow control and literals for review

### Requirement: Preserve native interface behavior
The initial theme SHALL customize syntax and basic editor colors using documented VS Code keys and existing palette values. It SHALL preserve native layouts, icons and interaction behavior, and leave full workbench styling for a subsequent change.

#### Scenario: Theme activation
- **WHEN** the theme is activated
- **THEN** editor colors change without adding commands or replacing interface components
