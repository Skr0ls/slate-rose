## ADDED Requirements

### Requirement: Swift control statement foreground

The VS Code theme SHALL use the approved control foreground for the verified Swift TextMate contexts of `if`, `throw`, and `return`.

#### Scenario: Swift flow control in the reviewed fixture

- **WHEN** VS Code tokenizes the reviewed Swift conditional, exception statement, and return with their native Swift TextMate scopes
- **THEN** the theme assigns the control foreground to the three statements
- **AND** the sampled declaration keywords and contextual type words retain their keyword foreground
