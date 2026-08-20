---
description: Record a captured specimen of AI slop into the corpus, verbatim and without discussion
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
source: claude.ai | claude-desktop | claude-mobile | claude-code | claude-design | other
note: (only if the user supplied one)
```

- Use today's date. If the user did not say which surface it came from, ask once, in one short line, and nothing else. Source matters: the corpus already shows document-writing producing different forms than chat replies, and that signal is lost if the field is guessed.
- Commit with the message `corpus: add specimen`. Do not push, do not run the build, do not touch `forms/active.md` or `SKILL.md`.
- Then report the running count in one line: `logged (N in inbox)`.
- If N is 20 or more, add one further line: `ready to distill`. Do not start the distill.
