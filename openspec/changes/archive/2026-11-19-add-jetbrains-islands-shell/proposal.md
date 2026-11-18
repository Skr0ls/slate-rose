# Proposal

## Why

The editor scheme is reviewed, but the surrounding JetBrains UI still uses host colors. Deliver a small, installable Islands shell before expanding language or IDE validation.

## What Changes

- Generate an Islands Dark child theme for approved shell, panel and tab colors.
- Package it with the unchanged editor scheme and MIT notice as a local resource-only plugin JAR.
- Add reproducible build/check commands and CI artifact delivery; verify installation and representative framing on Rider only.

## Capabilities

### New Capabilities

- `jetbrains-ui-theme`: approved Islands shell colors with native interactions retained.
- `jetbrains-plugin-package`: deterministic local theme packaging and consistency checks.

### Modified Capabilities

None.

## Impact

Adds a Python renderer, generated theme JSON, plugin descriptor, small package script, focused tests and installation notes. Core/terminal palettes, syntax mappings and existing generated schemes remain unchanged. Menus, inputs, other control states, terminal mapping, wider IDE acceptance and publication are later slices. The owner approved the color allocation in this session.
