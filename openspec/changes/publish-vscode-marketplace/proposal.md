## Why

Slate Rose has a public VS Code Marketplace listing. Maintainers need a
repeatable way to publish the same VSIX users can download from GitHub Releases.

## What Changes

Add manual VS Code Marketplace publication through GitHub Actions and Microsoft
Trusted Publishing.

## Capabilities

### Modified Capabilities

- `release-assets` gains verification and publication of the released VSIX.

## Impact

GitHub Actions, the release guide, and the VS Code Marketplace listing.
