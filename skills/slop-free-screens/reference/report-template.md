# Report template for chat

Use this when the tool can't make an HTML file, such as ChatGPT, Gemini, or Figma Make's chat.
It has the same parts as report-template.html, in the same order.

- **Show, don't tell.** Attach a screenshot or crop for each widget, each leftover and each break case. If the tool can't show images, name the file to open.
- **Captions only.** Keep "found" and "replaced with" to 6 words or fewer each.
- **Don't repeat the rules.** Tag each fix with its rule id from the slop list (L3, W1) or from team-rules.md. List only the new rules from this run.
- **A step that wasn't run** gets "Not run yet" under its heading.

---

## Slop report: {screen}

{date} · {tool}
**{verdict, 10 words or fewer}**
**For:** {who, when · the job}
**Picked:** {direction and why, new screens only}
**{n} fixes · {n} removed · {n} still there · {n} breaks**

### Before and after
{before screenshot} → {after screenshot}

### What changed
**{Widget} · Kept** · {before crop} → {after crop}
- {found} → {replaced with} `{rule}`

**{Widget} · Removed** · {before crop}
- {why it had no job}

### Still there
- {crop with the spot ringed} **{what}** `{rule}`: {why it stays}

### Try to break it
Breaks {n} · Ugly {n} · Holds {n}

| Case | Result | Screenshot | What happens |
|---|---|---|---|
| {case} | {Breaks / Ugly / Holds} | {file} | {6 words} |

**Not tried:** {case} ({why}) · {case}

### New rules
1. {rule} *(the rules the skill already holds are not listed)*

Saved to team-rules.md. Or, if the tool can't write files: "Add these to team-rules.md."
