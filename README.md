# Primer — the platform deck, with the open slides in place

This is Primer's sales deck in running order, with the four slides we're still deciding sitting in their real positions. You see each open slide where it actually lands in the pitch, flip between the options for it without leaving the page, and vote on the one to ship. The decided slides around them — cover, context, results, pricing — are there so you can judge each option in context, not in a vacuum.

The four open slides replace the old "How Boardwalk" step: **Overview**, **Flow**, the **Input sheet**, and the **Intelligence**. Three options each, twelve in all.

**▶ View the gallery:** https://proprise.github.io/primer-deck-options/

Every slide is one self-contained HTML file rendered at exactly 1280×720 — true deck size. Click the corner icon on any slide to open it full-screen.

## What you're looking at
The gallery is a single vertical spine — the deck top to bottom.

- **Decided slides** carry a hollow dot and a "Decided" tag. They render calmly; nothing to do but read them. These are sanitized for the public repo (see the note at the bottom).
- **Open slides** carry a filled teal dot and an "Open · pick one of N" tag. Below each one is a row of option pills — click a pill to **audition that option in place**, right where it sits in the deck. The slide swaps, the full-screen link follows, and the vote hint updates.

## How to vote
Open the [issues](https://github.com/PropRise/primer-deck-options/issues). There's one issue per open slide (A–D) with a comment for each option. 👍 the comment for the option you want shipped. The pill outlined in teal (marked ★ rec) is the working recommendation.

Current recommended arc: **A1 → B3 → C3 → D2**.

## How to make or change a slide (with your own Claude Code)
You don't have to be a designer or know git. The gallery hands you the prompt.

**The easy way — straight from the gallery.** Hover any slide and hit **✎ Tweak this**, or **＋ Add a slide here** in the gap between two slides. A panel pops up with a ready-to-paste prompt (and a one-line clone command for first timers). Copy it, paste it into your own Claude Code running in a clone of this repo, and describe what you want. It builds the slide, previews it, screenshots it, and opens a PR for JM to review. Tweak and add use different prompts, because they're different jobs. See `FLOW.md` for how the whole thing works.

**By hand, if you'd rather.** Point your Claude Code at the repo and talk to it:

1. Clone the repo and open your Claude Code in it.
2. Say: ***"Read ONBOARDING.md and let's design a slide."***
3. Describe what you want in plain English. It builds the slide, runs `./deck preview`, and you watch it at `http://localhost:5300` (refresh after each change). Refine together.
4. When you're happy, say **"ship it."** It screenshots the slide and runs `./deck publish "…"`, which opens a pull request with the screenshot in it. JM reviews and merges; the gallery updates within ~30 seconds.

Everything is driven by one tool — you rarely type these yourself:

```
./deck new C4 "Dark workbook" "Dark · formula bar"   # start a new option
./deck preview                                        # see the gallery locally
./deck publish "made slide C dark"                    # ship it as a PR (+ screenshot)
./deck shot A1-statement-pillars.html                # screenshot a slide into previews/
```

`FLOW.md` explains the contribution flow; `ONBOARDING.md` is the guide Claude Code follows; `DESIGN.md` is the full design language; `CLAUDE.md` is the short repo contract.

## Layout
```
deck                the one tool: new / preview / publish / check / shot
ONBOARDING.md       the human + Claude Code loop (start here)
FLOW.md             how the "tweak / add a slide" contribution flow works
index.html          gallery — renders the deck straight from slides.json
slides.json         the manifest: the deck running order + the open options
theme.js            color + font tokens   ── shared design source of truth
deck.css            the 1280×720 stage + helpers ──┘
slide-template.html the blank slide ./deck new copies from
DESIGN.md           the design language (read before building)
CLAUDE.md           contract for Claude Code
scripts/deckkit.py  helper behind ./deck (new, check)
A1-…D3-*.html       the twelve current options for the open slots
context/            the decided slides around them (sanitized)
previews/           slide screenshots attached to PRs (auto-made on publish)
assets/             corner-mark.svg (the only shared asset)
```

`slides.json` has two parts. `deck[]` is the full running order — `fixed` items point at a decided slide in `context/`, `decision` items reserve a slot for an open slide (A–D). `slides[]` holds the options for each open slot. The gallery walks `deck[]` to lay out the spine and pulls the options from `slides[]` for each open slot.

## A note on branches
The first commit that created this repo went straight to `main` to bootstrap it. From here on, **changes go through pull requests** — including new options. Keep `main` clean.

## Why this can be public
Two things keep it safe to leave open:

- The sample deal in the *open* slides ("The Jasmine," Dallas) is fictional.
- The *decided* context slides are sanitized. Real dollar figures show as `$`, real firm names are generalized (e.g. "Acme Storage"), and the one customer headshot is replaced with a neutral tile. The quotes, the figures' shape, the layout, and everything else are the real slides — only the identifying details are obscured.
