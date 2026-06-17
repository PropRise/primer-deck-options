# Working in this repo (for Claude Code)

This repo holds **slide options** for one part of Primer's sales deck. Each option is a single self-contained HTML file at exactly 1280×720. A teammate (or their Claude Code) can add a new option without touching anyone else's work.

## Read first
1. **`DESIGN.md`** — the design language. Colors, type, the 1280×720 frame, recurring components, the sample deal, and the banned copy/visual patterns. This is the contract.
2. **An existing slide** as a worked example — `A1-statement-pillars.html` (light) or `D2-ask-primer-chat.html` (richer). Copy patterns from these instead of inventing new ones.

## To add an option (the only workflow)
1. Copy the template: `cp slide-template.html E1-my-idea.html` (name it `<Slide><n>-<short-name>.html`; pick the next free number for that slide letter, or a new letter for a new slide).
2. Build the slide inside the single `<section class="stage">`. Keep the frame. Use the palette tokens from `theme.js` (e.g. `bg-bgdark`, `text-teal`, `font-serif`) and the helpers in `deck.css` — **don't** redefine colors or the stage inside the file.
3. Register it: add one entry to **`slides.json`** under the right slide letter. The gallery (`index.html`) renders straight from that file, so the option then appears automatically.
4. Preview locally by serving the folder (`python3 -m http.server` from the repo root, then open `index.html`) — opening `index.html` as a `file://` path won't load `slides.json`.
5. Open a **PR**. Don't commit slide changes to `main`.

## Hard rules
- One file = one option. Never edit another option's file to make yours work.
- The 1280×720 size is fixed — the deck is rebuilt 1:1 in PowerPoint against it.
- Keep the sample-deal numbers consistent with `DESIGN.md` so figures match across slides.
- Follow the banned-copy and banned-visual lists in `DESIGN.md` (no staccato fragments, no rhetorical Q+A, no accent lines under titles, etc.).
- The only shared asset is `assets/corner-mark.svg`. Don't add binary assets unless a slide genuinely needs one.

## What not to touch
- `theme.js` / `deck.css` — shared design source of truth. Change these only in a dedicated PR that's explicitly about the design system, never as a side effect of a new slide.
- Other people's slide files.
