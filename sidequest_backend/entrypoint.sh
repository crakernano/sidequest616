#!/usr/bin/env bash
set -e

# Optional automatic migrations: if APPLY_MIGRATIONS is '1' or 'true' (case-insensitive)
APPLY_VAR="${APPLY_MIGRATIONS:-false}"
APPLY_VAR_LOWER=$(echo "$APPLY_VAR" | tr '[:upper:]' '[:lower:]')

if [ "$APPLY_VAR_LOWER" = "1" ] || [ "$APPLY_VAR_LOWER" = "true" ]; then
  echo "[entrypoint] APPLY_MIGRATIONS is set -> running alembic upgrade head"
  # wait for DB to be available (simple loop)
  TRY=0
  until alembic upgrade head || [ $TRY -ge 10 ]; do
    TRY=$((TRY+1))
    echo "[entrypoint] alembic failed, retrying ($TRY/10) in 3s..."
    sleep 3
  done
  if [ $TRY -ge 10 ]; then
    echo "[entrypoint] alembic upgrade failed after retries" >&2
    exit 1
  fi
else
  echo "[entrypoint] APPLY_MIGRATIONS not set or false -> skipping alembic"
fi

# Exec the CMD
exec "$@"
