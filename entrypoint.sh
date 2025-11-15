#!/bin/sh

echo "Waiting for PostgreSQL..."

while ! python - <<END
import psycopg2, sys
try:
    conn = psycopg2.connect(
        dbname="${POSTGRES_DB}",
        user="${POSTGRES_USER}",
        password="${POSTGRES_PASSWORD}",
        host="${POSTGRES_HOST:-db}",
        port="${POSTGRES_PORT:-5432}"
    )
    conn.close()
except:
    sys.exit(1)
END
do
  sleep 0.5
done

echo "PostgreSQL is up - applying migrations..."
python manage.py migrate

echo "Creating superuser if not exists..."
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin','admin@example.com','admin')"

echo "Starting server..."
exec "$@"