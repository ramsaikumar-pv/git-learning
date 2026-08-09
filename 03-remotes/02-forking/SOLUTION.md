# Solution

## `git remote -v` after adding upstream
```
origin    git@github.com:ramsaikumar-pv/Hello-World.git (fetch)
origin    git@github.com:ramsaikumar-pv/Hello-World.git (push)
upstream  git@github.com:octocat/Hello-World.git (fetch)
upstream  git@github.com:octocat/Hello-World.git (push)
```

`origin` = your fork. `upstream` = the original. This naming convention is universal.

## `git fetch upstream`
```
From github.com:octocat/Hello-World
 * [new branch]      main       -> upstream/main
```

Git downloaded the branches from upstream and stored them as `upstream/main`, `upstream/feature-xyz`, etc. Your local branches are untouched.

## `git log --oneline HEAD..upstream/main`
```
a4f3e1c Add contributing guide
b2d9f8a Update README
```

These are commits that exist on `upstream/main` but not in your local `HEAD`. Your fork is 2 commits behind.

## `git merge upstream/main`
```
Updating d7c2a19..a4f3e1c
Fast-forward
 CONTRIBUTING.md | 15 +++++++++++++++
 README.md       | 3 ++-
```

Fast-forward (no divergence). Your main moves forward to upstream's tip.

## On GitHub after `git push origin main`

GitHub shows: "This branch is up to date with octocat/Hello-World:main ✓"

## Why forking exists

You don't have write access to the original. Your fork gives you a place to push branches and open pull requests. The original maintainers review and merge your PR into their repo. You never push directly to upstream — you can't, you don't have permission. The fork is your staging area for contributions.
