# Working in this repo

Deform is a skill generated from a corpus of specimens. Two workflows run here, and they must stay separate.

**Capture** is high frequency and must be near-free. A specimen arrives, it goes into `corpus/inbox.md` verbatim, and nothing else happens. No classification, no discussion of whether it is already covered, no argument about whether it deserves a form. Use `/slop`.

**Distill** is low frequency and deliberate. Roughly every twenty captures, accumulated specimens become dictionary entries. Use `/distill`.

Doing both at once is the failure mode this structure exists to prevent: it produces either a corpus nobody adds to, because every capture turns into a debate, or a dictionary full of one-off irritations.

## Generated files

`SKILL.md` is built from `engine.md` plus `forms/active.md` by `build.py`. Never edit it by hand; the next build erases the change. Edit the dictionary and rebuild.

`PREFERENCES.md` is a hand-compressed subset regenerated at distill time. It has a hard 1500-character budget for the pasteable block.

## The dictionary contract

`forms/active.md` carries the forms and the skill's `name` and `description`. `engine.md` carries application rules and nothing else. This split is what lets someone swap in their own dictionary; keep identity and taste out of the engine.

Every form needs `Form:`, `Examples:`, and `Instead:`. Forms are numbered from 1 without gaps. The cap is 30. `build.py` enforces all three and refuses to write output otherwise.
