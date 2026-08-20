# Deform

[![skills.sh installs](https://skills.sh/b/mickships/deform)](https://www.skills.sh/mickships/deform)

Deform stops AI writing patterns before they reach the page. It loads as a skill while Claude writes, so the prose comes out clean rather than getting cleaned up afterwards.

Nineteen banned forms, each with a replacement rule. Every example in the dictionary is a verbatim specimen from real Claude output, not an invented illustration.

## Before and after

Left column is real output. Right column is what the same sentence looks like written under the skill.

| Claude, unconstrained | Under Deform |
|---|---|
| The honest answer is that they mostly aren't in that fight, and you should say so plainly. | They aren't in that fight, because their distribution runs through carriers. |
| And the one genuine encroachment from Big Audio: Apple has been pushing spatial audio. | Apple has been pushing spatial audio, which threatens the premium tier. |
| "What drives you" — your honest, well-matched answer | How to answer "What drives you" |
| The honest vulnerability — name it, don't hide it | The business vulnerability: customer concentration |
| That's the complete, clean, ready-to-paste version with everything merged in the right order. | (nothing; the document was the answer) |

## Why constrain generation instead of correcting output

A rewrite can only remove what is on the page. It cannot recover the sentence that would have existed if the pattern had never been there.

Take the first row above. A post-hoc pass deletes the frame and leaves "They aren't in that fight." Correct, and still worse than the version that was never framed, because the frame was sitting in the slot where the reason belonged. Cutting it leaves a hole. Constraining generation makes the model reach for the cause instead. The same holds for headings, for lists that should have been prose, and for any form whose presence displaced something better.

The token argument runs alongside it. Correcting after the fact means a second pass that reads the whole draft back in and emits the whole draft again, so the cost of the correction scales with how much you wrote and repeats every time you write. Loading a constraint costs a fixed amount once. Deform's `SKILL.md` is roughly 3,000 tokens; a single 1,000-token document costs about 2,000 tokens to re-read and re-emit, before counting the rewriting skill itself. One document and the two approaches are close. Five documents in a session and the fixed cost has been paid once while the correction cost has been paid five times.

The rewrite approach still wins in one case, which is text Claude did not write. Deform has nothing to say about a colleague's draft until you ask it to deform that text explicitly.

## Install

With the [skills CLI](https://www.skills.sh):

```
npx skills add mickships/deform
```

On claude.ai: download this repo as a ZIP (green Code button, then Download ZIP) and upload it under Customize > Skills. Requires code execution enabled in Settings > Capabilities.

In Claude Code, manually:

```
git clone https://github.com/mickships/deform.git ~/.claude/skills/deform
```

Without installing anything, [`PREFERENCES.md`](PREFERENCES.md) holds a compressed subset that fits in a preferences field. Four of the nineteen forms are dropped to make it fit, so installing carries more than pasting does.

## Usage

Once enabled the skill applies to prose automatically. No invocation needed.

To point it at existing text:

```
Deform this: [paste text]
```

To check your own writing against it:

```
Which forms in the deform dictionary does this paragraph use?
```

## What it blocks

| # | Form | Specimen | Instead |
|---|------|----------|---------|
| 1 | Counted framing header | "Two things to note. First... Second..." | Head lists with the subject, never the count |
| 2 | Format meta-label | "Here's your full prep brief" | Show the content, name the subject |
| 3 | Negation pivot | "a hard performance lever, not a soft topic" | Assert the claim directly |
| 4 | Announcement transition | "Before I show you the file" | Start with the content |
| 5 | Significance label | "The takeaway:" | Show the consequence |
| 6 | Rule-of-three triplet | "the complete, clean, ready-to-paste version" | One word that does the work |
| 7 | Wrap-up restatement | "That's the complete version with everything merged" | End on the last substantive point |
| 8 | Em dash aside | "an elite architect — the world's foremost expert" | Commas, periods, parentheses, a colon |
| 9 | Emoji decoration | "## 🤖 Project Instructions" | Delete it |
| 10 | Bold-label bullet | "**Structured**: Use numbered steps" | Plain bullets or prose |
| 11 | Process signaling | "One important finding up front:" | Delete the signal, make the statement |
| 12 | Redundant qualifier | "merged in the right order" | Delete the modifier |
| 13 | Enumeration reflex | Two unrelated points rendered as bullets | Write it as prose |
| 14 | Concessive opener | "You're right, but I'm not doing it" | State the position, skip the softener |
| 15 | Candor frame | "The honest vulnerability", "The honest answer is" | Delete the word, give the cause |
| 16 | Delivery prescription | "and you should say so plainly" | Write the plain version |
| 17 | Imperative couplet | "name it, don't hide it" | Give the instruction once |
| 18 | Delayed subject | "And the one genuine encroachment: Apple has..." | Lead with the subject |
| 19 | Pre-sold heading | "'What drives you' — your honest answer" | Name the function |

Full definitions with replacement rules and boundary notes are in [`forms/active.md`](forms/active.md).

Bans target forms, not strings. "Three factors that shape the outcome" is banned as a shape, so rewriting it to "a trio of considerations" is the same violation. The dictionary also carries guards against overcorrection: lists and tables stay legal for genuinely parallel items, and prose that is visibly straining against the rules has failed differently rather than succeeded.

Five forms from the original seed set were cut for lack of evidence and sit unloaded in [`forms/watchlist.md`](forms/watchlist.md), restorable by copy-paste if a specimen appears. The cut includes the AI lexicon (delve, leverage, robust), which is a stronger tell for other vendors' models than for Claude.

## Make it yours

The dictionary is one file. `forms/active.md` carries the forms and the skill's name and description; `engine.md` carries application rules and nothing else. Swapping the dictionary changes what the skill is called, when it fires, and what it bans, without touching anything else.

`forms/example.md` is a working two-form dictionary about corporate jargon, shipped so you can see a swap before writing your own:

```
python3 build.py --dictionary forms/example.md --out /tmp/JARGONAUT.md
built /tmp/JARGONAUT.md as 'jargonaut': 2 forms, 39 lines
```

To build your own, copy that file, replace the forms, and run `python3 build.py`. The build refuses to emit a skill from a dictionary missing `name`, `description`, a required field on any form, or sequential numbering. Format rules are in [`forms/README.md`](forms/README.md).

## How it grows

Deform is generated from a corpus of specimens rather than assembled from taste. Sightings go verbatim into [`corpus/inbox.md`](corpus/inbox.md), without classification or debate at capture time, because capture that costs more than ten seconds stops happening. A periodic distill session ([`DISTILL.md`](DISTILL.md)) clusters accumulated captures into forms, and the maintainer promotes what has a workable replacement rule.

The dictionary is capped at 30 forms. Past that the loaded skill costs more context than it returns and forms start colliding, which shows up as stilted prose. The corpus underneath has no cap.

To contribute a specimen, see [CONTRIBUTING.md](CONTRIBUTING.md). No git knowledge needed; the GitHub web editor is enough.

## Relation to humanizer

[blader/humanizer](https://github.com/blader/humanizer) rewrites finished English text to remove AI tells, working from Wikipedia's "Signs of AI writing". Deform started from that list and diverged in three ways.

It runs at generation time rather than after, for the reasons above. Its forms are drawn from assistant-conversation output rather than from a guide to AI-written encyclopedia articles, which turns out to be a different genre; the largest cluster in this corpus is Claude annotating its own work, a category the article-focused list does not cover. And its dictionary is swappable by design, so the repo is a pipeline anyone can run on their own captures rather than a fixed list.

The two compose. Deform constrains what you write; humanizer cleans what someone else wrote.

## Repo layout

```
engine.md            application rules only. no forms, no name, no description
forms/active.md      the dictionary: forms plus the skill's identity. swap this
forms/example.md     a working two-form dictionary under a different name
forms/watchlist.md   forms parked for lack of evidence, not loaded
forms/README.md      dictionary format and the rules that make one work
build.py             engine + dictionary -> SKILL.md, with validation
corpus/inbox.md      raw captures, append-only
DISTILL.md           corpus -> dictionary
PREFERENCES.md       compressed subset for a preferences field
SKILL.md             generated, committed, do not edit
```

`SKILL.md` is committed so `npx skills add` works without anyone running a build.

## Version history

- 4.0.0: dictionary frontmatter carries the skill's `name` and `description`, so a swapped dictionary produces a differently named skill with its own trigger conditions. `engine.md` reduced to application rules. Added `forms/example.md` and frontmatter validation.
- 3.4.0: added form 19 (pre-sold heading).
- 3.3.0: added form 18 (delayed subject).
- 3.2.0: added form 17 (imperative couplet); widened form 15 to the word "honest" in any self-applied position.
- 3.1.0: added forms 15 (candor frame) and 16 (delivery prescription).
- 3.0.0: split the swappable dictionary from the invariant engine and added `build.py`. Audited every form against real Claude output: five unevidenced seed forms moved to the watchlist, emoji decoration added, all remaining forms given verbatim specimens.
- 2.x: forms 15 through 18 added from captures; capture-without-debate rule documented.
- 1.0.0: initial 14 forms, corpus and distill pipeline.

This README was written under the skill.

## License

MIT
