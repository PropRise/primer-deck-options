# Primer — platform slide options

Design options for the four new slides that replace the old "How Boardwalk" step in Primer's sales deck: **Overview**, **Flow**, the **Input sheet**, and the **Intelligence**. Three options each, twelve in all.

**▶ View the gallery:** https://jeanmichaeldiei.github.io/primer-deck-options/

Every option is one self-contained HTML file rendered at exactly 1280×720 — true deck size. Click any thumbnail to open it full-screen.

## How to vote
Open the [issues](https://github.com/jeanmichaeldiei/primer-deck-options/issues). There's one issue per slide (A–D) with a comment for each option. 👍 the comment for the option you want shipped. The one currently outlined in teal in the gallery is the working recommendation.

Current recommended arc: **A1 → B3 → C3 → D2**.

## How to propose your own option
You don't have to be a designer — point your own Claude Code at this repo.

1. Clone the repo.
2. Tell Claude Code: *"Read `DESIGN.md` and `A1-statement-pillars.html`, then build me a new option for slide C as `C4-my-idea.html` and register it in `slides.json`."*
3. Preview: from the repo root run `python3 -m http.server`, open the printed `localhost` URL, and check your slide in the gallery. (Opening `index.html` directly as a `file://` path won't load `slides.json`.)
4. Open a pull request. Once merged, it shows up in the gallery automatically.

`CLAUDE.md` is the short contract Claude Code should follow; `DESIGN.md` is the full design language.

## Layout
```
index.html          gallery — renders straight from slides.json
slides.json         the manifest (what appears in the gallery)
theme.js            color + font tokens   ── shared design source of truth
deck.css            the 1280×720 stage + helpers ──┘
slide-template.html copy this to start a new option
DESIGN.md           the design language (read before building)
CLAUDE.md           contract for Claude Code
A1-…D3-*.html       the twelve current options
assets/             corner-mark.svg (the only shared asset)
```

## A note on branches
The first commit that created this repo went straight to `main` to bootstrap it. From here on, **changes go through pull requests** — including new options. Keep `main` clean.

The sample deal in every slide ("The Jasmine," Dallas) is fictional, which is why this repo can be public.
