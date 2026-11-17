## Purpose

Keep C# builtin type aliases visually distinct from ordinary keywords in the JetBrains editor scheme without changing other language roles.

## ADDED Requirements

### Requirement: Narrow builtin type styling
In the reviewed Rider host, C# builtin type aliases `int`, `string`, `float` and `bool` SHALL use the approved primitive foreground at declaration and usage sites. Ordinary declaration keywords SHALL retain their existing keyword color, named reference types SHALL retain their type color, and `var` SHALL NOT be recolored merely because type aliases are keywords. Host inspections and unused-code overlays SHALL remain available.

#### Scenario: Aliases beside keywords and reference types
- **WHEN** a valid, successfully loaded C# fixture is opened with the generated scheme
- **THEN** builtin aliases use the approved primitive foreground and named types such as `String` and `Task` use their existing type foreground
- **AND** ordinary keywords and contextual identifiers retain their existing mappings, subject to documented host overlays

### Requirement: Bounded host behavior
The change SHALL preserve core and terminal palettes, UI mappings, VS Code output and the documented VS Code C# decision. Evidence SHALL identify the actual Rider build, loaded project and available SDK, inspected categories and before/after results. A failed project load SHALL NOT count as semantic acceptance.

#### Scenario: Native review with project context
- **WHEN** the updated package is reviewed in the isolated Rider context
- **THEN** the fixture loads successfully, positive alias targets and unaffected controls are inspected, and package identity and limitations are recorded
- **AND** the review makes no claim of Java, Kotlin, other IDE or provider parity
