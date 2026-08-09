# Challenge

## Challenge 1: Simulate the "stop the line"

1. Commit a syntax error to `main`:

```bash
echo "def broken(:" >> app.py
git add app.py
git commit -m "feat: new function (broken)"
```

2. In TBD culture, everyone on the team would stop committing. You'd immediately fix it:

```bash
vi app.py     # remove the broken line
git add app.py
git commit -m "fix: remove syntax error from broken function"
```

What's the time between the bad commit and the fix? That's the "blast radius" of breaking trunk. In TBD, this is measured and minimised.

---

## Challenge 2: Feature flag toggling script

Write a small shell script that lets you flip a flag:

```bash
#!/bin/bash
# toggle-flag.sh <flag_name> <true|false>
FLAG=$1
VALUE=$2
sed -i "s/\"$FLAG\": .*/\"$FLAG\": $VALUE,/" feature_flags.py
git add feature_flags.py
git commit -m "feat(flag): set $FLAG=$VALUE"
```

Use it:
```bash
bash toggle-flag.sh new_metrics_endpoint true
bash toggle-flag.sh enhanced_logging false
```

This simulates an automated flag management system.

---

## Challenge 3: Compare deploy frequencies

Research the DORA (DevOps Research and Assessment) metrics:
- Deployment frequency
- Lead time for changes
- Change failure rate
- Time to restore

How does TBD relate to each metric vs Gitflow? The Accelerate book measured that high-performing teams deploy to production on-demand (multiple times/day). What workflow makes that possible?

---

## Bonus: Strangler Fig pattern

Research the "Strangler Fig" pattern for gradually replacing legacy systems. How does it connect to TBD's "branch by abstraction" concept? Draw a diagram showing how you'd migrate a legacy login system to a new one using TBD + feature flags without a big-bang cutover.
