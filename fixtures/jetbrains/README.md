# JetBrains review fixtures

These fixtures provide project context for native editor review without adding
dependencies. From the repository root, create disposable copies and compile
them with the .NET 8 targeting pack and a JDK:

```sh
mkdir -p /tmp/sr-jb-review/projects/rider/jetbrains /tmp/sr-jb-review/projects/idea/preview /tmp/sr-jb-review/classes
cp fixtures/showcase.cs /tmp/sr-jb-review/projects/rider/showcase.cs
cp fixtures/jetbrains/Review.csproj /tmp/sr-jb-review/projects/rider/jetbrains/Review.csproj
cp fixtures/LabelRenderer.java /tmp/sr-jb-review/projects/idea/preview/LabelRenderer.java
printf '{"sdk":{"version":"8.0.419"}}\n' > /tmp/sr-jb-review/projects/rider/global.json
(cd /tmp/sr-jb-review/projects/rider && dotnet build jetbrains/Review.csproj --ignore-failed-sources -p:NuGetAudit=false)
javac -d /tmp/sr-jb-review/classes /tmp/sr-jb-review/projects/idea/preview/LabelRenderer.java
```

The temporary `global.json` selects the installed .NET 8.0.419 SDK; substitute
another installed .NET 8 SDK version if needed. The Java fixture was compiled
with the JDK bundled with IntelliJ IDEA.

Open `projects/rider/jetbrains/Review.csproj` in Rider and `projects/idea` in
IntelliJ IDEA under `/tmp/sr-jb-review`. The Java source uses package `preview`;
the C# project links the sibling `showcase.cs`. Neither fixture needs to run.

For the focused Rider C# builtin type review, create a separate disposable
project under the same trusted root. Select an installed .NET 8 SDK; the local
review used `8.0.418` from `~/.dotnet`:

```sh
mkdir -p /tmp/sr-jb-review/projects/rider/builtins/jetbrains
cp fixtures/jetbrains/BuiltinTypes.cs /tmp/sr-jb-review/projects/rider/builtins/BuiltinTypes.cs
sed 's/showcase.cs/BuiltinTypes.cs/g' fixtures/jetbrains/Review.csproj > /tmp/sr-jb-review/projects/rider/builtins/jetbrains/Builtins.csproj
printf '{"sdk":{"version":"8.0.418"}}\n' > /tmp/sr-jb-review/projects/rider/builtins/global.json
(cd /tmp/sr-jb-review/projects/rider/builtins && ~/.dotnet/dotnet build jetbrains/Builtins.csproj --ignore-failed-sources -p:NuGetAudit=false)
```

Open `builtins/jetbrains/Builtins.csproj` in Rider and verify successful loading.
The project links the sibling fixture; compilation is optional, and the fixture
must not be run.

For the focused Java primitive review, reuse the existing IDEA project and its
`preview` source folder. Copy the fixture and optionally compile it offline with
IntelliJ IDEA’s bundled JDK (adjust the application path if needed):

```sh
mkdir -p /tmp/sr-jb-review/projects/idea/preview /tmp/sr-jb-review/classes
cp fixtures/jetbrains/PrimitiveTypes.java /tmp/sr-jb-review/projects/idea/preview/PrimitiveTypes.java
"/Applications/IntelliJ IDEA.app/Contents/jbr/Contents/Home/bin/javac" -d /tmp/sr-jb-review/classes /tmp/sr-jb-review/projects/idea/preview/PrimitiveTypes.java
```

Open `projects/idea` in IntelliJ IDEA, confirm its SDK, source root and language
level, and allow indexing to finish before reviewing. The local compiler reports
`javac 25.0.4.1`. Compilation is optional; do not execute the fixture. See the
[review notes](../../previews/jetbrains/java-primitives/README.md) for source
evidence and the bounded native review.
