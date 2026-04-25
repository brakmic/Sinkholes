# Switch a clone made before the master -> main rename over to main.
# Safe to run more than once.
$ErrorActionPreference = 'Stop'

if (git show-ref --verify --quiet refs/heads/master) {
    git branch -m master main
}

git fetch origin
git branch -u origin/main main
git remote set-head origin -a
git remote prune origin

Write-Host "Done. Local branch is now 'main' and tracks 'origin/main'."
