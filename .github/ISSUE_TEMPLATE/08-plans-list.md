---
name: Backend: Plans - list
about: Implement endpoint to list plans with pagination and filters
title: "[backend] Plans: list plans (filters)"
labels: backend, plans
assignees: ''
---

Implement `GET /api/v1/plans` with pagination and optional filters.

Checklist:
- [ ] Define query parameters (skip/limit, owner, tags, date range, shared)
- [ ] Implement DB queries with indices where needed
- [ ] Add response schema (paginated)
- [ ] Add tests for filters and pagination
- [ ] Document usage and examples
