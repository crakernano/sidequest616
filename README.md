

# Plans API (backend)

Backend scaffold for a Plans application using FastAPI and PostgreSQL. In this repository the backend is located in the `siderequest_backend` folder; the same repo will host frontend and mobile app folders later.

Project layout (relevant paths)
-------------------------------
- `siderequest_backend/` — backend FastAPI app, `app/` package, `alembic/`, `Dockerfile`, `.env.example`, `requirements.txt`.
- `docker-compose.yml` — orquesta servicios (Postgres + backend) desde la raíz del repositorio.

Technology stack
----------------
- Backend framework: FastAPI
- ORM: SQLAlchemy
- Migrations: Alembic
- Database: PostgreSQL
- Validation/serializers: Pydantic
- Server: Uvicorn (ASGI)
- Containerization: Docker + Docker Compose

Entorno y variables
--------------------
Copiar el ejemplo de entorno y ajustarlo:

```bash
cp siderequest_backend/.env.example siderequest_backend/.env
# editar siderequest_backend/.env con tus credenciales
```

El backend lee `DATABASE_URL` desde `siderequest_backend/.env`. Cuando se usa Docker Compose, el host de la DB debe ser `db` (servicio del compose). Ejemplo incluido en `.env.example`:

```
DATABASE_URL=postgresql://user:password@db:5432/plans_db
```

Arrancar localmente sin Docker (opcional)
---------------------------------------
Si prefieres ejecutar localmente con un virtualenv:

```bash
python -m venv venv
source venv/bin/activate
pip install -r siderequest_backend/requirements.txt
uvicorn app.main:app --reload --port 8000 --host 0.0.0.0
```

Usando Docker Compose (recomendado para desarrollo)
--------------------------------------------------
Desde la raíz del repo ejecuta:

```bash
docker compose up --build
```

Qué hace:
- Levanta un servicio `db` con Postgres (imagen oficial).
- Levanta el servicio `backend` construyendo `siderequest_backend/Dockerfile`.
- Mapea el puerto `8000` del contenedor al `8000` del host.
- Monta un bind-mount `./siderequest_backend:/app` para que los cambios de código en tu máquina se reflejen inmediatamente en el contenedor sin rebuild (útil en desarrollo con `--reload`).

Migraciones con Alembic dentro de Docker
---------------------------------------
Una vez levantados los servicios, generar y aplicar migraciones desde el contenedor del backend:

```bash
# abrir shell en el contenedor backend
docker compose exec backend bash

# dentro del contenedor
alembic revision --autogenerate -m "create plans table"
alembic upgrade head
```

Migraciones automáticas al iniciar (opcional)
-------------------------------------------
El contenedor del backend ahora puede aplicar migraciones automáticamente al arrancar si estableces la variable de entorno `APPLY_MIGRATIONS=true` en el servicio.

Ejemplo en `docker-compose.yml` (override):

```yaml
services:
	backend:
		environment:
			- APPLY_MIGRATIONS=true
```

El `entrypoint` del contenedor ejecutará `alembic upgrade head` y reintentará hasta que la base de datos esté lista.


Notas importantes
-----------------
- Asegúrate de que `siderequest_backend/.env` contiene las variables `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` y `DATABASE_URL` coherentes con `docker-compose.yml`.
- El bind-mount `./siderequest_backend:/app` facilita el desarrollo pero no es recomendable en producción. Para producción elimina el bind-mount y construye una imagen inmutable.
- Para entornos de producción sustituye `--reload` por un proceso de arranque preparado (por ejemplo `gunicorn` con workers Uvicorn) y gestiona secretos con un vault o variables de entorno fuera del control de versiones.

Comandos útiles
---------------
- Arrancar (construir imagen si hace falta):
```bash
docker compose up --build
```
- Parar y eliminar contenedores:
```bash
docker compose down
```
- Ejecutar migraciones (desde host, dentro del contenedor):
```bash
docker compose exec backend alembic upgrade head
```

Makefile mágico ✨
-----------------
También incluimos un `Makefile` en la raíz del repositorio para acelerar tareas comunes. Está diseñado para usar `docker compose` y facilitar tu flujo de trabajo en desarrollo.

Comandos disponibles (ejemplos):

```bash
# Levantar (detached) y construir si hace falta
make up

# Parar y eliminar
make down

# Reconstruir imágenes
make build

# Seguir logs
make logs

# Entrar en shell del backend
make shell

# Aplicar migraciones
make migrate

# Crear una migración autogenerada (usa: make makemigration m="mi mensaje")
make makemigration m="create plans table"

# Ejecutar tests (si están configurados)
make test
```

Consejo pro-tip 🚀
------------------
- Si vas a trabajar en el backend, copia `siderequest_backend/.env.example` a `siderequest_backend/.env` y edita las credenciales antes de `make up`.
- El `Makefile` usa `docker compose` (plugin moderno). Si tu instalación usa `docker-compose` antiguo, reemplaza los comandos en el `Makefile` o ejecuta los comandos manualmente.

¡Listo! Ahora puedes usar atajos tipo mago para administrar el entorno con menos escritura y más café ☕️🪄

Siguientes pasos recomendados
-----------------------------
- Añadir tests y una configuración de CI que ejecute linters y tests.
- Añadir un `Makefile` o scripts para comandos comunes (`up`, `down`, `migrate`, `shell`).
- Implementar un flujo seguro para gestionar secretos en staging/producción.

Pre-commit y linters (desarrollo)
--------------------------------
Recomendado: usar `pre-commit` para ejecutar `ruff`, `pylint`, `bandit` y `vulture` antes de cada commit sobre la carpeta `siderequest_backend`.

Instalación rápida:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pre-commit install
```

Probando los hooks manualmente:

```bash
pre-commit run --all-files
```

Los hooks están configurados para ejecutar sobre archivos dentro de la carpeta `siderequest_backend`. Ajusta `.pre-commit-config.yaml` si tu código está en un path distinto.


