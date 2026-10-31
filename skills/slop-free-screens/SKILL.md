---
name: slop-free-screens
description: Design, redesign or check a product screen (dashboard, list, form, detail page, settings) so it fits its user and doesn't look or behave AI-made. Use when the user asks to build or fix a screen, pastes a screenshot and asks to "remove the slop", says "check this screen", or wants a review only. It sets the job first, applies a list of slop signs with fixes, keeps every widget and fixes what's inside it, tries worst-case data in a real browser, and ends with a visual report and new team rules saved to team-rules.md. Works in Claude Code, Codex, Cursor and other coding tools. In Figma Make or a chat tool it runs the same steps with a chat report. Landing, sign-up and checkout pages are secondary; the list covers only their worst signs.
---

# Slop-free screens

Makes an AI-made product screen fit one person doing one job, instead of the average screen.
Five steps. One report that grows across the run.

## Before anything

1. **Read `team-rules.md`** at the project root, if it exists.
   - Its rules win over the slop list. When they clash, follow the team rule and say so in the report.
   - Skip everything under its "Accepted on purpose". Don't flag those again.
2. **Start the report.**
   - If you can write files: copy `reference/report-template-marked.html` next to the screen, as `slop-report.html`.
   - If you can't: use `reference/report-template.md` in chat.
   - Fill `screen`, `date` and `tool` now. Each step fills its own keys after that.

## The five steps

| Step | File | What it does |
|---|---|---|
| 1 Set the job | `steps/1-set-the-job.md` | Who it's for, the job and the moment, asked once |
| 2 Set the rules | `steps/2-set-the-rules.md` | The signs that fit, colours with jobs, real-looking data |
| 3 Pick and check | `steps/3-pick-and-check.md` | New screen: 2–3 sketches, the user picks. Existing screen: a check of every widget |
| 4 Cut and break | `steps/4-cut-and-break.md` | Fix inside each widget, try worst cases in a browser, fill the report |
| 5 Make it a rule | `steps/5-make-it-a-rule.md` | Save only the new rules to `team-rules.md` |

Open only the step files the request needs.

## Route the request

| The user… | Open | Notes |
|---|---|---|
| asks for a new screen | 1 → 2 → 3 → 4 → 5 | |
| pastes a screenshot and asks to remove the slop | 1 → 2 → 3 → 4 → 5 | Step 1 asks, with guesses read from the screenshot. Step 2 uses any reference screens they gave. Step 4 rebuilds it as a page before fixing. |
| already answered the model's own questions | 1 → 2 → 3 → 4 → 5 | Step 1 reuses those answers and asks nothing new. |
| is building in a code project | 1 → 2 → 3 → 4 → 5 | Work on the real files. Skip questions the conversation or `team-rules.md` already answers. |
| says "check this screen" | 4 → 5 | If no job is known yet, ask step 1's questions first. |
| wants a review only | the slop-reviewer agent (`agents/slop-reviewer.md`) | If no job is known yet, ask step 1's questions first. Change nothing. Report the signs. |
| asks to break a rule ("make it pop", "add a gradient") | Do what they asked | Step 5 records it under "Accepted on purpose", so it isn't flagged again. |
| wants a whole app cleaned | 1 and 2 once, then 3 → 4 → 5 per screen | One screen per run, worst screen first. Ask which is worst if it isn't clear. |
| moves on to another screen for the same team | 2 → 3 → 4 → 5 | Run step 1 again only if the user or the job changes. Add only new rules. |

## Fast mode

Use it only when the user says so: "just build it", "don't ask me", "use your own judgment".
Otherwise ask, even without a question tool: write the questions in your reply and stop. The user answers in their next message.
- Step 1: use your guesses and mark each one "(assumed)" in the `for` line.
- Step 3: pick the direction yourself and show a table: choice → reference → reason.
- Everything else runs as normal.

## Tools without files or a browser

Figma Make, ChatGPT, Gemini and similar: run the same steps.
- Write the report in chat with `reference/report-template.md`.
- Break cases you couldn't run in a browser are "Not tried", never "Holds".
- Print the new rules for the user to paste into `team-rules.md`, or into the tool's own guidelines.
- For the review, open a fresh chat as `agents/slop-reviewer.md` describes.

## Always

- **Keep every widget.** Fix what's inside it. Remove one only when it has no job, and say why.
- **Name every number you remove or swap**, and why.
- **Never call a case "Holds"** unless you tried it in a browser.
- **Never list rules the slop list already holds.** Cite their ids.

## Reference files

- `reference/slop-list.md`: the slop signs, each with an id (L, W, D, B), a level and a fix.
- `reference/break-list.md`: worst-case data and states to try.
- `reference/report-template-marked.html`: the report. `reference/report-template.md`: the chat version.
- `reference/team-rules.example.md`: copy it to `team-rules.md` and make it yours.
