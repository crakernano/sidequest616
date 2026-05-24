---
name: Backend: Endpoint tests
about: Add endpoint tests using pytest
title: "[backend] Endpoint tests (pytest)"
labels: backend, tests
assignees: ''
---

Create pytest tests for API endpoints and CRUD operations.

Checklist:
- [ ] Add test requirements to `requirements-dev.txt` or `requirements.txt` (pytest, httpx)
- [ ] Add test DB configuration (sqlite or ephemeral Postgres via docker)
- [ ] Create fixtures for DB session and test client
- [ ] Implement tests for auth, plans CRUD, permissions
- [ ] Add CI job to run tests on push/PR
