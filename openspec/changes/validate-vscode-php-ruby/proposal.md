# Proposal

## Why

PHP and Ruby are the remaining languages in the initial web review batch. Their built-in grammars need direct inspection before the project can describe their lexical coverage or provider limitations.

## What Changes

- Add small PHP and Ruby fixtures with applicable types, methods, fields, variables, control flow, literals and interpolation.
- Review both in an isolated VS Code profile using the built-in language extensions; query semantic-token availability and record absent providers without claiming semantic coverage.
- Record screenshots, exact token inspections, editor/provider versions, artifact identity and validation limits.
- Correct only observed PHP/Ruby mapping discrepancies, then rebuild, reinstall and repeat affected review when the theme changes.

## Capabilities

### New Capabilities

- `vscode-php-ruby-validation`: Bounded lexical review and explicit semantic-provider coverage for PHP and Ruby.

### Modified Capabilities

None.

## Impact

Adds fixtures and review evidence, with potential narrow changes to VS Code mappings and regression tests. The palette, other adapters, runtime dependencies and publication flow remain unchanged. Third-party language-server validation remains a separate follow-up when no semantic provider is present in the selected built-in profile.
