# Design

Use a standalone Rust 2021 library fixture covering a struct and fields, a trait, lifetimes, a local macro, primitive types, and control words. Check formatting and emit only compiler metadata. Replay bounded lexical categories and inspect native colors in a dependency-free temporary Cargo project with rust-analyzer active. Keep the approved palette and use precise Rust selectors when the observed categories distinguish roles.

Use Rust-only `builtinType` and `keyword.controlFlow` semantic selectors for primitives and flow. Apply the primitive role to the observed Rust TextMate primitive and numeric type scopes. The bundled control scope also contains the `for` in an impl declaration, so retain the existing lexical fallback for that scope.
