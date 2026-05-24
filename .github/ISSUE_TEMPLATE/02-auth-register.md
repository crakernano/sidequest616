---
name: "Backend: Auth - register"
about: Implement user registration (signup) endpoint
title: "[backend] Auth: register"
labels: backend, auth, enhancement
assignees: ''
---

Create the user registration endpoint in `siderequest_backend`.

- Path: `POST /api/v1/auth/register`
- Input: name, email, password, (optional profile fields)
- Output: user summary (no password) or created response

Checklist:
- [ ] Define `User` model and migration if necessary
- [ ] Create Pydantic schema for `UserCreate` and `UserOut`
- [ ] Implement CRUD create_user in `app/crud`
- [ ] Add endpoint with validation and error handling (duplicate email)
- [ ] Hash passwords securely (bcrypt/argon2)
- [ ] Add tests and documentation

Notes: consider email verification as future extension.
