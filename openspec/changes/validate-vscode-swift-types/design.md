# Design

## Context

See proposal.md. VS Code 1.146.0 has built-in Swift grammar 10.0.0. Official extension `swiftlang.swift-vscode` 2.18.0 is installed only in `/tmp/sr-swift-extensions`; Apple Swift 6.4 and SourceKit-LSP are installed. Compatibility and actual semantic classifications require live evidence, not version inference. The adapter already maps standard type categories to sand and generic keywords to lilac.

## Goals / Non-Goals

Review one Swift macOS library fixture in VS Code. Preserve approved palette, generators, generated artifacts, user profiles and historical fixtures. No Xcode/JetBrains/Zed coverage, broad keyword recoloring or parser changes. Confirmed narrow mapping candidates are separate follow-up work.

## Decisions

- Add `fixtures/swift/TypeRoles.swift` covering Int/String/Bool/Float annotations and initializer expressions, optional shorthand/Optional, Array and a generic struct, typealias declaration/use, a tiny protocol with any/some type contexts, properties/methods and let/var/func/struct/typealias versus if/return/throw. Keep it original and small, without main or fixture execution.
- Create a dependency-free disposable SwiftPM library under the previously trusted `/tmp/sr-web-context/javascript/swift-review`. Record its tiny manifest/setup in fixture instructions rather than adding a build system to the repository. Verify with installed compiler typecheck or library build only; never run the fixture or tests. Restore missing project/toolchain context before semantic claims.
- Use isolated VS Code data/extensions directories. Package the current generated theme as a checked VSIX, install it in the isolated profile, and record hashes; leave personal extensions/settings unchanged. Select Slate Rose and verify theme/provider activation and resolved project context before capture. Do not disable semantic highlighting globally or alter trust protections.
- Inspect lexical TextMate scopes separately from semantic tokens, using native token inspector and, if helpful, a bounded SourceKit-LSP probe. Label direct LSP results as provider evidence rather than claiming VS Code selected them. Verify representative built-ins, alias, initializer and any/some/keyword controls in the host; group equivalent occurrences honestly.
- Deliver concise `previews/vscode/swift/README.md`, compact verification metadata and at most two unmodified native captures. Record host/grammar/extension/compiler versions, project context, actual selected theme hash, token categories and colors with lexical/semantic distinction. An unavailable provider or inseparable category is a documented limitation, not proof of universal absence. Update only the Swift backlog entry.

## Risks / Trade-offs

- Newer Swift toolchain than extension documentation -> observe activation and token results, record limitations.
- Lexical and semantic layers may differ -> inspect both without blanket disabling semantics; use inspector fallbacks/source grammar to distinguish layers.
- Initializer names can have constructor/function categories -> compare independently from explicit type positions, without forcing them into type roles.
- macOS service shortcut conflicts -> open command actions through menus, never use Cmd+Shift+A.
