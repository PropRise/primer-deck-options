#!/usr/bin/env python3
"""Helper for the `deck` CLI. Handles the slides.json-aware verbs (new, check)
so the bash side can stay simple. Not meant to be called directly — use `./deck`.
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "slides.json")
TEMPLATE = os.path.join(ROOT, "slide-template.html")
OPTION_RE = re.compile(r"^[A-Z][0-9]+-.*\.html$")

GREEN, RED, DIM, BOLD, END = "\033[32m", "\033[31m", "\033[2m", "\033[1m", "\033[0m"
def ok(m):   print("%s✓%s %s" % (GREEN, END, m))
def bad(m):  print("%s✗%s %s" % (RED, END, m))
def info(m): print("%s%s%s" % (DIM, m, END))

def load():
    with open(MANIFEST) as f:
        return json.load(f)

def save(data):
    with open(MANIFEST, "w") as f:
        f.write(json.dumps(data, indent=2, ensure_ascii=False) + "\n")

def slug(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")[:40]

def all_options(data):
    return [(s, o) for s in data["slides"] for o in s["options"]]

def cmd_new(argv):
    if len(argv) < 2:
        bad('Usage: ./deck new CODE "Name" "one-line description"')
        info('e.g.  ./deck new C4 "Dark workbook" "Dark · formula bar + tabs"')
        sys.exit(1)
    code = argv[0].strip().upper()
    name = argv[1].strip()
    sub  = (argv[2].strip() if len(argv) > 2 else "")
    if not re.match(r"^[A-Z][0-9]+$", code):
        bad("CODE should look like C4 or D7 (a slide letter + a number). Got: %s" % code)
        sys.exit(1)
    letter = code[0]
    data = load()
    if any(o["code"] == code for _, o in all_options(data)):
        bad("%s already exists. Pick the next free number for slide %s." % (code, letter))
        sys.exit(1)
    slide = next((s for s in data["slides"] if s["slide"] == letter), None)
    if slide is None:
        have = ", ".join(s["slide"] for s in data["slides"])
        bad("Slide %s doesn't exist yet (have: %s)." % (letter, have))
        info("To start a brand-new section, add a slide block to slides.json by hand — see CLAUDE.md.")
        sys.exit(1)
    fname = "%s-%s.html" % (code, slug(name) or "option")
    fpath = os.path.join(ROOT, fname)
    if os.path.exists(fpath):
        bad("%s already exists on disk." % fname); sys.exit(1)
    with open(TEMPLATE) as f:
        body = f.read()
    body = body.replace("<title>Primer — new option</title>",
                        "<title>Primer — %s · %s</title>" % (code, name))
    with open(fpath, "w") as f:
        f.write(body)
    slide["options"].append(
        {"code": code, "file": fname, "name": name, "sub": sub, "recommended": False})
    save(data)
    ok("Created and listed %s%s%s  (slide %s — %s)" % (BOLD, fname, END, letter, slide["title"]))
    print()
    info("Next:")
    info('  1. Edit %s — build your slide inside the <section class="stage">.' % fname)
    info("  2. ./deck preview   then refresh the gallery to see it.")
    info('  3. ./deck publish "what you made"   to open a PR.')

def cmd_check(argv):
    problems = 0
    try:
        data = load()
    except Exception as e:
        bad("slides.json is not valid JSON: %s" % e); sys.exit(1)
    ok("slides.json is valid")
    listed = {}
    for s, o in all_options(data):
        for k in ("code", "file", "name"):
            if not o.get(k):
                bad("an option in slide %s is missing '%s'" % (s["slide"], k)); problems += 1
        if o["code"] in listed:
            bad("duplicate code %s" % o["code"]); problems += 1
        listed[o["code"]] = o["file"]
        fp = os.path.join(ROOT, o["file"])
        if not os.path.exists(fp):
            bad("%s points to %s, which is missing" % (o["code"], o["file"])); problems += 1
    referenced = set(listed.values())
    for fn in sorted(os.listdir(ROOT)):
        if OPTION_RE.match(fn) and fn not in referenced:
            bad("%s exists but isn't in slides.json (it won't show in the gallery)" % fn)
            info('    add it with one line, or run: ./deck new ...')
            problems += 1
    n = len(listed)
    if problems == 0:
        ok("%d options, all wired up" % n)
        print("\n%severything checks out%s" % (GREEN + BOLD, END))
    else:
        print("\n%s%d problem(s) to fix%s" % (RED + BOLD, problems, END))
        sys.exit(1)

if __name__ == "__main__":
    verb = sys.argv[1] if len(sys.argv) > 1 else ""
    rest = sys.argv[2:]
    if verb == "new":     cmd_new(rest)
    elif verb == "check": cmd_check(rest)
    else:
        bad("unknown verb: %s" % verb); sys.exit(1)
