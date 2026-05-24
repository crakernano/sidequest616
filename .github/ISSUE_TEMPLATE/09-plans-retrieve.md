---
name: Backend: Plans - retrieve
about: Implement endpoint to retrieve a plan details
title: "[backend] Plans: retrieve plan"
labels: backend, plans
assignees: ''
---

Implement `GET /api/v1/plans/{id}` returning full plan details.

Checklist:
- [ ] Ensure related fields (items, collaborators, attachments, tags) are included or linked
- [ ] Implement permissions (public vs private vs collaborator)
- [ ] Add tests for access control and data correctness
- [ ] Document response structure
