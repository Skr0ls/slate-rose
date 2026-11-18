# Rider Islands shell review

This bounded review used Rider 2026.2.4, build 262.11879.110, in an isolated
test context with local plugin version 0.1.0. The installed JAR and the built
`dist/slate-rose-jetbrains.jar` had the same SHA-256:
`db5ad7238a57cdb84dead9c56af24ecfa1d8768020db1969e17bf956addf37ca`.

Appearance settings identified the UI theme as Slate Rose, provider UUID
`b981d7bb-b7a6-4d8b-a2c1-94d502763610`, and the editor scheme as Slate Rose
Theme default. The local plugin installed and the theme was selected.
The isolated profile's `config/options/laf.xml` persisted the same theme ID.

The observed frame, gaps, status bar, tabs and panels followed the approved
shell allocation. The inactive window retained the frame and tab colors while
host controls and the toolbar dimmed. Project toolbar color overlay and user
preferences were preserved.

- [Active window](active.png): the project loaded with .NET SDK 8.0.418.
- [Inactive window](inactive.png): owner-supplied capture from an earlier
  context, when the project reported a load failure; its geometry differs.

The captures are unmodified. Hashes are recorded in
[verification.json](verification.json).

After correcting the isolated project's SDK selection, an offline build succeeded
with no warnings or errors; the project was not executed. The active capture
shows sand type highlighting and inherited dimming of unused code. It does not
establish broader semantic or IDE acceptance. Menus and controls remain
inherited and outside this shell slice.
