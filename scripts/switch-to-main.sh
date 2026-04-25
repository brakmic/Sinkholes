#!/usr/bin/env sh
# Switch a clone made before the master -> main rename over to main.
# Safe to run more than once.
set -e

# Rename the local branch only if it still exists as 'master'.
if git show-ref --verify --quiet refs/heads/master; then
    git branch -m master main
fi

git fetch origin
git branch -u origin/main main
git remote set-head origin -a
git remote prune origin

echo "Done. Local branch is now 'main' and tracks 'origin/main'."
