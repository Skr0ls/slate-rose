## ADDED Requirements

### Requirement: Record baseline C highlighting evidence

The project SHALL provide a C fixture and record the sampled lexical and native foregrounds with the observed provider categories.

#### Scenario: Inspect a standalone C fixture

- **WHEN** the fixture is opened in VS Code in C mode with the Microsoft C/C++ provider
- **THEN** the review identifies fixture, host and provider versions, context and sampled categories
- **AND** the evidence distinguishes lexical behavior, semantic behavior and coverage limits
