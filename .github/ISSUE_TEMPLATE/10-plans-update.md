---
name: Backend: Plans - update
about: Implement endpoint to update a plan
title: "[backend] Plans: update plan"
labels: backend, plans
assignees: ''
---

Implement `PUT/PATCH /api/v1/plans/{id}` to update plan fields.

Checklist:
- [ ] Create `PlanUpdate` schema
- [ ] Implement update logic and ownership checks
- [ ] Add tests for partial and full updates
- [ ] Document allowed fields and behavior
