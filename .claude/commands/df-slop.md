---
description: "Deform: record a captured specimen of AI slop into the corpus, verbatim and without discussion"
---

Record the following capture in `corpus/inbox.md`, then stop.

$ARGUMENTS

Parse the argument into two parts:

- **The specimen.** Text in quotes. If nothing is quoted, the whole argument is the specimen and there is no note.
- **The note.** Anything the user wrote outside the quotes. Optional. Usually their own diagnosis of what is wrong with the specimen.

Rules:

- Record the specimen verbatim. Do not clean, trim, or paraphrase it.
- Record the note verbatim as well. Do not summarise it, do not rephrase it, do not correct it, do not argue with it. The maintainer's reading of a specimen outranks yours, and the distill weighs it accordingly.
- Add nothing of your own. Do not classify the specimen, do not name which form it matches, do not say whether it is already covered, do not assess whether it deserves a form. That happens at distill time and nowhere else. This rule binds you, not the user; their note is exactly the commentary you are forbidden to supply.
- Format the entry as:

## YYYY-MM-DD
> the specimen, verbatim
note: the user's note, verbatim (omit the line entirely if there was none)

- Use today's date. Ask nothing.
- Commit with the message `corpus: add specimen`. Do not push, do not run the build, do not touch `forms/active.md` or `SKILL.md`.
- Then report the running count in one line: `logged (N in inbox)`.
- If N is 20 or more, add one further line: `ready to distill`. Do not start the distill.
