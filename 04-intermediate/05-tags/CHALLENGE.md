# Challenge

## Challenge 1: Semantic versioning with tags

Real projects use [Semantic Versioning](https://semver.org/): `MAJOR.MINOR.PATCH`.

Create a sequence of tags that follows semver:

```bash
git tag -a v1.0.0 -m "Initial release"
# make a small bug fix commit
git tag -a v1.0.1 -m "Fix health check timeout"
# make a feature commit
git tag -a v1.1.0 -m "Add metrics endpoint"
```

List them: `git tag -l "v1.*"`. Now sort by version (not alphabetically):

```bash
git tag -l --sort=version:refname "v*"
```

What order do they appear in?

---

## Challenge 2: GitHub Release

Tags on GitHub can become full releases with changelogs and downloadable assets.

1. Push your tags: `git push origin --tags`
2. On GitHub: go to your repo → Tags → click on a tag → "Create release from tag"
3. Write release notes, set as "latest release"
4. Observe the GitHub release page

This is how npm packages, Helm charts, and Go modules signal new versions.

---

## Challenge 3: Tag in a GitHub Actions workflow

Write a workflow file that runs only when a tag is pushed:

```yaml
# .github/workflows/release.yml
on:
  push:
    tags:
      - 'v*'
```

This trigger fires when you push any tag starting with `v`. This is the standard CI/CD pattern for release pipelines. Save the file (don't worry about the full workflow body yet — that's module 07). What kind of automation makes sense in a release workflow?

---

## Bonus: GPG-signed tags

```bash
git tag -s v2.0 -m "Signed release"
```

This requires a GPG key configured. Signed tags prove the tag was created by someone with access to that private key. Used in security-sensitive projects. Research how to verify a signed tag: `git tag -v v2.0`.
