# Break list: worst-case data and states

Try these on the screen before calling it done. Most AI-made screens are drawn for one neat amount of data, and they break on the first real one.

**Which cases to pick**
- Always: **empty**, **one item**, **many items**, **a very long name**, **every control clicked**, **keyboard only**, **contrast**, **numbers agree**.
- Then pick the cases that fit this screen: a search box, numbers, a flow across several screens, a phone, a wall screen.
- Write down every case you tried, even the ones that held. A case you couldn't try goes under "Not tried" in the report, with the reason.

**Results**
- **Holds**: works and still looks right.
- **Ugly**: works, but looks wrong (it wraps badly, leaves a gap or hides something).
- **Breaks**: it fails, or it misleads.

**How to try a case**
- **With a browser:** load the case, then look and click. This is the only real test.
- **Without a browser:** read the code for each case and say what would happen. Mark the result "not tried" and say that only the code was read. Never mark it "holds" from reading the code alone.

To make cases easy to load, give the page test switches, for example `#empty`, `#one`, `#many` and `#long` at the end of the address.

## How much data

| Case | What usually breaks |
|---|---|
| **Empty**: no records yet | Charts divide by zero, cards show a fake change, reasons quote data that doesn't exist, widgets collapse |
| **One item** | A change or average with nothing to compare, a one-point chart |
| **Two or three items** | "Since last" wording, a chart with no middle |
| **Many**: 15, 300, 1,000 | Headers scroll away, chart labels crowd, the selected row hides under the top bar, the list pushes everything down |
| **Show all, then Show fewer** | The link vanishes with no way back |

## Text

| Case | What usually breaks |
|---|---|
| **A very long name**, such as "Thirumalai Venkata Lakshmi Narasimha Subramanya Sastrigal" | It stretches the table, pushes numbers off the side, or a badge cuts the word in half |
| **A long word with no spaces**, such as an email or a web address | The column overflows |
| **A short word in a narrow column** at 1024 px | It breaks mid-word ("Volun-teer") |
| **Long typed text in a field or search** | The button label or the field overflows |
| **Indian scripts, or right-to-left text** | Letters break, or the layout doesn't mirror |
| **Local formats**: ₹12,34,567, DD/MM, +91 | US defaults show up instead |

## Numbers

| Case | What usually breaks |
|---|---|
| **Huge numbers**, such as ₹12,34,56,789 or 1,284 members | The number card overflows, and columns stop lining up |
| **Zero, 0% and 100%** | A label falls off the top of the chart, or a fixed scale hides low values |
| **A very high and a very low value together** | The chart scale flattens one of them |
| **Tied values**, such as two weakest areas at 78% | It picks one at random, or highlights neither |
| **A missing value**, such as no phone or no date | A made-up value appears instead of "—", or the columns shift |
| **A falling number where down is good**, such as churn | It shows in red |
| **Numbers agree**: work out every change, average and count again from the rows | A change doesn't match the scores, "First mock" sits next to "12 done", or "Show all 12" opens 8 |

## Typing and actions

| Case | What usually breaks |
|---|---|
| **A part-match search + Enter**, such as only the company name | It acts on the wrong person |
| **A symbols-only search + Enter** ("@#") | It matches everyone and acts on a random row |
| **An empty search + Enter** | It acts on someone |
| **A sound-alike search** ("shah" for "Shaw") | The wrong person is ranked first |
| **The same action twice**, such as checking in someone already checked in | The second time looks like the first |
| **Undo**, after an action or a wrong entry | There's no undo, or a junk row is left behind |
| **Click every control** | Some controls do nothing |

## Moving around

| Case | What usually breaks |
|---|---|
| **Walk screen 1 → 2 → 3** | The header or nav changes, or a choice is lost on the way |
| **The back link, then the browser's back** | You land somewhere odd, or old totals stay |
| **Change a choice, then change it back** | Totals don't reset |
| **Reload in the middle of a task** | The work is lost |

## Access and loading

| Case | What usually breaks |
|---|---|
| **Permission denied**, such as a blocked microphone or a record you can't open | No message, or the screen gets stuck |
| **Slow load** | There's no loading state, and the screen pops in complete |
| **Failed load** | There's no error, or the error has no fix |
| **Open the page with errors showing** | A script error appears on load |

## Screens and senses

| Case | What usually breaks |
|---|---|
| **Phone width**, 375 or 390 px (when phones are in scope) | The page scrolls sideways, menus get clipped, or table columns sit off-screen. Turn table rows into stacked blocks |
| **Inside each table and card**, at 1280 and 1024 px | The page doesn't scroll, but the last column or a number is cut off inside its box |
| **A small laptop**, 1024 px, with a side panel open | Columns get squeezed |
| **200% zoom** | Things get clipped or overlap |
| **Dark mode** (if the product has it) | Text or borders vanish |
| **Keyboard only**: Tab, Enter, Esc | There's no visible focus, the focus ring is under 3:1 against what's behind it, or controls can't be reached |
| **Contrast**: measure text against the pixels behind it | Text under 4.5:1 (3:1 for large text), most often white on a coloured button or grey on grey |
| **Read from 2 m away**, for a wall or counter screen | The text can't be read |
