# previews/

Screenshots of slides, captured at 1280×720 and attached to pull requests so a
reviewer can see a change without checking out the branch.

`./deck publish` drops them here automatically (one PNG per changed slide) and
embeds them in the PR body. You can also make one by hand:

```
./deck shot A1-statement-pillars.html        # -> previews/A1-statement-pillars.png
./deck shot context/9-pricing.html           # -> previews/9-pricing.png
```

These PNGs are the one kind of binary we keep in the repo on purpose. They are
review artifacts, not slide assets — a slide must never depend on a file in here.

The files prefixed with `_` (e.g. `_launchpad-spine.png`) are screenshots of the
gallery UI itself, used to illustrate `FLOW.md` and the contribution-flow PR.
Everything else is a 1280×720 slide render.
