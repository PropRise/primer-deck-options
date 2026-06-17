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
./deck publish "made slide C dark"                    # branch + commit + push + PR (+ screenshot)
./deck check                                          # validate slides.json ↔ files
./deck shot A1-statement-pillars.html                 # screenshot a slide into previews/
```

- **New option:** `./deck new …` writes the file from the template **and** registers it in `slides.json`, so it always shows in the gallery. Then build inside the single `<section class="stage">`.
- **Edit an existing option:** just edit its `.html` file — no `new` needed.
- **Build rules:** keep the 1280×720 frame; use the palette tokens from `theme.js` (e.g. `bg-bgdark`, `text-teal`, `font-serif`) and the helpers in `deck.css`. Don't redefine colors or the stage in a slide file.
- **Preview:** `./deck preview` serves over http so the manifest loads (opening `index.html` as a `file://` path won't).
- **Ship:** `./deck publish "…"` opens a PR. It also screenshots each changed slide into `previews/` and embeds it in the PR so reviewers see the change without checking out the branch. Don't commit slide changes straight to `main`.

## The contribution flow (`✎ Tweak this` / `＋ Add a slide here`)
The gallery has buttons that hand a teammate a ready-to-paste prompt for their own Claude Code — one to tweak an existing slide, one to add a slide between two others. If you're the Claude Code that received such a prompt: follow it, read the design docs it points at, build inside the 1280×720 stage, preview, and on "ship it" screenshot the slide and `./deck publish`. **Never merge — JM reviews.** Full design note: `FLOW.md`.

## How the gallery is laid out — `deck[]` + `context/`
The gallery shows the **whole deck in running order**, not a loose grid of options. `slides.json` drives it with two parts:

- **`deck[]`** — the running order. Each entry is either `{ "type": "fixed", "file": "context/…html", … }` (a decided slide) or `{ "type": "decision", "slide": "A" }` (an open slot that renders the options from `slides[]`). Edit `deck[]` to reorder the deck or move where an open slot sits.
- **`slides[]`** — the options for each open slot (A–D), unchanged from before.

**`context/`** holds the decided slides that frame the open ones (cover, context, results, pricing). They use the same `theme.js` / `deck.css` via relative paths (`../theme.js`) and live in a subdir so `./deck check` doesn't mistake them for stray options.

**Sanitization — the repo is public, so context slides must not leak customer data.** When you add or edit anything in `context/`: real dollar figures become `$`, real firm names become a generic stand-in (e.g. "Acme Storage"), and any headshot becomes a neutral tile. Keep the quotes, figures, and layout exactly as the real slide — obscure only the identifying details. The open slides (A–D) already use a fictional sample deal ("The Jasmine," Dallas), so they need no sanitizing.

## Hard rules
- One file = one option. Never edit another option's file to make yours work.
- The 1280×720 size is fixed — the deck is rebuilt 1:1 in PowerPoint against it.
- Keep the sample-deal numbers consistent with `DESIGN.md` so figures match across slides.
- Follow the banned-copy and banned-visual lists in `DESIGN.md` (no staccato fragments, no rhetorical Q+A, no accent lines under titles, etc.).
- The only shared slide asset is `assets/corner-mark.svg`. Don't add binary assets unless a slide genuinely needs one. (`previews/*.png` are the one sanctioned exception — they're PR review screenshots, not slide assets, and no slide may depend on them.)
- Never put real customer names, dollar figures, or photos in `context/` — sanitize as above.

## What not to touch
- `theme.js` / `deck.css` — shared design source of truth. Change these only in a dedicated PR that's explicitly about the design system, never as a side effect of a new slide.
- Other people's slide files.
