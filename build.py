#!/usr/bin/env python3
"""Assemble a skill from an invariant engine and a swappable dictionary.

    python3 build.py                                  # build forms/active.md
    python3 build.py --dictionary forms/mine.md       # build your own
    python3 build.py --dictionary forms/mine.md --out MINE.md

The dictionary supplies both the forms and the skill's identity (name,
description, title). The engine supplies only application rules. Swapping the
dictionary therefore changes everything about the skill except how forms are
applied. No dependencies.
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
CAP = 30
LINE_BUDGET = 250
REQUIRED_FIELDS = ("Form:", "Examples:", "Instead:")
REQUIRED_META = ("name", "description")


def split_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    _, raw, body = text.split("---", 2)
    meta = {}
    for line in raw.strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, body.lstrip()


def parse_forms(text):
    blocks = re.split(r"^### ", text, flags=re.M)[1:]
    return [("### " + b).rstrip() for b in blocks]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dictionary", default="forms/active.md")
    ap.add_argument("--engine", default="engine.md")
    ap.add_argument("--out", default="SKILL.md")
    args = ap.parse_args()

    engine = (ROOT / args.engine).read_text()
    engine = re.sub(r"^<!--.*?-->\s*", "", engine, flags=re.S)

    meta, dictionary = split_frontmatter((ROOT / args.dictionary).read_text())
    forms = parse_forms(dictionary)
    errors, warnings = [], []

    for field in REQUIRED_META:
        if not meta.get(field):
            errors.append(f"dictionary frontmatter is missing '{field}'")

    if not forms:
        errors.append(f"no forms found in {args.dictionary}")

    for form in forms:
        title = form.splitlines()[0][4:].strip()
        for field in REQUIRED_FIELDS:
            if field not in form:
                errors.append(f"form '{title}' is missing a '{field}' line")

    numbers = [int(m.group(1)) for f in forms if (m := re.match(r"### (\d+)\.", f))]
    if numbers != list(range(1, len(forms) + 1)):
        errors.append(f"forms must be numbered 1..{len(forms)} in order; found {numbers}")

    if len(forms) > CAP:
        errors.append(f"{len(forms)} forms exceeds the cap of {CAP}")

    if errors:
        print("build failed:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    name = meta["name"]
    title = meta.get("title", name.title())
    intro = meta.get("intro", "A dictionary of banned writing forms with replacement rules.")

    frontmatter = (
        "---\n"
        f"name: {name}\n"
        f"description: {meta['description']}\n"
        "metadata:\n"
        f"  version: {meta.get('version', '0.1.0')}\n"
        "---\n"
    )

    maintenance = (
        "## Maintenance\n\n"
        "This file is generated. Do not edit it directly.\n\n"
        f"The dictionary lives in `{args.dictionary}` and carries both the forms and this "
        "skill's name and description; it is the only file that encodes taste. `engine.md` "
        "holds application rules and nothing else. Captures go to `corpus/inbox.md` verbatim, "
        "and `DISTILL.md` turns them into dictionary entries. Rebuild with "
        f"`python3 build.py --dictionary {args.dictionary}`.\n"
    )

    out = "\n".join([
        frontmatter,
        f"# {title}",
        "",
        intro,
        "",
        engine.rstrip(),
        "",
        "\n\n".join(forms),
        "",
        maintenance,
    ])
    (ROOT / args.out).write_text(out)

    n_lines = len(out.splitlines())
    if n_lines > LINE_BUDGET:
        warnings.append(f"{n_lines} lines exceeds the {LINE_BUDGET}-line budget")
    if len(forms) > CAP * 0.8:
        warnings.append(f"{len(forms)} forms is near the cap of {CAP}")

    print(f"built {args.out} as '{name}': {len(forms)} forms, {n_lines} lines")
    for w in warnings:
        print(f"  warning: {w}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
