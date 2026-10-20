# Formatting Review — v1 (Omnigent on OpenShift)

Reviewer: formatting (style, conventions, readability)
Draft reviewed: `drafts/v1.md`
Rubric: `references/reviewer-formatting.md`

## Scores

| Dimension | Weight | Raw | Weighted | Notes |
|---|---|---|---|---|
| Heading hierarchy | 1x | 10 | 10 | All 8 headings H2, sentence case, no H1, clean cascade |
| Code formatting | 1x | 7 | 7 | Real runnable code, but 28 inline backtick spans remain |
| CTA placement | 2x | 5 | 10 | Substantive closing CTA only; no top/mid CTA, no redhat.com links |
| SEO readiness | 1x | 5 | 5 | No title/H1 at all; keywords present in first paragraph |
| Link strategy | 1x | 4 | 4 | Zero hyperlinks in the post |
| Editorial compliance | 2x | 5 | 10 | Oxford commas clean; product name, acronyms, contractions, numerals need work |
| Brand standards | 1x | 9 | 9 | Mermaid themes use Red Hat red (#EE0000) palette correctly |
| Word count | 1x | 10 | 10 | 1078 words, within 800-1300 tutorial range |

**Weighted total: 65 / 100**
**Normalized score: (65 / 100) * 10 = 6.5 / 10**

## Line-level feedback

### Headings (all verified sentence case, no H1, no skipped levels)

| Line | Heading | Verdict |
|---|---|---|
| 6 | `## What is Omnigent?` | OK — sentence case |
| 20 | `## Why it matters for OpenShift AI` | OK as case, but first mention of the product should be "Red Hat OpenShift AI" (see editorial) |
| 33 | `## Setting up for deployment` | OK |
| 47 | `## Containerizing for OpenShift` | OK |
| 75 | `## Deploying to the cluster` | OK |
| 99 | `## Running the PoC tests` | OK |
| 115 | `## What we learned` | OK |
| 130 | `## Try it yourself` | OK |

Non-sentence-case headings found: **0**. H1 in body: **0**. Skipped heading levels: **0**.

### Em dashes (max 1-2 per post, no spaces around them)

| Line | Text | Note |
|---|---|---|
| 1 | `<!-- CHANGELOG — removed during finalization` | The only em dash in the file. It sits inside the changelog comment that is removed during finalization, so the published body has 0. Acceptable, but strip the comment or the dash in v2. |

Em dashes in published body: **0**.

### Passive voice

The draft is overwhelmingly active. Instances found:

| Line | Text | Note |
|---|---|---|
| 109 | "confirming the auth and feature subsystems **wired up**" | Reduced passive ("that were wired up"). Rewrite: "confirming the auth and feature subsystems came up wired" or attach to an active subject: "the server confirmed the auth and feature subsystems are wired up." |
| 110 | "served the **built** web UI" | Participial adjective, not a finite passive — acceptable, listed for completeness. |

True passive-verb instances: **1** (line 109).

### Contractions (use aggressively)

Missed opportunities:

| Line | Current | Suggested |
|---|---|---|
| 35 | "It is a monorepo" | "It's a monorepo" |
| 49 | "we did not have to write" | "we didn't have to write" |
| 59 | "a package that is not in the UBI 9 repositories" | "a package that isn't in the UBI 9 repositories" |
| 120 | "not code problems" | "weren't code problems" |
| 127 | "you would want Postgres" | "you'd want Postgres" |
| 136 | "it will walk the same path" | "it'll walk the same path" |

### Numerals in running text (rule: "3 tiers" not "three tiers")

| Line | Current | Suggested |
|---|---|---|
| 9 | "locking into one tool" | "1 tool" (borderline — "one" is often left as a word) |
| 52 | "assembles the two into a non-root image" | "assembles both" or "assembles the 2" |
| 55 | "We made two small changes" | "We made 2 small changes" |
| 80 | "fits in one pod" | "fits in 1 pod" (borderline) |
| 102 | "It exercised five pre-auth endpoints" | "It exercised 5 pre-auth endpoints" |
| 113 | "All five scenarios passed" | "All 5 scenarios passed" |
| 119 | "The two things that cost us time" | "The 2 things that cost us time" |
| 126 | "kept the deployment to one pod" | "kept the deployment to 1 pod" (borderline) |

Clear violations: 4 (lines 55, 102, 113, 119); borderline "one/both" instances: 4.

### Code formatting (no backticks in final output)

28 inline code spans across lines 49, 52, 53, 56, 59, 70, 73, 79, 80, 83, 84, 85, 86, 97, 105, 107, 108, 110, 111, 121, 122, 132, 133, 134, plus 2 fenced blocks (mermaid, lines 64-70 and 90-97). The code itself is real and runnable (actual Dockerfile stage names, real SCC fields, real endpoints) — no pseudocode. All inline backticks must be converted to the CMS's monospace markup during finalization. Mermaid fences are fine to keep.

### CTA placement (weight 2x)

- Top CTA: **missing**. The opening "What is Omnigent?" section never points readers toward a resource or the fork.
- Mid CTA: **missing**.
- Closing CTA: **present and good** (lines 130-137, "Try it yourself" + AutoPoC), matching the abstract's stated CTA.
- Linking: the fork is cited as plain text (`aicatalyst-team/omnigent`, line 132) rather than a hyperlink; no redhat.com links anywhere.

Fix: add one line near the top linking the fork or the PoC report, and hyperlink the fork reference and any AutoPoC mention to redhat.com.

### SEO readiness

- No title exists in the draft (no H1), so "keyword in title" cannot be satisfied and there is no 50-60 char title to check.
- First paragraph does carry the keywords: Omnigent, orchestration, AI coding agents, OpenShift (via later headings).
- Fix: add an H1 title of 50-60 characters containing "Omnigent" and "OpenShift", e.g. "Deploying Omnigent, an agent orchestration layer, on OpenShift AI" (65 chars — trim to fit).

### Link strategy

Zero hyperlinks in the post. No competitor links (good — Claude Code, Codex, Cursor, OpenCode are mentioned by name only). Add internal redhat.com links: the fork, the PoC report, and an OpenShift AI landing page.

### Product name compliance

| Line | Issue |
|---|---|
| 20 | First mention of the product is the shortened "OpenShift AI" (in a heading). Rule 4 requires the full "Red Hat OpenShift AI" on first mention. Move the full name into the first body paragraph (line 27 area already says "Red Hat AI" — combine: "the agentic AI direction in Red Hat AI, starting with Red Hat OpenShift AI"). |
| 27 onward | "OpenShift" alone is fine after first mention. "RHOAI" never appears — good. |

### Acronym expansion (first use)

| Acronym | First mention | Expanded? |
|---|---|---|
| UI | line 13 ("web UI") | No — expand to "user interface (UI)" |
| LLM | line 31 ("LLM gateway") | No — expand to "large language model (LLM)" |
| PoC | line 37 ("For the PoC") | No — expand to "proof of concept (PoC)" |
| SDK | line 36 ("Python SDK") | No — expand to "software development kit (SDK)" |
| TLS | line 78 ("over TLS") | No — expand to "Transport Layer Security (TLS)" |
| CI | line 121 ("CI workflows") | No — expand to "continuous integration (CI)" |
| YAML | line 10 | Borderline — commonly treated as a proper noun; optional |

### Marketing tropes and filler transitions

- "game-changer", "cutting-edge", "seamless", "powerful", "revolutionary", "leverage", "unlock": **0 found**. ("harness" appears once, line 8, as the project's own term "meta-harness" — legitimate, not a trope.)
- "Moreover", "Furthermore", "Additionally", "In conclusion": **0 found**.

Clean on this axis.

## Editorial compliance checklist

- [x] Sentence case headings — all 8 pass
- [x] Oxford commas — "Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and agents" (line 10); "the plan, test script, and report" (line 133); "analyze, containerize on UBI, build, deploy, and test" (lines 135-136)
- [ ] No backticks — 28 inline spans remain (convert at finalization)
- [ ] Full product name on first mention — "OpenShift AI" at line 20 lacks "Red Hat"
- [x] Never "RHOAI" — absent
- [x] Lowercase component descriptors — no violations found
- [x] No H1 in body — absent
- [ ] Expand acronyms on first use — 6 unexpanded (UI, LLM, PoC, SDK, TLS, CI)
- [ ] Contractions aggressively — 6 missed opportunities
- [ ] Numerals in running text — 4 clear + 4 borderline word-numbers
- [x] No em dashes (max 1-2) — 1, inside the removable changelog comment

## Summary

The draft reads well: clean heading cascade, active voice, no filler transitions, no marketing tropes, brand-colored diagrams, and a word count squarely in range. The gaps are mechanical and concentrated in three areas: (1) editorial micro-rules — first-mention product name, 6 unexpanded acronyms, 6 missed contractions, 4 word-numbers; (2) CTA/linking — everything funnels to one unlinked closing CTA, with zero hyperlinks; (3) SEO — no title exists. None of these require restructuring; a single pass with the checklist above should lift the editorial and CTA scores substantially.

**Normalized score: 6.5 / 10**
