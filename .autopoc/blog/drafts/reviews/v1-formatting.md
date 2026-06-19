# Formatting Review -- v1

## Scores
| Dimension | Raw (1-10) | Weight | Weighted |
|---|---|---|---|
| Heading hierarchy | 7 | 1x | 7 |
| Code formatting | 9 | 1x | 9 |
| CTA placement | 7 | 2x | 14 |
| SEO readiness | 8 | 1x | 8 |
| Link strategy | 8 | 1x | 8 |
| Editorial compliance | 8 | 2x | 16 |
| Brand standards | 7 | 1x | 7 |
| Word count | 9 | 1x | 9 |
| **Total** | | | **78 / 100 -> 7.8** |

## Line-Level Feedback
### Heading hierarchy
- **Location**: Title line
- **Issue**: The title uses `## Deploying Omnigent...` which is H2. The blog title should NOT be an H1 in the body (correct), but it's also repeated with the first H2 being the title. This creates a double-H2 at the top (`## Deploying...` followed by `## TL;DR`).
- **Suggestion**: The blog title should be in frontmatter or metadata, not as an H2 in the body. Remove the title H2 and let the publishing platform handle the title rendering.

### CTA placement
- **Location**: Only appears at end ("Try it yourself")
- **Issue**: CTA should appear near top, mid, and closing. Currently only at closing.
- **Suggestion**: Add a brief inline CTA in the TL;DR or after the "Why OpenShift" section. Something like: "Get started with [Red Hat OpenShift AI](https://developers.redhat.com/products/red-hat-openshift-ai) to try this yourself."

### Brand standards
- **Location**: Mermaid diagram
- **Issue**: Mermaid diagram has the Red Hat theme block, which is good. No other brand issues.
- **Suggestion**: Consider mentioning "Red Hat" before "OpenShift" on first reference in each major section for brand compliance.

### Editorial compliance
- **Location**: Numbered tips in "What we learned"
- **Issue**: Tip headers use bold + numbered format. This works but could use H3 for better semantic structure.
- **Suggestion**: Minor. The bold format is acceptable for a numbered list.

## Summary
Main issues: duplicate H2 at top (title + TL;DR), and CTA only at closing. Add mid-article CTA and fix the title heading.
