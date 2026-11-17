# Proposal

## Why

Rider currently renders C# builtin type aliases as lilac keywords. A registered C#-specific category lets the theme express the approved primitive role without changing ordinary keywords; address this before expanding to Zed.

## What Changes

- Map the verified Rider C# builtin-type category to the existing primitive color.
- Add a focused fixture and native before/after review for aliases, named types and keyword controls in a successfully loaded project.
- Keep VS Code's documented C# limitation and other language mappings unchanged; Java and Kotlin receive separate reviews.

## Capabilities

### New Capabilities

- `jetbrains-csharp-highlighting`: narrow builtin-type styling with host-specific validation and documented limits.

### Modified Capabilities

None.

## Impact

Touches the JetBrains editor renderer and generated scheme, focused tests/fixtures, installation evidence and mapping documentation. Rebuild/check the local plugin after the Islands package PR is integrated. No palette, UI mapping, parser, runtime plugin, semantic-highlighting preference or VS Code output changes.
