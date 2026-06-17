# Primer — platform slide options

Design options for the four new slides that replace the old "How Boardwalk" step in Primer's sales deck: **Overview**, **Flow**, the **Input sheet**, and the **Intelligence**. Three options each, twelve in all.

**▶ View the gallery:** https://jeanmichaeldiei.github.io/primer-deck-options/

Every option is one self-contained HTML file rendered at exactly 1280×720 — true deck size. Click any thumbnail to open it full-screen.

## How to vote
Open the [issues](https://github.com/jeanmichaeldiei/primer-deck-options/issues). There's one issue per slide (A–D) with a comment for each option. 👍 the comment for the option you want shipped. The one currently outlined in teal in the gallery is the working recommendation.

Current recommended arc: **A1 → B3 → C3 → D2**.

## How to make or change a slide (with your own Claude Code)
You don't have to be a designer or know git. Point your Claude Code at this repo and talk to it.

1. Clone the repo and open your Claude Code in it.
2. Say: ***"Read ONBOARDING.md and let's design a slide."***
3. Describe what you want in plain English. It builds the slide, runs `./deck preview`, and you watch it at `http://localhost:5300` (refresh after each change). Refine together.
4. When you're happy, say **"ship it."** It runs `./deck publish "…"`, which opens a pull request. JM reviews and merges; the gallery updates within ~30 seconds.

Everything is driven by one tool — you rarely type these yourself:

```
./deck new C4 "Dark workbook" "Dark · formula bar"   # start a new option
./deck preview                                        # see the gallery locally
./deck publish "made slide C dark"                    # ship it as a PR
```

`ONBOARDING.md` is the guide Claude Code follows; `DESIGN.md` is the full design language; `CLAUDE.md` is the short repo contract.

## Layout
```
deck                the one tool: new / preview / publish / check
ONBOARDING.md       the human + Claude Code loop (start here)
index.html          gallery — renders straight from slides.json
slides.json         the manifest (what appears in the gallery)
theme.js            color + font tokens   ── shared design source of truth
deck.css            the 1280×720 stage + helpers ──┘
slide-template.html the blank slide ./deck new copies from
DESIGN.md           the design language (read before building)
CLAUDE.md           contract for Claude Code
scripts/deckkit.py  helper behind ./deck (new, check)
A1-…D3-*.html       the twelve current options
assets/             corner-mark.svg (the only shared asset)
```

## A note on branches
The first commit that created this repo went straight to `main` to bootstrap it. From here on, **changes go through pull requests** — including new options. Keep `main` clean.

The sample deal in every slide ("The Jasmine," Dallas) is fictional, which is why this repo can be public.
