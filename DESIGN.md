# Design language

The contract that keeps every slide looking like the same deck. Read this before you build an option. If you point your own Claude Code at this repo, point it here first.

The two files that enforce it: **`theme.js`** (color + font tokens) and **`deck.css`** (the stage frame + helpers). Link both and your slide is in-language by default. Don't redefine colors or the stage inside a slide file.

---

## Design principles (the vibe)

These are the habits to carry into every slide. They are about taste and judgment, not exact numbers. When a choice is unclear, come back here.

- **Let it breathe. Nothing touches an edge.** Every element keeps equal padding from its container on all sides, with a sensible minimum. Text never runs up against a border, a divider, or the stage edge. When something feels tight, add room before adding cleverness.
- **Equal heights across a row.** Cards that sit side by side share one height. Align them to the row, not to their own content. Uneven card heights read as a mistake.
- **One idea per element.** A card, a callout, or a cell makes a single point. If you are explaining two things, use two elements. Cut anything that does not help the reader understand, decide, or trust.
- **Plain language always.** Simple words, complete sentences, no em or en dashes, no filler. See the Voice section below and `sales/knowledge/plain-writing-reference.md` in the GrowthOS repo. If you would not say it to a colleague, cut it.
- **Lead with the customer.** It is their model, their chart of accounts, their level of detail, their process. Use "you" and "your." Make clear Primer is configured to the way they already work, set up with them.
- **Say what is true, no more and no less.** Do not oversell: Primer runs the first pass and the model population, not the full underwrite. Do not undersell: it is not "just a reader." Match the claim to the evidence.
- **Show, don't assert.** Prove a point with a concrete artifact: a reconciliation, a cell reference, a comp query. Real examples beat adjectives.
- **Make the hero obvious.** The main thing on a slide should win by weight, space, or elevation, not by a louder color. Supporting elements stay quiet.
- **Connectors carry meaning.** Every arrow or line should mean something and land cleanly. Remove stray or decorative lines. If a numbered spine already shows the order, you do not also need arrows.
- **Replace decoration with substance.** If a box exists only to fill space, give it a real job or remove it.

---

## The frame

- Every slide is one `<section class="stage">` at exactly **1280 × 720**. Never change that size — the deck is rebuilt 1:1 in PowerPoint against it.
- Place elements absolutely with `.b` + Tailwind arbitrary values, in pixels from the top-left:
  ```html
  <div class="b left-[65.3px] top-[58px] w-[980px]">…</div>
  ```
- Standard left margin is **65.3px**. The eyebrow sits at `top-[18.2px]`, the headline at ~`top-[58px]`.
- The puzzle corner mark goes top-right on every slide: `<img src="assets/corner-mark.svg" class="corner" alt="">`.
- Light slides: `class="stage bg-paper text-ink"`. Dark slides: `class="stage bg-bgdark text-white"`.

## Color tokens (defined in `theme.js`)

| Token | Hex | Use |
|---|---|---|
| `ink` | `#1A1A1A` | primary text on light |
| `body` | `#3D4F47` | body copy on light |
| `muted` | `#6B7D75` | secondary / captions |
| `teal` | `#2C8B7B` | primary brand, headings-in-cards, icons |
| `tealbar` | `#408179` | the left nub on pillar cards, arrows |
| `tint` | `#E6F6F3` | soft teal fill (callouts, warehouse) |
| `bgdark` | `#193C33` | dark slide background |
| `paper` | `#FBFDFB` | light slide background |
| `line` | `#D8DDD9` | borders, rules |
| `risk` / `riskbg` / `riskline` | `#C0392B` / `#FBEEEC` / `#D64C42` | anomaly / flag cards |
| `warn` | `#B7791F` | softer caution (vacancy, subjective) |

Use the token, not the raw hex, so a palette change stays one edit.

## Type

- **Headlines:** Playfair Display via `class="title"` (serif, `line-height:1.06`). One idea, ≤ 2 lines.
- **Body / UI:** Inter (default).
- **Formulas / cell refs:** `font-mono` — e.g. `='Primer Input'!BY2`.
- **Eyebrow:** `class="eyebrow"` + a tracking preset (`tr-179` is standard). Short, uppercase.

## Recurring components (copy these, don't reinvent)

- **Pillar card** — white card, teal left nub, line icon, bold teal heading, body line, a divider + one proof detail. See `A1-statement-pillars.html`.
- **Flag / anomaly card** — `riskbg` fill, `riskline` left border, `⚠ TITLE` in `risk`, one explanatory line, optional `Risk` chip. See `A2` / `D2`.
- **Spreadsheet grid** — use the `.xl-grid` classes (`th.r`/`td.r` right-align, `.status-occ`/`.status-vac`, `.formula`). See `C3-excel-workbook.html`.
- **Warehouse strip** — dark/tint band, database icon, "saved to your warehouse" + an *Ask Primer* example line. See `A2` / `D2`.

## The sample deal (keep numbers consistent)

Every option uses the same fictional deal so figures match across slides:

- **The Jasmine**, 13450 Esperanza Rd, Dallas TX · Multi-Family · **370 units** · model `GoldRockModel_v12.xlsx`
- Avg rent/unit **$1,037 → $1,194**; NOI **$1.53M → $2.64M**; Gross Rev **~$4.49M → ~$5.36M**; unrenovated **318 / 370**
- Reconciliation: OM **$4,490,000** / T-12 **$4,412,000** → Rent Roll **$4,378,440** (OM overstated ~$111K)
- Three flags: **Taxes not broken out**, **Management fee not in T-12**, **Insurance not broken out**
- Warehouse: **1,465 comps**; example query → Phoenix insurance **$487/unit/yr** across 15 deals
- Sample formulas: `='Primer Input'!BY2`, `=+'RENT CALCS'!E7`, `='Primer Input'!BY12`
- Citations look like: *Rent Roll p.4*, *T-12 p.38*, file *The Jasmine_OM_NorthMarq.pdf*

If you need new numbers, keep them internally consistent with these.

## Voice — avoid these AI tells (hard rules)

Banned copy patterns:
1. Staccato fragments — "No AI. Just formulas."
2. Rhetorical question + punchy answer — "The result? It worked."
3. Three-word dramatic endings — "That's the difference."
4. Fake-profound one-liners — "Simple beats complex."
5. "Not X, it's Y" — "It's not about the data. It's about the people."

Write complete sentences with specific numbers and names. If you wouldn't say it to a colleague, cut it.

Banned visuals:
- No accent lines *under* titles (use whitespace).
- No decorative full-width colored bars/ribbons.
- No cream/beige backgrounds — light slides use `paper`.
- Nothing overflowing its box; nothing cut off at the stage edge.

## Product truth (so options stay accurate)

Primer is an **AI agents platform for institutional CRE acquisitions** — not generic "data extraction." It reads the deal room, pulls comps / market / tax data, reconciles conflicts, **maps into the customer's own Excel model** (it writes one "Primer Input" tab; the customer's formulas reference it — 255 of them in the sample), **cites every cell** to source, **flags anomalies**, and **saves every deal to a queryable warehouse**. It's configured to a firm's model during a paid pilot — don't imply a generic demo is already tuned to a prospect's exact model.
