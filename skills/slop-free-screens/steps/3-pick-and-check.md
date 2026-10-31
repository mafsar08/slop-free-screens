# Step 3 · Pick and check

Choose before building, then check the choice against the rules.
A new screen gets options and the user picks one. An existing screen gets every widget checked.

## A new screen

### 1. Draft 2–3 directions

Make them genuinely different: different layouts and a different first thing the eye lands on. Not three colour variants of one layout.
For each direction, give:
- a rough ASCII sketch of the screen's regions and its main action;
- the idea, in one line;
- what it gives up, in one line.

```
A · Next practice first
┌────────────────────────────────────┐
│ Practise problem solving   [Start] │
│ ┌──────┐┌──────┐┌──────┐           │
│ │ last ││change││ done │           │
│ └──────┘└──────┘└──────┘           │
│ chart            │ category bars   │
│ past mocks table                   │
└────────────────────────────────────┘
Idea: tonight's practice is the first thing they see.
Gives up: the overall score sits lower down.
```

### 2. The user picks

Ask which direction to build. Wait for the answer.
They may mix two directions ("A, with B's table"). Take the mix as the pick.

**Fast mode:** pick yourself, and show why in a table:

| Choice | Reference | Reason |
|---|---|---|
| Next practice first | the job from step 1 | the job is "practise next", so it goes first |
| One accent colour | team-rules.md, Look | blue means "the next thing to do" |

### 3. Write a short plan

- Colours, each with its job.
- Type: the sizes you set in step 2.
- Layout: the regions, in order.
- Every widget with its job, in one line each.

### 4. Check the plan before building

- Run every **Must** sign in `../reference/slop-list.md` against the plan.
- Check every widget's job against the job from step 1. A widget with no job doesn't go in.
- Check every number against "Not for". No comparisons with other people, no made-up targets.
- Fix the plan, then build.

## An existing screen or a screenshot

Check every widget. Don't redesign yet.
List each widget on the screen with:
- **its job**, in one line, tied to the job from step 1;
- **the slop inside it**, as sign ids with a short note, for example "L3 every bar a different colour";
- **every number it shows**, and whether the user acts on it at this moment (D1);
- **the call**: keep and fix, or remove. Remove a widget only when it has no job, and say why (B19).

Also note what's missing for the job, for example the main action buried 2,000 px down (B10).

If a number's job depends on the moment, such as a count of mocks done, keep it or ask. Don't drop it quietly (D14).

## Report: fill these keys

- `picked`: new screen only. One line, 15 words or fewer: the direction and why. In fast mode start with "Picked by AI".
- `steps.pick`: "done".
- Keep the widget list for step 4. It becomes the report's `widgets`.

Next: `steps/4-cut-and-break.md`.
