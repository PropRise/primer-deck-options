# Start here

You're Claude Code, and you're about to design a slide for Primer's sales deck together with the person you're talking to. This file tells you everything you need. Read it top to bottom, then say hello and ask what they want to make.

The whole point: **your human describes what they want in plain English, you build it, they look at it, you refine it together, and when they're happy you ship it as a pull request.** They should never have to think about files, JSON, ports, or git. That's your job.

## The three things to read before you build
1. **`DESIGN.md`** — the look. Colors, type, the 1280×720 frame, the reusable components, the sample deal's numbers, and the writing patterns to avoid. This is the contract that keeps every slide looking like one deck.
2. **One real slide** — open `A1-statement-pillars.html` (a clean light one) and `D2-ask-primer-chat.html` (a richer one). Copy these patterns instead of inventing new ones.
3. **`CLAUDE.md`** — the short rules of the repo.

## The tool: `./deck`
One command does each thing. You drive it; the human watches the result.

```
./deck new C4 "Dark workbook" "Dark · formula bar"   # start a new option
./deck preview                                        # gallery at localhost:5300
./deck publish "made slide C dark"                    # ship it as a PR
./deck check                                          # is everything wired up?
```

`./deck new` creates the file **and** lists it in the gallery, so it can't be forgotten. To change an existing option instead, just edit its `.html` file directly — no `new` needed.

## The loop
1. **Understand.** Ask which slide (A Overview · B Flow · C Input sheet · D Intelligence) and what they want — a fresh option, or a tweak to an existing one. One or two questions, then build.
2. **Build.** `./deck new …` for a new option (then edit the file), or edit the existing file. Stay inside the `<section class="stage">`, keep it 1280×720, use the palette tokens from `theme.js` (e.g. `bg-bgdark`, `text-teal`, `font-serif`) and the helpers in `deck.css`. Keep the sample-deal numbers consistent with `DESIGN.md`.
3. **Show.** Run `./deck preview` and tell them: *"Open http://localhost:5300 and refresh — it's the third card under Slide C."* If you have a browser or screenshot tool, look at it yourself first and fix the obvious things before handing it over.
4. **Refine.** Take their feedback, edit, tell them to refresh. Repeat until they say it's right.
5. **Ship.** `./deck publish "one line about what you made"`. That opens a pull request. Tell them the PR link and that JM reviews and merges it, after which it's live on the gallery within about 30 seconds.

## Rules that matter
- The frame is **exactly 1280×720** — the deck is rebuilt 1:1 in PowerPoint. Never resize it.
- **Don't touch** `theme.js`, `deck.css`, or anyone else's slide file. Those are shared. Your work lives in your own option file (+ the one line `./deck` adds to `slides.json`).
- Follow the **banned copy and visual patterns** in `DESIGN.md` (no staccato fragments, no rhetorical question-and-answer, no accent lines under titles, no overflowing boxes). Write like you'd talk to a colleague.
- Keep Primer accurate — it maps into the customer's own model, cites every cell, flags anomalies, and builds a comp warehouse. The product-truth paragraph in `DESIGN.md` is the source.

## First-time setup (only if a command fails)
- `./deck publish` needs the GitHub CLI signed in: run `gh auth status`, and if needed `gh auth login`.
- If the push is denied, the human isn't a collaborator yet — ask JM to add them (repo → Settings → Collaborators), or run `gh repo fork --remote` and re-run publish.

That's it. Say hi, ask what slide they want to make, and start.
