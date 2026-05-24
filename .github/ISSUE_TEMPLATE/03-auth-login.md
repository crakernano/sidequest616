---
name: "Backend: Auth - login"
about: Implement user login and token issuance
title: "[backend] Auth: login (token)"
labels: backend, auth, enhancement
assignees: ''
---

Implement authentication endpoint for issuing access tokens (JWT).

- Path: `POST /api/v1/auth/login`
- Input: email, password
- Output: access token (JWT) and optional refresh token

Checklist:
- [ ] Verify credentials against stored hashed password
- [ ] Implement token generation (JWT) with expiry and claims
- [ ] Add Pydantic schemas for request/response
- [ ] Add tests for successful and failed logins
- [ ] Document auth flow in README/API docs

Security: choose secure signing key and algorithm; avoid leaking user info on failures.
