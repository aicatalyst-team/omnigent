# Formatting Review — v2 (Omnigent on OpenShift)

Reviewer: formatting (style, conventions, readability)
Draft reviewed: `drafts/v2.md`
Rubric: `references/reviewer-formatting.md`

## Scores

| Dimension | Weight | Raw | Weighted | Notes |
|---|---|---|---|---|
| Heading hierarchy | 1x | 10 | 10 | All 8 headings H2, sentence case, no H1, clean cascade |
| Code formatting | 1x | 8 | 8 | Real runnable code; 20 inline backtick spans + 5 fenced blocks (convert inline at finalization) |
| CTA placement | 2x | 5 | 10 | Substantive closing CTA now hyperlinked to the fork; still no top/mid CTA, no redhat.com links |
| SEO readiness | 1x | 6 | 6 | No H1/title in body; first paragraph now front-loads "Omnigent" + "orchestration layer" + "AI coding agents" |
| Link strategy | 1x | 5 | 5 | 1 real hyperlink (fork, github.com, not a competitor); no internal redhat.com links |
| Editorial compliance | 2x | 6 | 12 | Oxford commas clean; acronyms mostly expanded (UBI missed); product-name first mention + "Red Hat AI" inconsistency; contractions still sparse |
| Brand standards | 1x | 9 | 9 | Mermaid diagrams use Red Hat red (#EE0000) / blue (#0066CC) palette correctly |
| Word count | 1x | 10 | 10 | 1056 prose words, within 800-1300 tutorial range |

**Weighted total: 70 / 100**
**Normalized score: (70 / 100) * 10 = 7.0 / 10**

## Line-level feedback

### Headings (all verified sentence case, no H1, no skipped levels)

| Line | Heading | Verdict |
|---|---|---|
| 16 | `## What is Omnigent?` | OK — sentence case |
| 32 | `## Why it matters for OpenShift AI` | OK as case, but first mention of the product should be "Red Hat OpenShift AI" (see editorial) |
| 46 | `## Setting up for deployment` | OK |
| 61 | `## Containerizing for OpenShift` | OK |
| 100 | `## Deploying to the cluster` | OK |
| 142 | `## Running the PoC tests` | OK |
| 161 | `## What we learned` | OK |
| 176 | `## Try it yourself` | OK |

Non-sentence-case headings found: **0**. H1 in body: **0**. Skipped heading levels: **0**.

### Em dashes (max 1-2 per post, no spaces around them)

| Line | Text | Note |
|---|---|---|
| 1 | `<!-- CHANGELOG — removed during finalization` | The only em dash in the file. It sits inside the changelog comment that is removed during finalization, so the published body has 0. Strip the comment (or the dash) when finalizing. |

Em dashes in published body: **0**.

### Passive voice (active voice preferred)

| Line | Text | Note |
|---|---|---|
| 158-159 | "the last 2 confirm the built web UI and the login page **are being served**" | Present-continuous passive. Rewrite actively: "...and the last 2 confirm the server is serving the built web UI and the login page." |

True passive-verb instances: **1** (line 158). Otherwise the draft is consistently active.

### Contractions (use aggressively)

Only one true contraction in the body ("you'd", line 173); the rest are possessives (developer's, file's, namespace's, fork's). The changelog claims contractions were added, but the running text is still formal.

Missed opportunities:

| Line | Current | Suggested |
|---|---|---|
| 63 | "we did not have to invent" | "we didn't have to invent" |
| 81 | "the image does not use" | "the image doesn't use" |
| 180 | "a project you are curious about" | "a project you're curious about" |
| 20 | "It is an open-source 'meta-harness'" | "It's an open-source 'meta-harness'" (softer — optional) |
| 48 | "It is a monorepo" | "It's a monorepo" (softer — optional) |

Clear misses: **3** (lines 63, 81, 180); softer "It is" instances: **2**.

### Numerals in running text (rule: "3 tiers" not "three tiers")

| Line | Current | Suggested |
|---|---|---|
| 54 | "**Two** things stood out." | "**2** things stood out." |
| 168 | "took **one** iteration to match" | "took **1** iteration to match" |
| 19 | "tied to **one** machine and **one** login" | Borderline — rhetorical "one" (= a single); acceptable, but "1" is stricter |

(Note: "First,"/ "Second," on lines 54/56 are ordinals and correctly left as words. "a single pod"/"A single Deployment" are adjectival and fine.)

Clear violations: **2** (lines 54, 168); borderline: **1** (line 19).

### Code formatting (no backticks in final output)

20 inline code spans across lines 63, 66, 80, 82, 84, 85, 98, 105, 108, 109, 126, 127, 167, 168, 179, 180, plus 5 fenced blocks (Dockerfile 70-77, two Mermaid diagrams 87-93 & 130-137, YAML 112-124, bash 148-154). The code is real and runnable — actual Dockerfile stage names, real SCC fields, real endpoints, real branch names — no pseudocode. All inline backticks must be converted to the CMS's monospace markup during finalization; the fences (incl. Mermaid) are fine to keep.

### CTA placement (weight 2x)

- Top CTA: **missing**. The opening "What is Omnigent?" hook never points readers toward a resource or the fork.
- Mid CTA: **missing**.
- Closing CTA: **present and good** (lines 176-183, "Try it yourself" + AutoPoC), matching the abstract's stated CTA. Improvement over v1: the fork is now a real hyperlink, `[aicatalyst-team/omnigent](https://github.com/aicatalyst-team/omnigent)`.
- Linking: the fork link points to github.com, not redhat.com; no other links.

Fix: add one line near the top linking the fork or the PoC report, and point the AutoPoC mention at a redhat.com URL.

### SEO readiness

- No title exists in the draft (no H1), so "keyword in title" cannot be satisfied and there is no 50-60 char title to check.
- First paragraph now front-loads the core keywords: "Omnigent" (line 20), "common orchestration layer over the AI coding agents" (line 21) — a clear improvement over v1.
- Fix: add an H1 title of 50-60 characters containing "Omnigent" and "OpenShift", e.g. "Deploying Omnigent on Red Hat OpenShift AI" (40 chars — room to extend, e.g. "Deploying Omnigent, an Agent Orchestration Layer, on OpenShift AI" — trim to 50-60).

### Link strategy

One real hyperlink (the fork, github.com) — not a competitor link (good). No internal redhat.com links. Add: the PoC report, an OpenShift AI landing page, and (optionally) the AutoPoC repo.

### Product name compliance

| Line | Issue |
|---|---|
| 32 / 34 | First mention of the product is the shortened "OpenShift AI" (heading) / "OpenShift" (body). Rule 4 requires the full "Red Hat OpenShift AI" on first mention. Put the full name in the first body paragraph of that section. |
| 37 | "the agentic AI direction in **Red Hat AI**" uses the umbrella brand, not the specific product "Red Hat OpenShift AI". Align with the abstract's product list. |
| elsewhere | "OpenShift" alone is fine after first mention. "RHOAI" never appears — good. |

### Acronym expansion (first use)

| Acronym | First mention | Expanded? |
|---|---|---|
| UI | line 28 ("web user interface (UI)") | Yes |
| LLM | line 42 ("large language model (LLM)") | Yes |
| SDK | line 49 ("software development kit (SDK)") | Yes |
| PoC | line 50 ("proof of concept (PoC)") | Yes |
| TLS | line 103 ("Transport Layer Security (TLS)") | Yes |
| CI | line 166 ("continuous integration (CI)") | Yes |
| UBI | line 54 ("a UBI 9 Dockerfile") | **No** — expand to "Universal Base Image (UBI)" |

Big improvement over v1 (6 unexpanded → 1).

### Marketing tropes and filler transitions

- "game-changer", "cutting-edge", "seamless", "powerful", "revolutionary", "leverage", "unlock": **0 found**. ("meta-harness" is the project's own term — legitimate, not a trope.)
- "Moreover", "Furthermore", "Additionally", "In conclusion": **0 found**.

Clean on this axis.

## Editorial compliance checklist

- [x] Sentence case headings — all 8 pass
- [x] Oxford commas — "a browser, a phone, or a whole team" (22); "Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and agents" (26); "the test suites, docs, and deploy directories" (81); "analyze, containerize on UBI, build, deploy, and test" (182)
- [ ] No backticks — 20 inline spans remain (convert at finalization)
- [ ] Full product name on first mention — "OpenShift AI"/"OpenShift" at lines 32/34 lack "Red Hat"; "Red Hat AI" (37) ≠ "Red Hat OpenShift AI"
- [x] Never "RHOAI" — absent
- [x] Lowercase component descriptors — no violations found
- [x] No H1 in body — absent
- [ ] Expand acronyms on first use — 1 unexpanded (UBI)
- [ ] Contractions aggressively — 3 clear + 2 soft missed opportunities
- [ ] Numerals in running text — 2 clear + 1 borderline word-numbers
- [x] No em dashes (max 1-2) — 1, inside the removable changelog comment

## Summary

Solid improvement over v1 (6.5 → 7.0). The draft reads well: clean heading cascade, active voice, no filler transitions, no marketing tropes, brand-colored diagrams, in-range word count, and the acronym/numeral cleanup from the v1 round largely landed (6→1 unexpanded, 4→2 word-numbers). The fork is now a real hyperlink. The two 2x-weighted dimensions still cap the score:

1. **CTA (2x)** — everything still funnels to a single closing CTA; no top or mid CTA, and the only link is github.com, not redhat.com.
2. **Editorial (2x)** — first-mention product name still lacks "Red Hat", "Red Hat AI" diverges from the product "Red Hat OpenShift AI", UBI is unexpanded, and contractions remain sparse despite the changelog claiming they were added.

Remaining mechanical fixes: expand UBI at line 54, add "Red Hat" to the first product mention, align line 37 to "Red Hat OpenShift AI", convert "Two things" (54) and "one iteration" (168) to numerals, add the 3 missed contractions, flip line 158's passive, add a top CTA + a redhat.com link, and add an H1 title. None require restructuring.

**Normalized score: 7.0 / 10**
