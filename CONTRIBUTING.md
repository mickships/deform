# Contributing

Deform grows from specimens, real AI-written sentences captured in the wild. You contribute by adding captures, and the maintainer promotes recurring shapes into the skill.

## What counts as a specimen

- A verbatim sentence or short passage written by an AI (Claude or otherwise) in English.
- It shows a recurring *shape*, a pattern you have seen more than once, rather than a one-off bad sentence.
- No personal information, no confidential content. Trim identifying context before submitting.

## How to submit (no git needed)

1. Open [`corpus/inbox.md`](corpus/inbox.md) on GitHub.
2. Click the pencil icon (Edit this file). GitHub creates a fork for you automatically.
3. Add your entry at the bottom in this format:

```
## 2026-08-17
> the offending sentence, verbatim
```

4. Click "Propose changes", then "Create pull request". Done.

One entry per sighting. If you have five captures of the same shape from five different sessions, submit five entries; independent occurrences are exactly what earns promotion.

## What happens next

The maintainer runs the distill procedure ([`DISTILL.md`](DISTILL.md)) periodically. A shape enters [`SKILL.md`](SKILL.md) once it has 3 or more independent captures and a workable replacement rule. Everything else stays in the corpus as evidence.

## Ground rules

- Do not open PRs against `SKILL.md` directly; it is generated from the corpus.
- Arguments about whether a form deserves banning are settled with specimens, not opinions. Bring captures.
- Captures are never argued with on arrival. If a specimen is real AI output and the submitter finds it grating, it gets recorded. Whether it becomes its own form, folds into an existing one, or stays in the corpus is decided later, in batch.
- If the skill makes prose worse in some situation, open an issue with a before and after. The fix is usually a better "Instead" rule, and that feedback is as valuable as a new capture.
