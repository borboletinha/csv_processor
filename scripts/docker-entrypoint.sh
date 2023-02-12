#!/bin/sh
set -e

python manage.py migrate --run-syncdb
python manage.py collectstatic --noinput

exec "$@"