# Content Review -- v3

## Scores
| Dimension | Raw (1-10) | Weight | Weighted |
|---|---|---|---|
| Technical accuracy | 9 | 2x | 18 |
| Red Hat voice | 9 | 2x | 18 |
| Audience alignment | 9 | 1x | 9 |
| Originality | 8 | 1x | 8 |
| Evidence & examples | 9 | 2x | 18 |
| Product positioning | 9 | 1x | 9 |
| Human authenticity | 9 | 2x | 18 |
| **Total** | | | **99 / 110 -> 9.0** |

## Verification of the flagged claims

Checked directly against `deploy/docker/Dockerfile.ubi`, `deploy/docker/Dockerfile.ubi.autopoc`, `kubernetes/deployment.yaml`, `kubernetes/secret.yaml`, `.dockerignore`, and `intake-digest.md`:

- **Image name** `quay.io/aicatalyst/omnigent-server` -- matches `deployment.yaml` (`...omnigent-server:autopoc-20261020`). PASS.
- **`fsGroup: 1001480000` + `hostUsers: false` + `runAsNonRoot: true`** -- the draft's YAML block matches `deployment.yaml` byte-for-byte, including the `restricted-v3` / `fsGroup: 0` rejection rationale. PASS.
- **SQLite** -- `secret.yaml` sets `DATABASE_URL: sqlite:////data/omnigent.db` on the `emptyDir` `/data`; matches the draft. PASS.
- **5/5 results** -- the five curls (`/health`, `/api/version`, `/v1/info`, `/`, `/login`) match the abstract's five control-plane checks; "All 5 scenarios passed on the first run" is consistent. PASS.
- **4-of-6 stages feed the server image** -- `Dockerfile.ubi` has exactly 6 `FROM` stages (`web-builder`, `builder`, `server-builder`, `node-runtime`, `host`, `runtime`). The runtime chain is `web-builder` -> `builder` -> `server-builder` -> `runtime` (4); `node-runtime` + `host` are the separate sandbox target. The v2 off-by-one is now correct in both prose and the Figure caption. PASS.
- **UBI Dockerfile reuse** -- `deploy/docker/Dockerfile.ubi` exists, is UBI 9, multi-stage, `USER 1001`, `EXPOSE 8000`, `/health`; the inline snippet and the `tmux`-in-`host` rationale are accurate. PASS.
- **Build-context trim "roughly 124 MB to about 54"** -- now verifiable: repo excluding `.git` is 123M, and the `.dockerignore`-kept items (web 26M + omnigent 24M + sdks/examples/lockfiles/etc.) sum to ~52M. The v2 "unanchored numbers" concern is resolved. PASS.

## Line-Level Feedback

### Technical accuracy
- **Location**: "Deploying to the cluster" -- "the server logged that it had run its migrations and registered its built-in agents"
- **Issue**: Carried over from v2. The artifacts confirm migrations re-run on pod start (`secret.yaml`: "re-initialized on each pod start via migrations"), but "registered its built-in agents" is a light embellishment not recorded in any committed artifact. Harmless and plausible (built-in agents do exist under `examples/`), but tighten so the claim survives scrutiny.
- **Current**: "and the server logged that it had run its migrations and registered its built-in agents."
- **Suggested**: "and the server logged that it had run its migrations on startup."

### Originality
- **Location**: "What we learned" -- overall
- **Issue**: The v2 recommendation to state the server-only limitation explicitly was not taken. The opening establishes the server/host split ("the actual agent work runs on hosts that register with it"), but "What we learned" never says the PoC proves the control plane, not full agent execution. Naming that boundary is the single most distinctive thing this post can say and it would turn the lessons section from a success recap into a genuine perspective.
- **Current**: "The biggest lesson is that a well-packaged upstream project makes a PoC almost trivial."
- **Suggested**: Prepend: "The honest limit of this PoC is that it proves the control plane, not agent execution. The harness work runs on registered hosts, so a server-only deployment demonstrates the coordination layer and web UI, not a full agent run. The biggest lesson is that a well-packaged upstream project makes a PoC almost trivial."

## AI Writing Flags
### Em Dashes: 0 in readable body prose
19 ASCII `--` sequences, all structural: 2 changelog-comment delimiters (lines 1, 13, marked "removed during finalization"), 14 Mermaid `-->` arrows inside the three diagrams, and 3 CLI flag prefixes on the `oc start-build` line (`--from-dir`, `--follow`, `--wait`). One Unicode `—` sits inside the changelog comment (line 1). None appear in the body copy, so this is not a hard failure. Strip the changelog comment before publication to keep the zero-tolerance rule clean.
### Formulaic Phrases: none detected
No "that changes today," "enter [product]," "we are pleased to announce," "moreover," "furthermore," or vague-enthusiasm words ("powerful," "seamless," "robust," "delve," "leverage"). The single "lets" (line 24, "Omnigent lets you supervise") is a natural second-person verb, not "let's" overuse. Paragraph rhythm is varied and the "First... Second..." enumerations are justified by genuinely distinct items.

## Summary
Add the explicit server-only limitation to "What we learned": state plainly that this PoC proves the control plane (coordination + web UI), not full agent execution, since the harness work runs on registered hosts. Every flagged factual claim now verifies cleanly against the Dockerfiles, manifests, and `.dockerignore` (including the previously-unanchored 124->54 MB figure, which checks out at 123M/~52M). The only residual nit is the "registered its built-in agents" embellishment, which should be tightened to "ran its migrations on startup."
