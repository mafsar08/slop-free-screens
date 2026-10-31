# Team rules

Copy this file into your project as `team-rules.md`, then replace the example lines with your own.
The skill reads it before it designs or checks anything. Step 5 saves the new rules from each run here, so nobody copies and pastes.
Your rules win over the slop list. When they clash, the skill follows yours and says so in the report.

**Make each tool read it.** Add one line to the file your tool already reads:

| Tool | File | Line to add |
|---|---|---|
| Claude Code | `CLAUDE.md` | `@team-rules.md` |
| Codex, Cursor, Copilot | `AGENTS.md` | `Before designing or changing a screen, read team-rules.md.` |
| Figma Make | Guidelines.md | Paste this file's rules in. Figma Make can't read project files. |
| ChatGPT, Gemini | Project instructions | Paste this file's rules in. |

The example below is for an interview-practice app.

## Product and users

- **Product:** a web app where job seekers practise mock interviews and track their scores.
- **Main user:** a designer in the middle of a job search, on a laptop, most evenings after work.
- **Not for:** recruiters, employers or investors.
- **Devices:** laptop first. Phones aren't in scope yet.
- **Locale:** India. Use ₹, DD MMM (12 Oct), +91 and 12-hour time (11:00 am).

## Look

- **Page:** white background, near-black text.
- **Colours and their jobs:**
  - Blue `#1D5BD6`: the next thing to do. At most one button per screen.
  - Green and red: a score going up or down. Nothing else.
  - Everything else is grey.
- **Type:** one body size (15 px) and one heading size (20 px). Body text in regular weight.
- **Spacing:** a 4 px scale.
- **Reuse these parts:** the score table, the number card and the button styles from the design system.
- **References to follow:** Codecademy's progress page (bars in one colour with a clear scale) and Coursera's week view (numbers compared with your own last week).

## Words

- Say "mock interview" or "mock", never "session" or "assessment".
- Buttons name the action: "Practise this", "Start practice".
- No subtitles under headings.

## Data

- Scores are percentages with no decimals.
- Only compare with the user's own past mocks.
- Sample data uses Indian names and companies, with at least one very long name.

## Accepted on purpose

These look like slop, but are right for us. The skill doesn't flag them again.

| What | Why | Since |
|---|---|---|
| The latest score shows in the card and in the table's top row | Users read the card first and the table later | 30 Oct 2026 |

## Rules learned

Step 5 adds a line here after each run. Each rule follows the pattern "Don't … Do …".

| Date | Screen | Rule |
|---|---|---|
| 30 Oct 2026 | Dashboard | Number cards: don't show numbers nobody acts on, like hours practised. Do show the last score and the change since the mock before. |
| 30 Oct 2026 | Dashboard | Chart: don't add made-up goal lines. Do show their own scores, with the latest one labelled. |
| 30 Oct 2026 | Dashboard | Don't hard-code counts like "See all 12". Do count from the data. |
