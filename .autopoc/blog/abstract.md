# Blog Abstract — Omnigent on OpenShift

- **Blog type:** Red Hat Developer Blog
- **Thesis:** Deploying Omnigent, an open-source agent orchestration "meta-harness,"
  on OpenShift AI proves that rich, governable agent control planes run as durable,
  self-contained, UBI-packaged services with no external dependencies.
- **Target audience:** Platform engineers and agent/ML developers evaluating
  agentic tooling for OpenShift.
- **Products/projects:** Red Hat OpenShift AI, Open Data Hub, Red Hat OpenShift,
  Omnigent.
- **CTA:** Try deploying your own project with AutoPoC.

## Key points (max 3)
1. Omnigent is a "meta-harness" that gives teams a common orchestration layer
   over Claude Code, Codex, Cursor, OpenCode, and custom agents, with policies
   and a multi-device web UI.
2. Its server containerizes on UBI 9 and deploys as a single non-root pod on
   OpenShift using a built-in SQLite store, with no external database required.
3. All five control-plane checks (health, version, server-info, web UI, login
   page) passed through an OpenShift Route.

## Proposed section outline
1. What is Omnigent?
2. Why it matters for OpenShift AI
3. Setting up for deployment
4. Containerizing for OpenShift
5. Deploying to the cluster
6. Running the PoC tests
7. What we learned
8. Try it yourself
