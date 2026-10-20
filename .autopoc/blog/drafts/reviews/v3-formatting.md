# Formatting Review — v3 (Omnigent on OpenShift)

Reviewer: formatting (style, conventions, readability)
Draft reviewed: `drafts/v3.md`

## Scores

| Dimension | Weight | Raw (1-10) | Weighted | Notes |
|---|---|---|---|---|
| Heading hierarchy | 1x | 10 | 10 | All H2, sentence case, no H1, no skipped levels |
| Code formatting | 1x | 7 | 7 | Real runnable blocks; 21 inline backtick spans violate "no backticks" |
| CTA placement | 2x | 6 | 12 | Mid (roadmap pointer) + closing CTA present; no near-top CTA; CTA not linked to redhat.com |
| SEO readiness | 1x | 6 | 6 | No title in file; "Omnigent" in para 1 but "OpenShift" absent until section 2 heading |
| Link strategy | 1x | 7 | 7 | 1 redhat.com link (UBI), 1 GitHub fork link, no competitor links; AutoPoC mention unlinked |
| Editorial compliance | 2x | 7 | 14 | Oxford commas clean; UBI + YAML unexpanded on first use; 5 missed contractions; 2 word-numbers |
| Brand standards | 1x | 9 | 9 | All 3 mermaid diagrams use Red Hat theme (#EE0000 red, #0066CC blue, #6A6E73 gray) |
| Word count | 1x | 10 | 10 | ~1,138 prose words, within 800-1300 tutorial band |

**Weighted total: 75 / 100**
**Normalized: (75 / 100) * 10 = 7.5**

## Line-level feedback

- Line 1: Em dash in the changelog HTML comment ("CHANGELOG — removed during finalization"). Acceptable if the comment is stripped in finalization; strip it in v4 so no em dash survives anywhere in the file.
- Line 25: "agents you define yourself in YAML" — YAML is an acronym; expand on first use, e.g. "YAML (Yet Another Markup Language) agents" or at minimum "YAML configuration files".
- Line 60: "Red Hat OpenShift AI" — correct official name on first mention. Good.
- Line 76: "It is a monorepo" — missed contraction; use "It's".
- Line 82: "Two things stood out" — word-number; use "2 things stood out".
- Line 82: "ships a UBI 9 Dockerfile" — UBI first use, not yet expanded (expansion doesn't appear until line 113). Expand here: "a Red Hat Universal Base Image (UBI) 9 Dockerfile".
- Line 91: "we did not have to invent" — missed contraction; use "didn't".
- Line 93: "Four of them feed the server image" — word-number; use "4 of them".
- Line 96: "target we did not need" — missed contraction; use "didn't".
- Line 112: "a package that is not in the Red Hat Universal Base Image (UBI) 9 repositories" — (a) missed contraction: "that's not"; (b) if UBI is expanded on line 82 instead, this becomes the short form and should drop the parenthetical.
- Line 119: "pushes to Quay" — first prose mention of the product; use "Red Hat Quay" on first mention, then "Quay" after.
- Line 136: "The 4 stages that feed the server image" — numeral, good (consistent with the line 93 fix).
- Lines 216-222 (closing CTA): "Try it yourself" is a strong imperative close, but the AutoPoC mentions (lines 219, 222) are unlinked. Link AutoPoC to a redhat.com page so the CTA resolves to an internal destination, and consider a brief CTA in the opening section (e.g., end of "What is Omnigent?") so CTAs appear near top + mid + closing.
- Line 71-72: "The sections that follow show exactly what that deployment looks like and what it took to get there." — acceptable mid-article pointer, but it previews rather than calls; a light "keep reading" framing would strengthen the mid-CTA.

## Editorial compliance checklist

| Rule | Status | Detail |
|---|---|---|
| Sentence case headings | PASS | All 8 H2s sentence case |
| No H1 in body | PASS | Body starts at H2 |
| Clean H2/H3 cascade, no skipped levels | PASS | Flat H2 structure, no gaps |
| Oxford commas | PASS | All 3+ item lists use the serial comma (lines 24, 77, 93, 111, 220) |
| No backticks | FAIL | 21 inline code spans (lines 91, 94, 96, 110, 112, 115, 116, 143, 144, 146, 147, 164, 165, 205, 206, 217, 218) |
| Official product names, full on first mention | PARTIAL | "Red Hat OpenShift AI" correct; "Quay" should be "Red Hat Quay" on first mention (line 119) |
| Lowercase component descriptors | PASS | "web user interface", "security context constraint" lowercase |
| Acronyms expanded on first use | FAIL | UBI used line 82, expanded line 113; YAML never expanded (line 25). UI (27), LLM (69), SDK (77), PoC (78), TLS (141), CI (205) all pass |
| Aggressive contractions | FAIL | Missed: "It is" (76), "did not" (91), "did not" (96), "that is not" (112), "you are" (218) |
| Numerals in running text | FAIL | "Two" (line 82), "Four" (line 93); all other counts are numerals |
| No em dashes | PASS (body) | 0 in body; 1 in changelog comment (line 1) pending removal |
| Active voice | PASS | No passive constructions found in prose |
| No marketing tropes | PASS | No "seamless", "unleash", "game-changing", "supercharge", etc. |
| No filler transitions | PASS | "Concretely," (line 24) and "We also learned" (line 209) are mild but functional |

## Remaining violations

- Em dashes: 0 in body; 1 in changelog comment (line 1) — remove with the comment
- Unexpanded acronyms on first use: UBI (line 82), YAML (line 25)
- Missed contractions: lines 76, 91, 96, 112, 218
- Word-numbers: "Two" (line 82), "Four" (line 93)
- Product name: "Quay" without "Red Hat" on first mention (line 119)
- Links/CTA: no near-top CTA; AutoPoC unlinked in closing CTA (lines 219, 222); only 2 links in the article
- Backticks: 21 inline spans remain

## Summary

v3 fixed the prior round's weak spots (redhat.com UBI link, "Red Hat OpenShift AI" first mention, mid-article pointer, stronger close) and the prose reads well: active voice, no tropes, no filler, clean heading cascade, on-brand diagrams, and a word count squarely in the tutorial band. What holds it at 7.5 is a cluster of small mechanical misses the changelog claimed to have cleared: UBI used before expansion, YAML never expanded, two word-numbers, five uncontracted phrases, a "Quay" without "Red Hat", 21 inline backticks, and a CTA arc that lacks a near-top beat and an internal redhat.com destination. All are one-pass fixes for v4.
