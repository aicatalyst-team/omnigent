# Image Review — v2 (Omnigent on OpenShift)

Reviewer role: IMAGE/VISUAL. Scope: the two inline Mermaid diagrams, their
captions, and visual-coverage gaps. Per the Mermaid rubric, brand color and
aspect-ratio gaps are not penalized; the `%%{init}%%` theme block is checked.

## Scores

| Dimension | Weight | Raw | Weighted |
|---|---|---|---|
| Placement rationale | 2x | 9 | 18 |
| Prompt specificity | 2x | 9 | 18 |
| Brand compliance | 2x | 9 | 18 |
| Aspect ratio & sizing | 1x | 7 | 7 |
| Alt text quality | 1x | 8 | 8 |
| Image count | 1x | 9 | 9 |
| **Total** | | | **78 / 90** |

**Normalized: (78 / 90) × 10 = 8.7**

## Per-diagram feedback

### Figure 1 — Build stages (lines 87-95)
- **Correctness:** Accurate. Node → Python → Runtime → Quay mirrors the
  Dockerfile narrative and correctly shows only the 3 runtime-relevant stages,
  consistent with the "6 stages, 3 relevant" framing in the prose.
- **Value:** High. Turns a 6-stage build description into a one-glance pipeline
  and visually anchors the "ends in the Quay image" payoff.
- **Placement:** Correct — immediately after the runtime-stage snippet and the
  `.dockerignore`/`host`-trimming discussion.
- **Diagram type:** Right choice; a linear `graph LR` is the correct shape for a
  sequential build pipeline.
- **Theme:** `%%{init}%%` present with valid Red Hat variables
  (#EE0000, #A30000, #6A6E73, #F0F0F0, #0066CC).
- **Caption:** Clear and specific.
- Minor: node labels are dense (`UBI9, USER 1001, :8000`) but legible at width.

### Figure 2 — Single-pod topology (lines 130-140)
- **Correctness:** Accurate. Route → Service → Pod → emptyDir, plus a dashed
  ConfigMap/Secret → Pod edge for env injection, matches the deployment
  description (port 80→8000, `/data` emptyDir, edge TLS).
- **Value:** High. Concretizes the "deliberately small" single-pod claim and the
  config-injection detail that prose alone undersells.
- **Placement:** Correct — after the securityContext block and the `oc apply`
  success line.
- **Diagram type:** Right choice; a topology graph is the appropriate form.
- **Theme:** Same valid Red Hat init block.
- **Caption:** Clear, mentions the emptyDir volume and config injection.

No image placeholders remain; both visuals are diagrammable content correctly
rendered as Mermaid, so no further conversions are required.

## Missing visual opportunities

- **"What is Omnigent?" (lines 16-30):** The central thesis — a server acting as
  a coordination point over multiple agents (Claude Code, Codex, Cursor,
  OpenCode, Hermes, Pi, custom YAML) running on registering hosts, with
  approval-gate/spend-cap policies — is currently prose-only. This is the
  highest-value gap: the reader never sees the meta-harness relationship that
  the rest of the post depends on.
- **"Running the PoC tests" (lines 144-159):** The 5 endpoint checks are a bash
  block. A compact sequence-style check (client → Route → server → 200/JSON)
  is possible but lower priority; the code block already carries the expected
  outputs well, so this is optional, not required.

## Summary

Two well-chosen, accurate, correctly-themed Mermaid diagrams, each placed
adjacent to the prose it explains and each carrying a specific caption. They
earn their place and keep the post within a lean visual budget. The main
remaining gap is conceptual rather than corrective: the core "server-as-
coordination-point-over-multiple-agents" idea in the opening has no diagram.

**Single most important visual change still needed:** Add an architecture
diagram in "What is Omnigent?" showing the Omnigent server as the coordination
point connected to multiple agents (Claude Code, Codex, Cursor, OpenCode,
Hermes, Pi, custom YAML) on registering hosts, with the policy/approval-gate
layer and the web UI — the central meta-harness relationship is currently
prose-only.
