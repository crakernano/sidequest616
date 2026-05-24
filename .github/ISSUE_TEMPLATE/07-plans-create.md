---
name: Backend: Plans - create
about: Implement endpoint to create a plan
title: "[backend] Plans: create plan"
labels: backend, plans
assignees: ''
---

Create `POST /api/v1/plans` to create a plan resource.

Checklist:
- [ ] Define/confirm `Plan` model fields and migrations
- [ ] Create Pydantic `PlanCreate` and `PlanOut` schemas
- [ ] Add CRUD `create_plan` function
- [ ] Implement endpoint with auth/ownership
- [ ] Add tests and OpenAPI docs

Consider default visibility (private/public) and initial collaborators.
