---
description: Deform: turn accumulated corpus captures into dictionary entries, rebuild, and publish
---

Run the procedure in `DISTILL.md` against the current contents of `corpus/inbox.md`.

Order of operations, and do not reorder them:

1. Read `DISTILL.md`, `corpus/inbox.md`, and `forms/active.md`.
2. Work through the procedure. Cluster captures, promote what qualifies, update examples, add boundary lines where two forms could be confused.
3. Bump `version` in the `forms/active.md` frontmatter.
4. Run `python3 build.py`. If it fails, fix the dictionary and run it again. Do not commit while the build is failing, and do not edit `SKILL.md` to make the build pass.
5. Regenerate `PREFERENCES.md` and confirm the pasteable block is under 1500 characters.
6. Add a line to the Version history section of `README.md`, and update the forms table there if the dictionary changed.
7. Archive processed entries to `corpus/archive/YYYY-MM.md` and leave the inbox header in place.
8. Commit and push.
9. Report: forms added, forms updated, candidates left on watch, entries archived, new version number.

Two standing constraints from the maintainer:

- The maintainer's taste is the specification. A specimen they recorded belongs in the dictionary; whether it is also a general writing fault, or whether it fits the existing taxonomy neatly, is not grounds to drop it.
- Seed forms carry no specimens and have no standing against observed evidence. When a capture conflicts with an existing category, the category is what is under review.

After pushing, remind the maintainer in one line that the installed copy is separate and needs `npx skills update`.
