# Step 5 · Make it a rule

Turn what this run learned into rules, so the next screen starts where this one ended.
Save them where every tool reads them: `team-rules.md`.

## 1. Find the new rules

Go through this run's fixes and break results. A new rule is something this team wants that the lists don't already say.
- **Already in `../reference/slop-list.md` or `team-rules.md`?** Not new. Cite its id in the report and move on.
- **New:** write it as "Don't … Do …", one line, about one widget or one kind of data.
  Example: "Past interviews table: don't use a card per mock. Do use columns: company and role, date, score, change, one thing to fix."
- Keep only rules that would change the next screen. Two good rules beat ten.

## 2. Record the overrides

When the user asked for something the slop list calls slop ("make it pop", "keep the gradient"), it's their call.
Add a row to "Accepted on purpose", so the next run doesn't flag it again:

| What | Why | Since |
|---|---|---|
| Gradient on the hero card | The brand asked for it | 30 Oct 2026 |

Write their reason. If they didn't give one, write "user asked".

## 3. Save to team-rules.md

**The file exists:**
- add each new rule as a row in "Rules learned": date, screen, rule;
- add each override to "Accepted on purpose";
- don't rewrite or reorder the team's own lines.

**There's no file yet:**
- create `team-rules.md` at the project root, using the headings of `../reference/team-rules.example.md`;
- fill "Product and users" from step 1's answers;
- fill "Look", "Words" and "Data" from step 2;
- add the new rules and overrides;
- don't copy the example's own content.

**Make every tool read it.**
Check that the project's `CLAUDE.md` or `AGENTS.md` points to `team-rules.md`. If not, tell the user the one line to add (the example file has the table).
Don't edit those files unless the user says yes.

**The tool can't write files** (Figma Make, ChatGPT):
- print the new rules and overrides as rows, ready to paste;
- say where they go: `team-rules.md`, or the tool's guidelines (Figma Make's Guidelines.md, ChatGPT's project instructions).

## Report: fill these keys

- `rules_added[]`: the new rules, as written. Only new ones.
- `rules_file`: "team-rules.md".
- `rules_saved`: `true` if you wrote them to the file, `false` if you printed them. The report shows a Copy button when it's false.
- `rules_created`: `true` if you created `team-rules.md` in this run. Tell the user you created it.
- `steps.rule`: "done".

Next: hand the report to the user.
- Give its path, or paste the chat version.
- Then add one line: the verdict, plus anything still there or broken.
