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
