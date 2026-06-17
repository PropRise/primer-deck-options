# Working in this repo (for Claude Code)

This repo holds **slide options** for one part of Primer's sales deck. Each option is a single self-contained HTML file at exactly 1280×720. A teammate (or their Claude Code) can add a new option without touching anyone else's work.

**If you're here to help someone design a slide, read `ONBOARDING.md` first** — it's the step-by-step for the human + Claude Code loop.

## Read first
1. **`DESIGN.md`** — the design language. Colors, type, the 1280×720 frame, recurring components, the sample deal, and the banned copy/visual patterns. This is the contract.
2. **An existing slide** as a worked example — `A1-statement-pillars.html` (light) or `D2-ask-primer-chat.html` (richer). Copy patterns from these instead of inventing new ones.

## The workflow — use `./deck`
One tool does each step. Prefer it over running git / servers / JSON edits by hand.

```
./deck new C4 "Dark workbook" "Dark · formula bar"   # create + auto-list a new option
./deck preview                                        # gallery at localhost:5300
./deck publish "made slide C dark"                    # branch + commit + push + PR
./deck check                                          # validate slides.json ↔ files
```

- **New option:** `./deck new …` writes the file from the template **and** registers it in `slides.json`, so it always shows in the gallery. Then build inside the single `<section class="stage">`.
- **Edit an existing option:** just edit its `.html` file — no `new` needed.
- **Build rules:** keep the 1280×720 frame; use the palette tokens from `theme.js` (e.g. `bg-bgdark`, `text-teal`, `font-serif`) and the helpers in `deck.css`. Don't redefine colors or the stage in a slide file.
- **Preview:** `./deck preview` serves over http so the manifest loads (opening `index.html` as a `file://` path won't).
- **Ship:** `./deck publish "…"` opens a PR. Don't commit slide changes straight to `main`.

## Hard rules
- One file = one option. Never edit another option's file to make yours work.
- The 1280×720 size is fixed — the deck is rebuilt 1:1 in PowerPoint against it.
- Keep the sample-deal numbers consistent with `DESIGN.md` so figures match across slides.
- Follow the banned-copy and banned-visual lists in `DESIGN.md` (no staccato fragments, no rhetorical Q+A, no accent lines under titles, etc.).
- The only shared asset is `assets/corner-mark.svg`. Don't add binary assets unless a slide genuinely needs one.

## What not to touch
- `theme.js` / `deck.css` — shared design source of truth. Change these only in a dedicated PR that's explicitly about the design system, never as a side effect of a new slide.
- Other people's slide files.
