# Step 4 · Cut and break

Fix the slop inside each widget, then try to break the screen with worst-case data in a real browser.
Fill the report as you go.

## 1. Get a page to work on

- **Code project:** work on the real files.
- **A screenshot only:** rebuild it as one HTML page first, keeping every widget, its content and its wiring. Then fix that page. The break tests run on it.
- **Keep the screen's real data:** its names, scores and dates. Don't swap them for new numbers. If they don't add up, work the derived numbers out again from them (D3), or ask. Made-up rows belong only behind the test switches.
- **Long browser tests:** wait for them to finish before you end your reply. Don't leave one running in the background.
- **Before you change anything:** take a full-page screenshot of the before. If the before is the user's screenshot, use it as it is.

## 2. Fix inside each widget

Work through the widget list from step 3. If step 3 didn't run ("check this screen"), list every widget and its job first.
- **Keep the widget and fix what's inside it.** Cards stay cards, the chart stays a chart (B19).
- **Remove a widget only when it has no job.** Write down why, in 10 words or fewer.
- **Name every number you remove or swap**, with its reason tied to the job (D14).
  Example: "Hours practised → last score: nobody acts on hours tonight."
  When the reason depends on the moment, keep the number or ask.
- **Fix the page-wide signs too:** colour families (L1), type (L7), repeats (W8).
- **Leave in place** anything `team-rules.md` lists under "Accepted on purpose".
- Can't fix something now? It goes in the report as "still there" (`left`), with the reason.

## 3. Add test switches

Let each case load from the address, so anyone can check it again:
`#empty`, `#one`, `#many` and `#long`, plus any case this screen needs.
Test data stays behind its switch and never shows by default.

## 4. Try to break it

Open `../reference/break-list.md`.
- **Always run:** empty, one item, many items, a very long name, every control clicked, keyboard only, contrast, numbers agree.
- **Then add the cases that fit this screen:** phone width, a search, a flow, a wall screen.
- **Use a real browser:** any browser tool you have. Load the case, look, click, then take a screenshot.
- **No browser?** Read the code and say what would happen. Mark it "not tried", **never "holds"** (B20).
- **Results:** holds, ugly or breaks. Fix what breaks, then try again.
- Close every browser you open before you finish.

## 5. Capture for the report

Use one browser width for the before and after screenshots, 1440 px if you can.
- **Full-page screenshots:** before and after.
- **Crops:** for each widget, `before_crop` and `after_crop`. A removed widget has only `before_crop`.
- **Boxes:** for each kept widget and each leftover, where it sits on the after screenshot, as `[x, y, w, h]` fractions of the page.
  Measure them in the browser: `getBoundingClientRect()` divided by the page's width and height.
- **Ring spots:** for each leftover, a crop with the problem circled in red.
- **Break shots:** one screenshot per case you tried.

No browser at all? Leave the boxes as `null`. The report then shows the notes as a plain list.

## 6. Review with fresh eyes

Run the slop-reviewer agent (`../agents/slop-reviewer.md`). Give it:
- the after screenshots, desktop and phone;
- the `for` line from step 1;
- the path to `../reference/slop-list.md`.

Fix every Must it finds, or add it to `left` with the reason.
No subagents in this tool? Do the review in a fresh chat, as the agent file describes.

## Report: fill these keys

- `verdict`: 10 words or fewer, the result a stranger should read first. If anything breaks, say so.
  Example: "Cleaner, but it breaks on a phone."
- `before.image`, `after.image`: the full-page screenshots.
- `widgets[]`: one per widget on the old screen. Each has:
  - `name`, `status` ("kept", "removed", or "" for a page-wide fix);
  - `box`, `before_crop`, `after_crop`, `note` (6 words or fewer, such as "4 → 3"), and `why` (removed widgets only);
  - `fixes[]`: each with `found` and `replaced` (6 words or fewer each) and `rule` (a sign id).
- `left[]`: slop still there, each with `what`, `rule`, `note` (why it stays), `image` (the ringed crop) and `box`.
- `breaks[]`: each with `case`, `result` (holds, ugly, breaks or not tried), `note` (6 words or fewer) and `image`.
- `team_rules[]`: `{id, text}` for any `team-rules.md` rule a fix cites.
- `steps.cut`: "done".

Captions only. The rules live in the lists, so cite their ids. Don't repeat their text.

Next: `steps/5-make-it-a-rule.md`.
