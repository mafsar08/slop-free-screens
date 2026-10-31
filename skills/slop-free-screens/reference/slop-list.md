# Slop list: product screens

Signs that an AI-made product screen (dashboard, list, form, detail page, settings) is slop, and what to do instead.

**Fix the slop, keep the widget.** A dashboard keeps its cards, chart, bars and table. Fix what's inside each one.
Remove a widget only if it has no job for this user, and say which one and why.

**Levels**
- **Must**: it misleads, breaks the job or breaks the screen. Fix before anyone sees it.
- **Should**: people spot it as AI-made at a glance. Fix it, or write down why it stays.
- **Could**: polish. Fix it if there's time.

**How to check**
- **Eye**: look at the screenshot.
- **Count**: count something on the page (colours, sizes, repeats).
- **Use**: click, type or resize in a real browser.

Each sign has an id (L1, W2, D3, B4) for the report.

## Look

- **L1 · Should · Count** **Decoration colour.** Three or more colour families that mean nothing. We have counted 8 and 9 on one screen.
  **Fix:** one strong colour for the next thing to do, and status colours only where they show a status. Make the rest grey.
- **L2 · Must · Eye** **One colour, two meanings**, for example a source tag in the same red as "Late by 4 min".
  **Fix:** give each colour one meaning, and give the other meaning its own colour or an icon.
- **L3 · Should · Eye** **A colour per item**: every bar, category, tag or avatar gets its own colour.
  **Fix:** keep the bars and tags in one quiet colour. Highlight only the one that needs action.
- **L4 · Should · Eye** **Gradients, glows, glass or blur** on cards, charts or buttons.
  **Fix:** keep the element and give it a flat fill.
- **L5 · Should · Eye** **The default AI look**: a purple or indigo accent, cream with a serif and orange, or near-black with neon green.
  **Fix:** keep an accent, but take it from the product's brand or from your references.
- **L6 · Should · Eye** **Everything in a box**: every block is its own floating card, or a card sits inside a card.
  **Fix:** keep every widget. Box the page regions, not each row, and put rows into one table or list.
- **L7 · Should · Count** **Flat type**: many sizes that are nearly the same, and almost everything semibold.
  **Fix:** one body size and one heading size, with regular weight for body text.
- **L8 · Could · Count** **Random spacing**, such as 5, 7, 9, 11 and 13 px.
  **Fix:** snap all spacing to a 4 or 8 px scale.
- **L9 · Should · Count** **One part drawn many ways**, for example a status dot in 6 forms or 3 shadow styles on one screen.
  **Fix:** pick one form and reuse it.
- **L10 · Must · Use** **The frame changes between screens**: the header, nav or buttons differ from one screen to the next.
  **Fix:** copy the first screen's frame exactly onto every screen.
- **L11 · Could · Eye** **Bare rows, or emoji as icons.**
  **Fix:** a face for a person, and an icon for a type, all from one icon set.
- **L12 · Should · Count** **A pill on every row.** We have seen about 19 on one page.
  **Fix:** keep the information in one status form (a dot and a word). Use a badge only for what needs attention.
- **L13 · Should · Count** **AI marks everywhere**, such as sparkle icons and "AI-powered" badges.
  **Fix:** keep the AI feature. Mark AI once, where it acted.
- **L14 · Should · Eye** **Ornaments instead of numbers**, such as a score ring or a decorative mini chart.
  **Fix:** keep the number. Show it plainly, or as a chart that compares something real.
- **L15 · Must · Eye** **Text too small for where it's read**, such as 11 px on a laptop, or a wall screen read from 2 m away.
  **Fix:** size the text for the device and the reading distance.
- **L16 · Must · Count** **Low contrast**: text under 4.5:1 against what's behind it (3:1 for large text), including white text on a coloured button or badge.
  **Fix:** darken it until it passes. Measure against the real background, not the page colour.
- **L17 · Should · Use** **Short values wrap or break mid-word**, such as "Volun-teer", or a time split across two lines.
  **Fix:** let only names wrap. Keep times, sizes and statuses on one line.
- **L18 · Must · Use** **Things overlap or get cut off.**
  **Fix:** give them room, or shrink the text to fit.
- **L19 · Could · Eye** **Big empty areas** in a panel or detail page.
  **Fix:** fill it with what the job needs, or size it to its content.
- **L20 · Should · Use** **Widgets shrink and leave holes** when there's little data.
  **Fix:** give each widget a minimum height so the grid holds.

These are slop on landing pages only, not on product screens: a centred purple-to-blue hero, emoji section markers, cards with a coloured side stripe, three identical feature cards, "1, 2, 3" step rows, a stat banner, and a badge above the headline.

## Words

