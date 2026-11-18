# Design

Use the existing C# fixture in an isolated VS Code profile. Compare the bundled grammar output with the token inspector after the Microsoft C# provider is ready. Inspect `if`, `for`, `throw` and `await`, with a declaration keyword as a control. Preserve semantic highlighting and the approved palette. Keep the existing decision for primitive aliases.

Bind `controlKeyword:csharp` to the existing control foreground. Scope the selector to the C# language ID and retain existing lexical rules, including the fallback for files without the Microsoft C# provider.
