# Step 2 · Set the rules

Decide the rules before drawing. Every choice nobody makes falls back to the model's default, and defaults are what make a screen look AI-made.

## 1. Read the team's rules

- Read `team-rules.md` at the project root. Follow its Look, Words and Data sections. They win over the slop list.
- Note its "Accepted on purpose" items. Don't flag them.
- Use only the references it names. Don't search the web for new ones.
- No `team-rules.md` yet? Carry on with the defaults below. Step 5 creates the file.

## Reference screens from the user

If the user gives reference screenshots, open every one.
- Take the ideas the user names. If they name none, say in one line each which idea you'll take and why it fits the job.
- Take patterns: layout, order, how data is shown. Don't copy their colours, logos, fonts or wording.
- Where a reference clashes with a Must sign or a team rule, the sign or rule wins. Say so.
- Cite them in step 3's choice → reference → reason table.

## 2. Pick the signs that fit this screen

Open `../reference/slop-list.md`. Every **Must** sign applies to every screen.
Then read these closely for the kind of screen:

| Screen | Read closely |
|---|---|
| Dashboard | L1 L3 L6 L14 · W8 W10 · D1 D2 D3 D4 D5 D8 D14 · B10 B11 B16 |
| List or table | L12 L17 L18 · W9 · D11 D12 · B2 B5 B11 B16 B17 |
| Form or settings | L15 · W2 W5 W6 · B1 B7 B8 B18 |
| Detail page | L19 L20 · W9 W10 · D6 · B6 B13 |
| A flow across screens | L10 · W13 · B14 B15 |
| Wall or counter screen, read from far away | L15 L16 · B11 B12 |

Read the "Not slop on its own" section too, so you don't flag what's fine.

## 3. Give each colour a job

Use the team's colours if `team-rules.md` has them. Otherwise:
- **One strong colour** for the next thing to do. At most one main button per screen.
- **Status colours** (green, red, amber) only where they show a status, and never two meanings for one colour.
- **Everything else is grey.**
- Write the colours down with their jobs, for example "blue = the next thing to do".

## 4. Set type and spacing

- One body size and one heading size, plus a size for big numbers if the screen has them.
- Size text for where it's read: a laptop, a phone, a wall 2 m away.
- One spacing scale, such as 4 px steps.

## 5. Set the words

- Use the product's own words for things. Write them down if they aren't in `team-rules.md`.
- Buttons name the action ("Start practice"), not the system ("Submit").
- No subtitles that repeat the heading. No helper lines under controls.

## 6. Set the data

Sample data is part of the design. Make it look like the real users' data:
- **Names and companies** from the users' world, including at least one very long name.
- **Local formats** from `team-rules.md`, or from the users' country: currency, dates, phone numbers, time.
- **Dates around the moment** from step 1. If the interview is tomorrow, the past mocks are from this month.
- **Numbers worked out from the rows**: every change, average, total and count.
- **Not too neat:** uneven values, a missing value or two shown as "—".

## Keep the rules

Keep the picked signs, colour jobs, type, words and data rules for steps 3 and 4.

## Report: fill these keys

- `steps.rules`: "done".

Next: `steps/3-pick-and-check.md`.