- **W1 · Should · Eye** **A subtitle that repeats the heading**, for example "Payroll · Your payroll at a glance".
  **Fix:** keep the heading. Drop the subtitle, or swap in the one fact the user needs.
- **W2 · Should · Eye** **Helper lines under controls**, such as "Say a few words" or "Find a quiet spot".
  **Fix:** let the label and the state say it. Explain only an abnormal state.
- **W3 · Must · Eye** **The AI's own notes left on screen**, such as "This panel shows your…", or planning notes.
  **Fix:** replace them with what the user acts on.
- **W4 · Should · Eye** **Instructions inside an empty state.**
  **Fix:** one action, such as "+ Add Priya as a walk-in".
- **W5 · Should · Eye** **Keyboard-hint strips, key labels (↵, Esc, 1 2 3) and legends.**
  **Fix:** keep the shortcuts, and show them in a tooltip or a menu.
- **W6 · Should · Eye** **System words on buttons**, such as "Submit" or "OK".
  **Fix:** name the action, for example "Save deal" or "Add as walk-in".
- **W7 · Must · Eye** **Template leftovers**, such as "[Restaurant name]", "Lorem ipsum" or "Your Company".
  **Fix:** put in the real value.
- **W8 · Should · Count** **The same fact twice or more**, for example 87% in a card, as a chart label and in a table.
  **Fix:** say it once, where it's used. If the brief needs it in more than one place, make it clear they're one fact.
- **W9 · Could · Eye** **"Updated by…" sentences, or the same label on every row.**
  **Fix:** show a face, and say a fact shared by every row once, at page level.
- **W10 · Should · Eye** **Sentences where a number would do.**
  **Fix:** show the number or a chart.
- **W11 · Should · Eye** **A generic heading that fits any product**, such as "Dashboard · Track your progress".
  **Fix:** name this user's thing, for example "Senior UX Designer at Freshworks, tomorrow".
- **W12 · Must · Use** **Copy that promises what the app doesn't do**, such as "We'll text you a reminder" when no text is ever sent.
  **Fix:** keep the line only if the feature is built.
- **W13 · Must · Use** **The header names the wrong task**, such as "Doctor" while the user is rescheduling.
  **Fix:** make the header follow what the user is doing now.

These are slop on landing pages only: invented proof ("Trusted by 10,000+ teams", 5.0 stars, made-up testimonials), a marketing tagline on a task screen, and guilt-trip opt-outs ("No thanks, I don't like saving money").

## Data

Sample data gets replaced later, so not every made-up row is slop. A data sign matters when **(a)** it's a design choice (which number a card shows), **(b)** it hides a break (every name short and neat), or **(c)** someone could read it as real.

- **D1 · Must · Eye** **Numbers nobody acts on**, such as "hours practised" or "total logins".
  **Fix:** keep the card, and swap in a number the user acts on. If you can't say why nobody acts on it for this job and moment, keep it.
- **D2 · Must · Eye** **Comparisons with other people, or made-up targets**, such as "+12% vs industry" or an "Excellence 90" line.
  **Fix:** compare with the user's own past, or with a target the user set.
- **D3 · Must · Count** **Numbers that don't add up**, for example a change that doesn't match the scores, or totals that jump.
  **Fix:** work out every total, change, average, percent and "Show all n" from the same rows. The first item says "First", never a made-up change.
- **D4 · Should · Use** **Numbers typed in rather than worked out**, so the widgets disagree or can't update.
  **Fix:** build every widget from one set of data.
- **D5 · Should · Use** **A change or average with nothing to compare**, such as "+x%" on the first item.
  **Fix:** show "—" or "Your first one".
- **D6 · Must · Eye** **A missing value filled with a made-up one.**
  **Fix:** show "—".
- **D7 · Should · Eye** **Colour by direction rather than meaning**, such as falling churn shown in red.
  **Fix:** colour it by whether the change is good or bad for this number.
- **D8 · Should · Eye** **A chart that compares nothing.**
  **Fix:** keep the chart and make it answer a real question, such as the user's own trend or progress against a target they set.
- **D9 · Should · Use** **Counts typed into links**, such as "See all 12".
  **Fix:** count from the data.
- **D10 · Must · Eye** **Dates that don't fit the moment**, such as a history from 2023 for an interview tomorrow.
  **Fix:** put the dates around the scenario's "now".
- **D11 · Should · Eye** **The wrong local formats**, such as a (555) phone number, $ or MM/DD in a product for India.
  **Fix:** use local formats, such as +91, ₹ and DD/MM.
- **D12 · Should · Eye** **Sample data that's too neat**: one row per letter, only famous companies, every name short.
  **Fix:** use an uneven, realistic set, with some long names and some gaps.
- **D13 · Could · Eye** **The default AI sample people**: Sarah Chen, John Doe, Acme, the same names in every run.
  **Fix:** use names and companies that look like the real users.
