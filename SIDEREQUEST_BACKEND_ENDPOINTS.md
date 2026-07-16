# Lista de endpoints — SideQuest

Listado consolidado de endpoints a desarrollar para el backend. Úsalos como checklist de funcionalidad.

[] **Health check**  
  [X] GET /api/v1/health — Estado de la aplicación y comprobaciones básicas (DB, uptime). Público.  

[] Autenticación  
  [X] POST /api/v1/auth/register — Registro de usuario (nombre, email, contraseña).  
  [X] POST /api/v1/auth/login — Login; devuelve token de acceso (JWT) y opcional refresh token.  
  [] POST /api/v1/auth/refresh — Renovación de token (refresh).  
  [] POST /api/v1/auth/logout — Cierre de sesión / revocación de tokens.  

[] Usuarios  
  [X] GET /api/v1/users/me — Perfil del usuario autenticado.  
  [] PUT/PATCH /api/v1/users/me — Actualizar perfil del usuario.  

[] Planes  
  [X] POST /api/v1/plans — Crear un plan (título, descripción, fechas, visibilidad, tags).  
  [X] GET /api/v1/plans — Listar planes (paginación + filtros: owner, tags, fechas, compartidos).  
  [] GET /api/v1/plans/{id} — Recuperar detalle de un plan (items, colaboradores, attachments).
  [X] PUT/PATCH /api/v1/plans/{id} — Actualizar plan.  
  [X] DELETE /api/v1/plans/{id} — Eliminar plan (soft[]delete opcional).  

[] Items dentro del plan  
  [] POST /api/v1/plans/{plan_id}/items — Añadir item (actividad, lugar, nota).  
  [] PUT/PATCH /api/v1/plans/{plan_id}/items/{item_id} — Actualizar item.  
  [] DELETE /api/v1/plans/{plan_id}/items/{item_id} — Eliminar item.  

[] Colaboración / Compartir  
  [x] POST /api/v1/plans/{id}/collaborators — Invitar colaborador (email, rol).  
  [] DELETE /api/v1/plans/{id}/collaborators/{user_id} — Remover colaborador.  

[] Attachments  
  [] POST /api/v1/plans/{id}/attachments — Subir archivo asociado a un plan.  
  [] DELETE /api/v1/plans/{id}/attachments/{attachment_id} — Borrar attachment.  

[] Tags  
  [X] GET /api/v1/tags — Listar etiquetas.  
  [X] POST /api/v1/tags — Crear etiqueta.  
  [X] DELETE /api/v1/tags/{id} — Eliminar etiqueta.  
  [] Soportar filtrado por tag en `GET /api/v1/plans`.

[] Búsqueda y exportación  
  [] GET /api/v1/search?query=... — Búsqueda global (plans, items).  
  [] GET /api/v1/plans/{id}/export?format=ics|json — Exportar plan (ICS para calendarios o JSON).  

[] Administración  
  [] GET /api/v1/admin/users — Listar usuarios (admin only).  
  [] DELETE /api/v1/admin/users/{id} — Eliminar usuario (admin only).  

