# slop-free-screens

Makes AI-made product screens fit the person using them, not the average screen every AI draws.

For dashboards, lists, forms and settings. Works in Claude Code, Codex and Cursor.

## How it works

1. **Set the job.** Asks who it's for, the job and the moment. Fills in guesses from your screenshot.
2. **Set the rules.** Picks the slop signs that matter for this screen.
3. **Pick and check.** New screen: 2–3 sketches, you pick one. Existing screen: checks every widget.
4. **Cut and break.** Fixes what's inside each widget, then tries worst cases (empty, long names, phone) in a real browser.
5. **Make it a rule.** Saves what it learned to `team-rules.md`, so the next run starts from there.

You get `slop-report.html`: the verdict, before and after, every fix tied to its rule, and every test with a screenshot.

## Install

**Claude Code:** copy `skills/slop-free-screens` into your project's `.claude/skills/` folder, or into `~/.claude/skills/` for every project.

**Codex, Cursor, Copilot:** copy the folder into your project and add this line to `AGENTS.md`:
`For screen design work, follow skills/slop-free-screens/SKILL.md.`

## Use it

- "Here's my screen (screen.png). Use slop-free-screens to remove the slop."
- "Here's my screen and a screen I like (ref.png). Use slop-free-screens."
- "Check this screen." Fixes and tests an existing page.
- "Review this screen only." Lists the slop and changes nothing.

Say "just build it" to skip the questions.

## Team rules

Each run saves new rules to `team-rules.md` in your project. Add `@team-rules.md` to `CLAUDE.md` (Claude Code), or a line to `AGENTS.md`, so every session reads it. Choices you make on purpose, like "make it pop", are remembered and not flagged again.

## Good to know

- Tested with Claude Opus 5.5 on two screens. Other models not yet.
- Needs a browser for real tests. Without one, tests are marked "Not tried".
- A full run takes about 15–25 minutes.

Built on ideas from 10 open skills: see [CREDITS.md](CREDITS.md). MIT licence.
