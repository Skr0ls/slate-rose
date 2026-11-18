# Design

Dispatch from main with an existing tag and a dry-run flag enabled by default. Resolve the tag to a commit reachable from main and find a successful Quality push run from main for that exact commit. Check the downloadable bundle contains the three expected files. The verification job uses read permissions. An explicit write job creates a draft with the verified files and existing tag. It fails on an existing release instead of replacing it.
