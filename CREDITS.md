# Credits

slop-free-screens takes **ideas** from the open skills and guides below. Each idea is rewritten in our own words. **No text or code was copied.**

Licences are as recorded when we read each source in October 2026. Where we read the licence only in a README, we say so. Check the source for its current terms.

## The 10 sources

| Source | Author | Licence | The idea we took | Where it shows up |
|---|---|---|---|---|
| [impeccable](https://github.com/pbakaus/impeccable) | Paul Bakaus | Apache 2.0 (licence as stated in its README) | Accent colour only for action, selection or state. Judge with your eyes first, then run the checks, and report any check that couldn't run. A list of accepted findings, so they aren't raised again. | Step 2 colour jobs, step 4 "Not tried", team-rules "Accepted on purpose" |
| [frontend-design](https://github.com/anthropics/skills) | Anthropic | Apache 2.0 | Name who it's for, the job and the moment, and confirm them before designing. A quick plan (colours, type, rough wireframe) checked against the brief before building. Borders, numbers and labels must carry real information. | Steps 1 and 3, Data signs |
| [audit-ai-design-slop](https://github.com/MengTo/Skills) | Meng To | MIT (licence as stated in its README) | Name each element's job, and remove it only if it has none. A report that leads with a verdict and lists unknowns. Fake-content signs such as stock names and round stats. | Step 4, the report, Data signs |
| [break-ui](https://github.com/emilkowalski/skills) | Emil Kowalski | MIT (licence as stated in its README) | Feed worst-case data into the screen: a very long name, exactly one item, 1,000+ rows, huge numbers. Build options with a switch to compare them. | The break list, step 3 |
| [Hallmark](https://github.com/Nutlope/hallmark) | Nutlope / Together AI | MIT | Test at set widths so nothing scrolls sideways. Fail if working parts disappear. Three levels of check, from must-fix to nice-to-have. Show the picks as a short block the person can redirect. | Break list, Must / Should / Could, step 1 |
| [ux-skill](https://github.com/Laith0003/ux-skill) | Laith0003 | MIT | Add "Not allowed" and "How we'll know it worked" to the questions. Rate severity by who notices: spotted as AI within 3 seconds is critical. Fake-content signs. | Step 1 questions, sign levels |
| [Refero skill](https://github.com/referodesign/refero_skill) | Refero | MIT | Every big choice traces to a reference. Don't average references into a safe middle. Lock one direction and keep a table: choice → reference → reason. | Step 2 reference screens, step 3 fast-mode table |
| [open-design anti-slop](https://github.com/nexu-io/open-design) | nexu-io | Apache 2.0 | Slop signs in tiers. Accent colour only where it means something. | The slop list's levels, step 2 colour jobs |
| [DESIGN.md](https://github.com/google-labs-code/design.md) | Google Labs | Apache 2.0 | A product's design values written down with the reasons behind them. Real references beat adjectives like "modern". Compare rule versions and flag when things get worse. | team-rules.md, step 2 |
| [Web Interface Guidelines](https://vercel.com/changelog/web-interface-guidelines-now-available-as-an-agent-command) | Vercel | MIT | Craft checks across focus, forms, empty states and number formats. | The break list, Behaviour signs |

## Added after testing against Hallmark (30 Oct 2026)

We ran Hallmark's own checker on the same dashboard we used to test this skill. It found things our first version missed, so we added these ideas, again in our own words:

- **Contrast is measured against the real background,** including white text on a coloured button or badge.
- **A focus ring needs 3:1 or better** against whatever is behind it.
- **Every number is worked out again from the rows behind it:** changes, averages, counts and "Show all n".
- **Check inside each table and card,** not just the page: a page that doesn't scroll sideways can still cut off a column.

## Where "defaults" come from

The idea that models drift to the most common answer, so every choice nobody makes falls back to the average, comes from Anthropic Applied AI's post on improving frontend design through skills. They call it **distributional convergence**.
Prithvi Rajasekaran, Justin Wei and Alexander Bricken, 12 Nov 2025: https://claude.com/blog/improving-frontend-design-through-skills
