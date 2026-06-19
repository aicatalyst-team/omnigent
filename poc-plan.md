# PoC Plan: omnigent

## Project Classification
- **Type:** web-app
- **Key Technologies:** Python 3.12, FastAPI, Uvicorn, SQLAlchemy, PostgreSQL, WebSocket, React (web UI)
- **ODH Relevance:** Omnigent is an AI agent orchestration platform that coordinates multiple coding agents (Claude Code, Codex, Cursor). Deploying the server on OpenShift demonstrates the platform's ability to host agentic AI coordination infrastructure, with the web UI providing observability into multi-agent sessions.

## PoC Objectives
1. Deploy the Omnigent server (FastAPI + React SPA) on OpenShift using UBI-based containers
2. Deploy PostgreSQL as a backing database service
3. Verify the web UI loads and the health endpoint responds
4. Validate that database migrations run successfully at startup
5. Confirm the server can accept WebSocket connections for runner registration

## Infrastructure Requirements
- **Resource Profile:** medium (1Gi RAM, 500m CPU)
- **GPU Required:** No
- **Persistent Storage:** 5Gi PVC for artifacts
- **Sidecar Containers:** PostgreSQL 16 (separate deployment)
- **External Dependencies:** None (LLM APIs are used by agent runners, not the server)

## Test Scenarios

### Scenario 1: Health Check
- **Description:** Verify the /health endpoint responds with 200 OK
- **Type:** http
- **Input:** GET /health
- **Expected:** HTTP 200 with health status response
- **Timeout:** 30 seconds

### Scenario 2: Web UI Loading
- **Description:** Verify the React SPA serves correctly from the root path
- **Type:** http
- **Input:** GET /
- **Expected:** HTTP 200 with HTML containing the SPA bundle (index.html)
- **Timeout:** 30 seconds

### Scenario 3: API Docs Availability
- **Description:** Verify the OpenAPI documentation endpoint is accessible
- **Type:** http
- **Input:** GET /docs
- **Expected:** HTTP 200 with Swagger UI HTML
- **Timeout:** 30 seconds

### Scenario 4: Auth Endpoint
- **Description:** Verify the authentication system is functioning
- **Type:** http
- **Input:** GET /auth/status
- **Expected:** HTTP 200 or 401 (either indicates auth system is running)
- **Timeout:** 30 seconds

## Dockerfile Considerations
- The project already has a production UBI Dockerfile at `deploy/docker/Dockerfile.ubi`
- Multi-stage build: Node.js for web UI, Python builder, Python runtime
- Uses `registry.access.redhat.com/ubi9/python-312` and `registry.access.redhat.com/ubi9/nodejs-20`
- Entrypoint runs database migrations then starts Uvicorn
- Ports: 8000 (HTTP)
- Health check built into the Dockerfile via HEALTHCHECK directive

## Deployment Considerations
- **Deployment model:** deployment (long-running server)
- **Service creation:** Yes, ClusterIP service on port 8000
- **PostgreSQL:** Deploy as a separate pod with a Service
- **Secrets:** DATABASE_URL (PostgreSQL connection string), OMNIGENT_ACCOUNTS_COOKIE_SECRET
- **ConfigMap:** HOST, PORT, ARTIFACT_DIR, auth settings
- **PVC:** For artifact storage at /data
- **Auth mode:** accounts (built-in, no external IdP needed)
- **Test method:** HTTP requests to Service ClusterIP
