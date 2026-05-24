---
name: Backend: Health check
about: Implement health check endpoint for the backend
title: "[backend] Health check endpoint"
labels: backend, api, enhancement
assignees: ''
---

Implement a lightweight health-check endpoint for `siderequest_backend`.

- Path: `GET /api/v1/health`
- Purpose: return service status and basic diagnostics (ok, timestamp, optional DB connectivity)

Checklist:
- [ ] Add route in `app/api` (router)
- [ ] Implement minimal handler returning 200 + JSON `{status: "ok", uptime: ..., db: "ok"}`
- [ ] Add unit/integration tests (pytest)
- [ ] Document endpoint in OpenAPI (FastAPI does this automatically if routed)
- [ ] Close issue when endpoint is reachable and documented

Notes: keep this endpoint light and safe for unauthenticated checks (used by k8s or health-probes).
