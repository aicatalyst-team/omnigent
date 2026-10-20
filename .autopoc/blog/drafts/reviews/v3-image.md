# Image Review — v3 (Omnigent on OpenShift)

Reviewer role: IMAGE/VISUAL. Scope: the three inline Mermaid diagrams
(architecture, build stages, deployment topology), their captions, and
visual-coverage gaps. Per the Mermaid rubric, brand color and aspect-ratio
gaps are not penalized; the `%%{init}%%` theme block is checked for Red Hat
brand variables.

The v2 gap — the opening "server as coordination point over multiple agents"
thesis being prose-only — is resolved: v3 adds the architecture diagram in
"What is Omnigent?".

## Scores

| Dimension | Weight | Raw | Weighted |
|---|---|---|---|
| Placement rationale | 2x | 10 | 20 |
| Prompt specificity | 2x | 9 | 18 |
| Brand compliance | 2x | 9 | 18 |
| Aspect ratio & sizing | 1x | 10 | 10 |
| Alt text quality | 1x | 8 | 8 |
| Image count | 1x | 10 | 10 |
| **Total** | | | **84 / 90** |

**Normalized: (84 / 90) × 10 = 9.3**

Rationale notes:
- Placement 10: every diagram sits immediately after the prose it explains
  and each aids comprehension; none is decorative. The hero diagram now
  anchors the opening thesis.
- Specificity 9: node labels carry concrete names, ports, stages, and the
  Quay image path. Small precision nits: Figure 2's linear chain hides the
  fan-in (the server stage consumes both the Node and Python stages), and
  Figure 3 omits the Deployment that the prose names.
- Brand 9: all three diagrams carry the same valid `%%{init}%%` block with
  Red Hat palette values (#EE0000, #A30000, #6A6E73, #F0F0F0, #0066CC,
  #fff). Consistent and correct; the near-black neutral #151515 is the only
  palette family unused.
- Aspect ratio 10: per the Mermaid rubric, no penalty — theming is handled
  by the init directive.
- Alt text 8: captions are descriptive and state the takeaway, but Figure 1's
  caption could also surface the multi-device UI point.
- Count 10: three diagrams, each earns its place, well under the cap of 10.

## Per-diagram feedback

### Figure 1 — Meta-harness architecture (lines 31-56)
- **Correctness:** Accurate against the prose. The Hosts subgraph covers all
  seven named agent types plus custom YAML agents (compressed into 5 nodes,
  which is fine). The Server subgraph matches "coordinates sessions, enforces
  policies such as approval gates and spend caps, and serves a web UI", and
  "hosts that register with it" is captured by the agent→coordinator edges.
  Minor: `POL --> COORD` reads as "policy drives the coordinator" rather than
  "policy constrains it"; the caption's "behind a policy layer" phrasing
  carries the meaning, so this is cosmetic.
- **Value:** High. Closes the v2 gap — the central meta-harness relationship
  is now visible in the first section.
- **Placement:** Correct — after the "What is Omnigent?" prose, before
  "Why it matters", so the reader sees the model before being told why it
  matters on OpenShift.
- **Diagram type:** Right choice; `graph TD` with subgraphs is the correct
  form for a conceptual architecture split into host-side and server-side.
- **Theme:** Valid Red Hat init block.
- **Caption:** Clear. Improvement: the prose's opening hook is "point a
  browser, a phone, or a whole team at" — no human/user actor appears
  anywhere in the diagram. Adding a "You (browser / phone)" node feeding the
  Web UI node would tie the hero diagram to the multi-device value prop.
- **Missing element (most important remaining change):** the user. The
  diagram ends at the server; the person supervising agents from a browser or
  phone — the reason this is a "real server" rather than a laptop tool — is
  invisible.

### Figure 2 — Build stages (lines 127-136)
- **Correctness:** Accurate. Node → Python (uv) → Server (web bundle) →
  Runtime (UBI9, USER 1001, :8000) → Quay image mirrors the prose's "four of
  six stages feed the server image" framing and the v3 stage-count fix.
  Minor: in the actual Dockerfile the server stage depends on both the Node
  and Python stages (fan-in); the linear chain is an acceptable schematic
  since the prose also presents the stages sequentially.
- **Value:** High. Turns the multi-stage build into a one-glance pipeline and
  lands on the Quay image that the `oc start-build` block produces.
- **Placement:** Correct — immediately after the on-cluster build command.
- **Diagram type:** Right choice; a linear `graph LR` is the correct shape
  for a build pipeline.
- **Theme:** Valid Red Hat init block.
- **Caption:** Clear and consistent with the corrected 4-of-6 count.

### Figure 3 — Single-pod topology (lines 168-178)
- **Correctness:** Traffic flow is accurate: Route (edge TLS) → Service
  (80→8000) → Pod, with the emptyDir `/data` volume shown as a cylinder and a
  dashed ConfigMap+Secret → Pod edge for env injection. One gap: the prose
  says "A single Deployment runs the server", but the diagram goes
  Service → Pod directly. Readers who check the OpenShift Console topology
  will expect Route → Service → Deployment → Pod.
- **Value:** High. Concretizes the "deliberately small" single-pod claim and
  the volume/config details that prose undersells.
- **Placement:** Correct — after the securityContext block and the `oc apply`
  success line.
- **Diagram type:** Right choice; a topology graph is the appropriate form.
- **Theme:** Valid Red Hat init block.
- **Caption:** Clear, mentions the emptyDir volume and config injection.
- Suggested fix: insert a `Deployment` node between Service and Pod
  (`SV --> DEP[Deployment] --> PD`) to match both the prose and the console
  topology view.

No image placeholders remain; all three visuals are diagrammable content
correctly rendered as Mermaid, so no further conversions are required.

## Missing visual opportunities

- **"Running the PoC tests" (lines 182-197):** The 5 endpoint checks are a
  bash block with inline expected outputs. A compact client → Route → server
  → 200/JSON diagram is possible but low priority; the code block already
  carries the results well. Optional, not required — and adding it would
  push the post toward a fourth visual for marginal gain.

## Summary

Three well-chosen, accurate, correctly-themed Mermaid diagrams, each placed
adjacent to the prose it explains and each carrying a specific caption. The
v2 hero-diagram gap is closed. Remaining items are refinements, not
corrections: the architecture diagram has no human actor despite the
multi-device pitch, and the topology diagram omits the Deployment the prose
names.

**Single most important visual change still needed:** Add a user actor to
the Figure 1 architecture diagram — a "You (browser / phone)" node connected
to the Web UI node — so the hero diagram shows the multi-device supervision
story the opening section sells ("point a browser, a phone, or a whole team
at"); as drawn, the diagram ends at the server and the human is invisible.
