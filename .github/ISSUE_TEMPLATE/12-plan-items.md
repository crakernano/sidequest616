---
name: Backend: Plan items - CRUD
about: Implement CRUD for items inside a plan (activities, places)
title: "[backend] Plan items: add/update/delete"
labels: backend, plans
assignees: ''
---

Implement endpoints for plan items under `/api/v1/plans/{plan_id}/items`.

Checklist:
- [ ] Define `PlanItem` model and relationship to `Plan`
- [ ] Implement create/list/update/delete handlers
- [ ] Add validation for dates/locations
- [ ] Add tests and document
