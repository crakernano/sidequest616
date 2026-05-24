---
name: "Backend: Auth - refresh/logout"
about: Implement token refresh and logout endpoints
title: "[backend] Auth: refresh token/logout"
labels: backend, auth
assignees: ''
---

Add token refresh and logout functionality.

- Paths:
  - `POST /api/v1/auth/refresh` (exchange refresh token for new access token)
  - `POST /api/v1/auth/logout` (revoke tokens / blacklist)

Checklist:
- [ ] Decide refresh token strategy (JWT with rotation or server-side store)
- [ ] Implement refresh endpoint and tests
- [ ] Implement logout/revocation mechanism if required
- [ ] Document token lifetimes and revocation behavior

Notes: consider simplicity vs security tradeoffs; rotation + short access tokens recommended.
