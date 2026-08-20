# Distill procedure

Run every ~20 inbox entries or monthly, whichever comes first. Open this repo in Claude Code (or paste the relevant files into a claude.ai chat) and give Claude this file as the instruction.

## Steps

1. Read `corpus/inbox.md` and `forms/active.md`. Never edit `forms/active.md`; it is generated.
2. For each inbox entry, either match it to an existing form in `forms/active.md` or cluster it with other unmatched entries into a candidate form. A candidate is an abstract shape ("counted framing header"), never a literal sentence.
3. Promotion rule: a candidate enters `forms/active.md` only with 3 or more independent captures (different sessions or sources). Below 3, it stays in the corpus as a watch item.
   - Seeding exception: the maintainer may add a form on a single capture when the form is unambiguous and has a workable replacement rule. This is how the initial set was built. Contributed captures always go through the 3-capture bar; the exception is not available for forms proposed by others, and every seeded form still gets a corpus entry as evidence.
4. For matched entries, add the capture to the form's examples in `forms/active.md` when it shows a surface variant the existing examples do not already cover. Cap examples by variety, not by count: keep every distinct surface shape, cut any example that teaches the same shape twice. Quote the offending fragment in `forms/active.md`, not the surrounding paragraph; full specimens belong in `corpus/`.
5. Every form must have an "Instead" rule. If you cannot write one, the form is not ready.
6. Enforce the caps: 30 forms maximum, and `forms/active.md` stays under roughly 250 lines. At the cap, a new form displaces the weakest existing one (fewest recent captures).
7. Bump `version` in the `forms/active.md` frontmatter (minor version for new or changed forms, patch for example tweaks) and add a line to the Version history section of `README.md`.
8. Regenerate `PREFERENCES.md`: the top 10 forms, one line each, total under 1,500 characters, suitable for pasting into claude.ai user preferences.
9. Run `python3 build.py` to regenerate `SKILL.md`, and commit the result. The build validates required fields, numbering, and the form cap; a failed build means the dictionary is malformed, not that the check is wrong.
10. Move processed inbox entries to `corpus/archive/YYYY-MM.md`. Leave the inbox header in place.
11. Report: forms added, forms updated, candidates on watch, entries archived.

## Capture rules

- Captures are recorded verbatim on receipt, without discussion, classification, or objection. Sorting and any disagreement happen in the distill session, never at capture time.
- The maintainer's taste is the specification. A form the maintainer finds annoying belongs in the skill; whether it is also a general writing fault, or whether it fits the existing taxonomy, is a question for the distill, not a reason to decline the capture.
- When a capture conflicts with an existing category, the category is the thing under review. Seed forms carry no specimens and have no standing against observed evidence.

## Rules

- Never delete raw captures; archive them. They are the evidence base and the contribution surface.
- Do not invent forms without captures. A form with no specimen belongs in `forms/watchlist.md`, not in the dictionary.
- Watch for overcorrection reports: if applying the skill produces stilted output, the fix is a better "Instead" rule, not more bans.
