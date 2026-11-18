# Proposal

## Why

The three editor packages are already built and checked in CI. A release
needs their installable files together, with a ZIP for Zed.

## What Changes

Assemble the existing CI packages as a single downloadable release bundle
and document the path from that bundle to a reviewed GitHub Release.

## Capabilities

### New Capabilities

- `release-assets` gathers the VS Code, JetBrains and Zed packages from one validated commit.

## Impact

The Quality workflow, a small archive helper and release documentation.