- **D14 · Must · Count** **A number dropped or swapped without saying so**, such as "Total interviews" quietly replaced inside a number card.
  **Fix:** name every number removed or swapped in the report, with its reason tied to the job. When the reason depends on the moment, keep the number or ask.

## Behaviour

- **B1 · Must · Use** **Controls that do nothing.**
  **Fix:** wire it up. If it's out of scope, keep its label unchanged and show "Not built yet" only on the page it opens. Never add the note to a tab, menu item or button.
- **B2 · Must · Use** **Enter acts on the wrong item**: a part-match search and Enter acts on the first row.
  **Fix:** act only on an exact match, or on a row the user picked.
- **B3 · Must · Use** **One key press handled twice**, on two screens.
  **Fix:** handle each key once.
- **B4 · Should · Use** **Letter shortcuts on a screen where people type.**
  **Fix:** use numbers, Enter and Esc.
- **B5 · Must · Use** **The selection jumps after an action**, for example the list re-sorts and the highlight lands on someone else.
  **Fix:** keep the selection on the item just acted on.
- **B6 · Should · Eye** **Two different states look the same**, such as "Already checked in" and "Checked in".
  **Fix:** give each state its own look.
- **B7 · Should · Use** **No undo, or an undo that leaves a junk row.**
  **Fix:** undo puts everything back.
- **B8 · Must · Use** **Happy path only**: no empty, loading or error version.
  **Fix:** keep every widget, and give each one its empty, loading and error version with the next step.
- **B9 · Must · Use** **An empty state that pretends there's data**, such as a reason "from your last mock" when there was none.
  **Fix:** a first-run version with its own main action.
- **B10 · Must · Eye** **The main action is buried**, for example a practise button 2,282 px down the page.
  **Fix:** make it the first thing on the first screen.
- **B11 · Should · Eye** **The most urgent items aren't first.**
  **Fix:** sort by what needs action now.
- **B12 · Should · Eye** **One screen serving several roles**, such as kitchen, front desk and delivery on one board.
  **Fix:** keep every job, and give each role its own view.
- **B13 · Should · Eye** **The right-looking pattern for the wrong job**, such as a work profile drawn as a social profile.
  **Fix:** pick the pattern that fits this user's task.
- **B14 · Must · Use** **A choice doesn't carry to the next screen**, for example "Added to cart" and then an empty cart.
  **Fix:** carry the state through the flow.
- **B15 · Must · Use** **Undoing a choice doesn't reset what depends on it**, so totals stay wrong.
  **Fix:** reset everything that depends on the choice.
- **B16 · Should · Use** **Lists only fit the amount drawn**: headers scroll away, with no "Show all" or "Show fewer".
  **Fix:** keep the list. Add sticky headers, then the first few rows, "Show all N" and "Show fewer".
- **B17 · Must · Use** **Sideways scroll at phone width**, when phones are in scope.
  **Fix:** wrap or stack, with a 16 px side margin.
- **B18 · Must · Use** **No visible focus, or parts you can't reach by keyboard.**
  **Fix:** give every control a focus ring at 3:1 or better against what's behind it.
- **B19 · Must · Count** **Widgets deleted to "remove slop".**
  **Fix:** keep the widget and fix what's inside it. Remove only what has no job, and say why.
- **B20 · Must · Use** **The AI says it checked something it didn't**, such as "All checks passed" or "Helper lines cut".
  **Fix:** check in a real browser, and treat the AI's own check as unchecked.
- **B21 · Must · Use** **A script error when the page loads.**
  **Fix:** open the page with errors showing before calling it done.

These are slop on landing, sign-up and checkout pages: countdown timers, fake discounts, pre-ticked boxes and hidden close buttons.

## Not slop on its own

Don't flag these unless something else is wrong.

- **Cards, charts and tables on a dashboard.** The widget isn't slop. What's inside it can be.
- **No animation at all.** Calm is fine on a task screen.
- **A common font such as Inter.** It's often picked on purpose. The real sign is flat type (L7).
- **Looking like a familiar product** (Linear, Attio). Familiar helps on a task screen. Going "distinct" for its own sake often fails.
- **Rounded panels at page-region level.** Only boxing every row is slop (L6).
- **A bright colour that always means one thing**, such as Apple Fitness rings or a green for money coming in.
- **A dense list that uses signs people already know**, such as a veg mark, or a rating with its count.
- **Made-up sample rows in a prototype.** Only invented proof, numbers that don't add up, or data that hides a break count (D3, D12).
- **One slip on a careful screen.** Judge the pattern, not one sign.
- **A number repeated because the brief asked for it.** Check the brief first (W8).
- **A polished screen.** Polish isn't a pass. A good-looking screen built for nobody is still slop. Check the job first.
