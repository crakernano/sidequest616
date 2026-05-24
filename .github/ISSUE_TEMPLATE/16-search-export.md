---
name: "Backend: Search & Export"
about: Implement search and export functionality
title: "[backend] Search & export (JSON/ICS)"
labels: backend, features
assignees: ''
---

Provide search across plans and export functionality.

Checklist:
- [ ] Implement `GET /api/v1/search?query=` with pagination
- [ ] Implement export: `GET /api/v1/plans/{id}/export?format=ics|json`
- [ ] Add tests for formats and edge cases
- [ ] Document usage and examples
