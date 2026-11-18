# VS Code C# flow-color review

**Semantic reviewed for the sampled keywords.** The review used
[`fixtures/showcase.cs`](../../../fixtures/showcase.cs) in VS Code 1.146.0 on
macOS arm64. The language ID was `csharp`. A byte-identical copy was opened in
an isolated profile with Microsoft C# 2.160.4 and .NET Install Tool 3.2.0.
The workspace contained no C# project. Roslyn 5.12.0-1.26452.1 loaded
the file through its generated miscellaneous project after restore with the
local .NET SDK 11.0.100. The fixture was inspected without execution.

The shipped VS Code TextMate engine and bundled C# grammar provided lexical
colors. The editor's **Developer: Inspect Editor Tokens and Scopes** reported
semantic categories and effective foregrounds before and after the fix.

| Token (line:column) | TextMate scope | Lexical | Semantic type | Before | After |
| --- | --- | --- | --- | --- | --- |
| `public` (20:6) | `storage.modifier.public.cs` | `#CAA1DE` | `keyword` | `#CAA1DE` | `#CAA1DE` |
| `await` (22:10) | `keyword.operator.expression.await.cs` | `#D7829B` | `controlKeyword` | `#CAA1DE` | `#D7829B` |
| `if` (23:10) | `keyword.control.conditional.if.cs` | `#CAA1DE` | `controlKeyword` | `#CAA1DE` | `#D7829B` |
| `throw` (25:14) | `keyword.control.flow.throw.cs` | `#D7829B` | `controlKeyword` | `#CAA1DE` | `#D7829B` |
| `for` (28:10) | `keyword.control.loop.for.cs` | `#CAA1DE` | `controlKeyword` | `#CAA1DE` | `#D7829B` |
| `return` (32:10) | `keyword.control.flow.return.cs` | `#D7829B` | `controlKeyword` | `#CAA1DE` | `#D7829B` |

Before the change, the provider's semantic fallback `keyword.control.cs`
matched the generic keyword color. Afterward, the inspector reported
`controlKeyword:csharp` as the applied theme rule. The selector also covers
other tokens this provider classifies as `controlKeyword` in C#.

At 20:24, the primitive alias `string` remained semantic `keyword` with a
lilac foreground and a sand lexical fallback. This agrees with the
[historical primitive-alias decision](../README.md). In a lexical-only
context, the generic keyword rule still colors `if` and `for` lilac.
Results cover this provider and fixture. Other project and provider contexts
remain pending.
