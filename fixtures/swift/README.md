# Swift type-role fixture

`TypeRoles.swift` is an original, dependency-free library fixture for the VS Code
Swift classification review. It has no entry point and is not intended to be
executed. It covers built-in type annotations and initializers, optional and
generic forms, an alias, protocol existentials and opaque returns, properties,
methods, and declaration and control-flow keywords.

For the review, create a disposable SwiftPM library at an already trusted
workspace location, here `/tmp/sr-web-context/javascript/swift-review`, with
this `Package.swift`:

```swift
// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "SwiftReview",
    products: [.library(name: "Review", targets: ["Review"])],
    targets: [.target(name: "Review")]
)
```

Copy `TypeRoles.swift` unchanged to `Sources/Review/TypeRoles.swift` under that
project and open the project folder in VS Code. The project has no executable,
tests, or package dependencies. With Apple Swift 6.4 and the Command Line Tools
SDK on the review machine, this offline typecheck succeeded without executing
the fixture:

```sh
/Library/Developer/CommandLineTools/usr/bin/swiftc \
  -sdk /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk \
  -typecheck -module-cache-path /tmp/sr-swift-review-module-cache \
  fixtures/swift/TypeRoles.swift
```

The explicit SDK was needed on that machine; the default invocation could not
load the standard library. The module cache remains outside the repository.
See the [native review](../../previews/vscode/swift/README.md) for observed editor
classifications and limitations.
