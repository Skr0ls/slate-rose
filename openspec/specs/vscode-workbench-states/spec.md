# vscode-workbench-states Specification

## Purpose

Provide coherent Slate Rose workbench colors and distinguish interactive states in VS Code while preserving native window behavior and approved syntax colors.

## Requirements

### Requirement: Palette-derived workbench surfaces
The theme SHALL use approved palette colors for workbench text, editor groups, tabs, sidebars, Activity Bar, panels, status bar, inputs, menus, completion and hover widgets, notifications, separators and scrollbars. Active editor surfaces SHALL use bg, surrounding panels surface, and raised widgets surface2.

#### Scenario: Open the installed theme
- **WHEN** Slate Rose is selected and editor, sidebar and bottom panel are visible
- **THEN** these regions use the documented palette-derived mappings and retain native layout and controls

### Requirement: Distinguishable interaction states
The theme SHALL distinguish active and inactive tabs, active and inactive selection, hover, keyboard focus and disabled text. Focus and active indicators SHALL use accent without making every separator an accent border.

#### Scenario: Navigate with keyboard and pointer
- **WHEN** focus moves between an input, list and editor and the pointer hovers a scrollbar
- **THEN** focused controls, selection and scrollbar hover remain identifiable using documented state colors

### Requirement: Search and diagnostic overlays
The theme SHALL define search matches, current search result, word highlights and error, warning, information and hint states using existing palette roles. Overlay backgrounds SHALL retain underlying text visibility; current search results SHALL have an accent border.

#### Scenario: Find text and inspect diagnostics
- **WHEN** a document contains multiple search matches and representative diagnostics
- **THEN** the current match is distinct and severity decorations remain visible without opaque overlays covering code

### Requirement: Git and diff state colors
The theme SHALL distinguish additions with green, modifications with blue and removals with error colors in Git decorations, gutters and diff views. Diff text and line backgrounds SHALL be transparent palette-derived overlays.

#### Scenario: Compare changed files
- **WHEN** a native diff contains added, modified and removed content
- **THEN** the corresponding decorations remain identifiable and code remains legible over diff backgrounds

### Requirement: Native host and syntax preservation
The theme SHALL preserve syntax mappings, palette bytes, operating-system window decorations and user window settings. It SHALL use supported VS Code color keys, without runtime code, CSS injection or terminal ANSI overrides.

#### Scenario: Install and switch themes
- **WHEN** the local extension is installed and Slate Rose is selected
- **THEN** only theme resources change, native title-bar configuration remains untouched, and existing syntax roles remain unchanged

### Requirement: Reproducible output and observed review
The theme SHALL remain deterministically generated and locally installable. Review evidence SHALL identify host version, package and installed-theme identity, tested UI states and unverified behavior separately from automated checks and owner acceptance.

#### Scenario: Review a local package
- **WHEN** fixed-metadata packages are built and the final package is installed in an isolated profile
- **THEN** repeated package bytes match, installed theme bytes match generated output, and native screenshots document the UI states actually inspected

### Requirement: Modern UI shell and frame colors
The theme SHALL color Modern UI gutters and supported custom title-bar backgrounds with bg in active and inactive windows, and floating-card frame borders with surface2. Title foregrounds SHALL remain readable. It SHALL preserve native gap sizes, rounding, controls and user title-bar style settings.

#### Scenario: Inspect Modern UI window framing
- **WHEN** the installed theme is displayed with Modern UI and the window gains or loses focus
- **THEN** shell gutters and supported title-bar fills use the approved background, frame lines use the documented palette mapping, and native geometry remains unchanged
