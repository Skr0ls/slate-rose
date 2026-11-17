# Rider Islands shell review

This partial review used Rider 2026.2.4, build 262.11879.110, in an isolated
test context with local plugin version 0.1.0. The installed JAR and the built
`dist/slate-rose-jetbrains.jar` had the same SHA-256:
`db5ad7238a57cdb84dead9c56af24ecfa1d8768020db1969e17bf956addf37ca`.

Appearance settings identified the UI theme as Slate Rose, provider UUID
`b981d7bb-b7a6-4d8b-a2c1-94d502763610`, and the editor scheme as Slate Rose
Theme default. The local plugin installed and the theme was selected.
The isolated profile's `config/options/laf.xml` persisted the same theme ID.

The observed frame, gaps, status bar, tabs and panels followed the approved
shell allocation. The selected tab's focus border changed when focus moved
from the editor to a tool window. Project toolbar color overlay and user
preferences were preserved.

- [Editor focused](editor-focused.png)
- [Tool window focused](tool-window-focused.png)

The captures retain the white padding present in the original screenshots.
Hashes are recorded in [verification.json](verification.json).

Whole-window inactivity was not reliably observed, so native shell acceptance
remains pending that check. The test project reported a load failure; these
captures do not establish new semantic highlighting acceptance or a successful
project build. Menus and controls remain inherited and outside this shell slice.
