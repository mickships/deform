# Dictionaries

`active.md` is the dictionary. It is the only file that encodes taste. Everything else in this repo is machinery that works with any dictionary you put here.

To make Deform yours, replace `active.md` with your own forms and run `python3 build.py`. The skill is regenerated around your dictionary, the guards and application rules stay intact, and nothing else needs touching.

## Format

A dictionary is one file with frontmatter and a list of forms. The frontmatter carries the skill's identity, so a swapped dictionary produces a differently named skill with its own trigger conditions:

```
---
name: jargonaut                      # required. the skill's name
description: Use when ...            # required. decides when the skill fires
version: 0.1.0
title: Jargonaut                     # optional. defaults from name
intro: One line under the title.     # optional
---
```

`description` is the field an agent reads to decide whether to load the skill, so write it for your dictionary's scope. A dictionary of legal-drafting forms whose description still says "any English prose" will fire on holiday emails.

Each form is then one block:

```
### N. Name of the form
Form: one sentence describing the abstract shape, not a specific sentence.
Examples: "verbatim specimen" / "verbatim specimen" / "verbatim specimen"
Instead: what to write in its place.
Boundary: optional. Only when the form could be confused with another one in the dictionary.
```

`Form`, `Examples`, and `Instead` are required, forms must be numbered from 1 without gaps, and the frontmatter must carry `name` and `description`. The build fails on any of these rather than emitting a broken skill.

`example.md` in this folder is a working two-form dictionary with a different name and description. Build it with `python3 ../build.py --dictionary forms/example.md --out /tmp/JARGONAUT.md` to see the swap before writing your own.

## Rules that make a dictionary work

Name the shape, not the string. "Counted framing header" generalizes; "ban the phrase 'three things that'" teaches the model to write "a trio of considerations" instead. A form is a shape a reader could recognize in text they have never seen.

Every form needs an `Instead`. A ban with no replacement produces a gap, and the model fills gaps with something worse. If you cannot write the replacement, the form is not ready.

Examples should be verbatim specimens from real output, and each should show a different surface variant. Three examples of the same shape teach less than three examples of different shapes sharing one deep structure. Cut any example that duplicates a shape already covered.

Keep the dictionary under about 30 forms. Past that, the loaded skill costs more context than it returns and forms start colliding, which shows up as overcorrected, stilted prose. If a new form must enter at the cap, the weakest existing one leaves.

Add a `Boundary` line whenever two forms could be confused. It is the cheapest defense against a dictionary that slowly turns into near-duplicates.

## Where forms come from

Captures go to `../corpus/inbox.md` verbatim, without discussion. `../DISTILL.md` is the procedure that turns accumulated captures into dictionary entries. That separation is the whole design: capture has to be frictionless, and classification has to be deliberate. Doing both at once produces either a corpus nobody adds to or a dictionary full of one-off irritations.

`watchlist.md` holds forms that are plausible but have no specimen. Nothing there is loaded by the skill. It exists so a form can be parked rather than deleted, and restored the moment a capture turns up.
