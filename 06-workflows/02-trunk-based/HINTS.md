# Hints

<details>
<summary>Hint 1 — How does TBD handle code review if branches are so short-lived?</summary>

Two approaches:

1. **Pre-commit pair review**: developer pairs review code as it's written, then commit directly. Common at Google.

2. **Short-lived PR**: open a PR from a short-lived branch. Use CI automation to run fast (< 5 min). Reviewer approves quickly. Merge same day. The key is keeping the PR scope small enough to review in 30 minutes.

The anti-pattern TBD avoids: the "big PR" with 500 changed lines that lives for 2 weeks, accumulates conflicts, and takes 3 days to review. Small is fast.

</details>

<details>
<summary>Hint 2 — What if a feature takes weeks to build — how does TBD handle that?</summary>

Three strategies:

1. **Feature flags**: commit small pieces of unfinished code to `main` behind a flag. The flag hides it from users until complete.

2. **Branch by abstraction**: refactor existing code to call an abstraction layer, replace the implementation incrementally.

3. **Dark launching**: the feature runs in the background but output is not shown to users until ready. Used by Facebook/Google to test performance before release.

The mental model shift: in TBD, "code is in main" doesn't mean "feature is live." Flags decouple them.

</details>

<details>
<summary>Hint 3 — My CI is broken — can I still commit to main in TBD?</summary>

Conventionally: **no**. In strict TBD culture, a red CI means the whole team stops and fixes it before anyone else commits to `main`. This is called "stop the line" (from manufacturing). Broken `main` = broken development velocity for everyone.

In practice at smaller teams: you might commit anyway but flag it clearly ("chore: this breaks CI, fixing next commit") and fix it immediately in the next commit.

The key principle: `main` should ALWAYS be deployable. If CI is broken, `main` is not deployable. Fix it first.

</details>
