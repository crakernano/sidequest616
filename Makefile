.PHONY: help up down build logs ps shell migrate makemigration test

help:
	@echo "Makefile - comandos útiles para el proyecto 🧰"
	@echo "  make up            -> Levanta el entorno (docker compose)"
	@echo "  make down          -> Para y elimina los contenedores"
	@echo "  make build         -> Fuerza la reconstrucción de las imágenes"
	@echo "  make logs          -> Sigue los logs (compose)"
	@echo "  make ps            -> Muestra los contenedores en ejecución"
	@echo "  make shell         -> Abre shell en el contenedor backend"
	@echo "  make migrate       -> Aplica migraciones (alembic upgrade head)"
	@echo "  make makemigration m=MSG -> Crea una migración autogenerada con mensaje MSG"
	@echo "  make test          -> Ejecuta tests dentro del contenedor backend (si tienes pytest)"

up:
	docker compose up --build -d

down:
	docker compose down

build:
	docker compose build --no-cache

logs:
	docker compose logs -f

ps:
	docker compose ps

shell:
	docker compose exec backend bash

migrate:
	docker compose exec backend alembic upgrade head

makemigration:
	if [ -z "$(m)" ]; then \
		echo "Usage: make makemigration m=\"message\""; exit 1; \
	fi
	docker compose exec backend alembic revision --autogenerate -m "$(m)"

test:
	docker compose exec backend pytest
