---
name: "Feature request"
about: Plantilla para nuevas mejoras o endpoints (features)
title: "[feature] "
labels: enhancement, backend
assignees: ''
---

Resumen
-------

Describe brevemente la nueva funcionalidad o endpoint que propones.

Objetivo
-------

¿Qué problema resuelve? ¿Qué beneficio añade?

Endpoints afectados (si aplica)
--------------------------------

- Método y ruta: e.g. `POST /api/v1/plans`
- Campos esperados: (lista los campos principales)

Diseño / Esquemas
------------------

Adjunta o describe los schemas Pydantic, cambios de modelos (SQLAlchemy) o migraciones necesarias.

Seguridad / Permisos
---------------------

¿Requiere autenticación? ¿Qué rol puede acceder (owner/editor/viewer)?

Casos de prueba / Criterios de aceptación
----------------------------------------

- [ ] Caso 1: ejemplo
- [ ] Caso 2: ejemplo

Notas y dependencias
---------------------

Incluye cualquier otra dependencia (S3, colas, tareas background) o notas de diseño.

Checklist
---------
- [ ] Añadir schema Pydantic
- [ ] Añadir modelo y migración si procede
- [ ] Implementar CRUD en `app/crud`
- [ ] Añadir endpoint en `app/api` y documentarlo
- [ ] Añadir tests (pytest)
