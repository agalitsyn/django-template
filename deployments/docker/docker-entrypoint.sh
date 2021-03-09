#!/usr/bin/env bash

set -ex

if [[ -n "$RUN_COLLECT_STATIC" ]]; then
	python manage.py collectstatic --no-input
fi

if [[ -n "$RUN_COMPILE_MESSAGES" ]]; then
	python manage.py compilemessages --verbosity 3 --locale ru
fi

if [[ -n "$RUN_MIGRATIONS" ]]; then
	python manage.py migrate
fi

if [[ -n "$RUN_DEV_SCRIPTS" ]]; then
	python manage.py create_superuser_with_password --username=admin --password=123qweasd --email=foo@bar.com
	python manage.py print_settings
fi

if [[ -n "$RUN_DEV_SERVER" ]]; then
  python manage.py runserver 0.0.0.0:5000
else
  gunicorn app.asgi:application --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:5000 --timeout 60 --log-file -
fi
