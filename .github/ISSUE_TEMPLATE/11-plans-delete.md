---
name: Backend: Plans - delete
about: Implement endpoint to delete a plan
title: "[backend] Plans: delete plan"
labels: backend, plans, destructive
assignees: ''
---

Implement `DELETE /api/v1/plans/{id}` for removing a plan.

Checklist:
- [ ] Decide soft-delete vs hard-delete strategy
- [ ] Implement deletion with permissions
- [ ] Add tests to ensure proper authorization
- [ ] Document behavior and potential recovery steps
