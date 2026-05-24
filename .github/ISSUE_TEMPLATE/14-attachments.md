---
name: Backend: Attachments
about: Implement attachments upload and deletion
title: "[backend] Attachments: upload/delete"
labels: backend, files
assignees: ''
---

Add upload/delete endpoints for attachments related to plans.

Checklist:
- [ ] Decide storage (local disk for dev, S3 for prod)
- [ ] Implement upload endpoint with size/type checks
- [ ] Implement delete and listing endpoints
- [ ] Add tests for storage and security (ACLs)
- [ ] Document storage and backup strategy
