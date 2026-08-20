---
description: Deform: record a captured specimen of AI slop into the corpus, verbatim and without discussion
---

Append the following specimen to `corpus/inbox.md`, then stop.

$ARGUMENTS

Rules:

- Verbatim. Do not clean, trim, or paraphrase the specimen.
- Do not classify it, do not name which form it matches, do not say whether it is already covered, do not argue about whether it belongs. Classification happens at distill time and nowhere else.
- Format the entry as:

```
## YYYY-MM-DD
> the specimen, verbatim
note: (only if the user supplied one)
```

- Use today's date. Ask nothing. The specimen carries its own context, and the distill reads every entry anyway.
- Commit with the message `corpus: add specimen`. Do not push, do not run the build, do not touch `forms/active.md` or `SKILL.md`.
- Then report the running count in one line: `logged (N in inbox)`.
- If N is 20 or more, add one further line: `ready to distill`. Do not start the distill.
