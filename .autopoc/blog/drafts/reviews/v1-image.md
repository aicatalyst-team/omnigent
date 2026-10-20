# Image / Visual Review — v1 (Omnigent on OpenShift)

Reviewer: IMAGE/VISUAL
Draft: drafts/v1.md
Abstract: abstract.md

## Scope

The draft uses **two inline Mermaid diagrams** (Red Hat themed) and **zero image
placeholders**. No `![...]` image embeds exist. Per the rubric, Mermaid diagrams
are evaluated on **diagram clarity** and **diagram type**; missing brand colors or
aspect ratios are not penalized, but the `%%{init}%%` theme block is checked.

## Diagram Inventory

| # | Location (line) | Type | Theme block | Content |
|---|-----------------|------|-------------|---------|
| D1 | Containerizing (§, L64-70) | `graph LR` (flowchart) | Present, RH hex | Node stage → Python stage → Runtime stage → Quay |
| D2 | Deploying (§, L90-97) | `graph LR` (flowchart) | Present, RH hex | Route → Service → Pod → emptyDir; ConfigMap/Secret -.env.-> Pod |

### D1 — Build pipeline (L64-70)
- **Correctness:** Accurate. Mirrors the prose: Node stage compiles the React
  UI, Python stage runs `uv` install + web bundle, runtime stage is UBI9
  non-root (USER 1001) exposing :8000, pushed to `quay.io/aicatalyst/omnigent-server`.
- **Type:** Flowchart (`graph LR`) is the correct choice for a linear,
  ordered multi-stage build. Good.
- **Clarity:** Readable, four nodes, no ambiguity. The `Q[(...)]` cylinder
  correctly signals a registry/store.
- **Theme:** Valid Red Hat palette — `#EE0000` primary, `#A30000` border,
  `#6A6E73` line, `#F0F0F0` secondary, `#0066CC` tertiary. All genuine RH
  hex values.
- **Placement:** Immediately after the paragraph describing the multi-stage
  build and the two edits. Strong rationale.

### D2 — Deployment topology (L90-97)
- **Correctness:** Accurate. Route (edge TLS) → Service (80→8000) →
  Pod (omnigent-server) → `emptyDir /data` (SQLite + artifacts);
  ConfigMap + Secret dotted into the Pod for env. Matches the restricted-v3 /
  single-pod narrative.
- **Type:** Flowchart is acceptable for a small request-path topology. A
  dedicated architecture layout would be marginal, but for 4-5 nodes a
  `graph LR` is the right, minimal choice.
- **Clarity:** Readable. The dashed `-.env.->` edge for ConfigMap/Secret is a
  nice touch distinguishing config injection from the traffic path.
- **Theme:** Same valid Red Hat palette as D1.
- **Placement:** Directly after the deployment/security-context discussion.
  Strong rationale.

## Redundancy / Missing Opportunities
- No redundant diagrams. D1 (build) and D2 (deploy) cover distinct concerns.
- No leftover image placeholders to convert.
- **One missed opportunity:** the "Running the PoC tests" section lists five
  endpoint checks in prose only. A compact flow (Route → 5 GET checks → pass)
  is *not* strictly needed and a diagram here would risk clutter; leaving it
  as a list is defensible. Not flagged as a defect.

## Per-Dimension Feedback

- **Placement rationale:** Both diagrams sit exactly where the corresponding
  mechanism is explained and each materially aids comprehension (build stages,
  request path + storage). No decorative visuals.
- **Prompt specificity (diagram detail):** Nodes carry concrete, verifiable
  labels (stage names, ports, image name, volume path). Specific enough to
  render correctly on first try.
- **Brand compliance:** Both `%%{init}%%` blocks present with authentic Red
  Hat hex values (primary `#EE0000`, dark red `#A30000`, neutral `#6A6E73`,
  `#F0F0F0`, blue `#0066CC`). Compliant.
- **Aspect ratio & sizing:** Mermaid-managed; wide `graph LR` suits both. Not
  penalized per rubric.
- **Alt text quality:** **Weakest area.** Neither diagram has a caption or
  alt-text equivalent. Rendered Mermaid in the RH blog pipeline benefits from a
  one-line caption beneath each figure for screen readers and standalone
  reading. Currently generic/missing.
- **Image count:** 2 diagrams, each earning its place, well under the cap of 10.

## Scores

| Dimension | Weight | Raw (1-10) | Weighted |
|-----------|--------|------------|----------|
| Placement rationale | 2x | 9 | 18 |
| Prompt specificity | 2x | 9 | 18 |
| Brand compliance | 2x | 9 | 18 |
| Aspect ratio & sizing | 1x | 8 | 8 |
| Alt text quality | 1x | 7 | 7 |
| Image count | 1x | 9 | 9 |
| **Total** | | | **78** |

**Normalization:** `(78 / 90) * 10 = 8.7`

## Summary

Two accurate, well-typed, properly-themed Mermaid diagrams, each placed
precisely beside the prose it illustrates, with no redundancy and a healthy
count. The only material gap is the absence of accessible captions / alt text
under each diagram.

**Most important visual change:** add a one-line caption (alt-text equivalent)
beneath each Mermaid diagram — e.g. *"Figure: Omnigent multi-stage UBI build
pipeline ending in the Quay image"* and *"Figure: Single-pod deployment
topology — Route → Service → Pod with emptyDir storage and config injection"* —
to close the accessibility/standalone-readability gap.
