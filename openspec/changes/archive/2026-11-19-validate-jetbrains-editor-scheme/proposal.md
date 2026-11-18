# Proposal

## Why

The first JetBrains adapter has automated XML checks but no native import or language review. Verify the delivered scheme in Rider and IntelliJ before designing UI or packaging a plugin.

## What Changes

- Add a small Java fixture and minimal C# project context reusing the existing fixture.
- Import the generated scheme through each IDE's documented UI and review representative code and editor states.
- Retain two overview captures and a concise reproduction/coverage record, with actual host versions and limitations.

## Capabilities

### New Capabilities

None: this change verifies existing behavior and updates documentation (`skip_specs: true`).

### Modified Capabilities

None. Record observed mapping gaps for a separate focused fix rather than expanding this validation PR.

## Impact

Fixtures, review evidence and support documentation only. Palettes, generators, generated schemes, UI/plugin/terminal features and publication are outside this slice. Native checks must remain pending if a host or provider is unavailable; XML validity is not native acceptance.
