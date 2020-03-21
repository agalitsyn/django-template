#!/usr/bin/env bash

set -ex

if [[ "$COLLECT_STATIC" == 'true' ]]; then
  python manage.py collectstatic --no-input
fi

if [[ "$COMPILE_MESSAGES" == 'true' ]]; then
  python manage.py compilemessages --verbosity 3 --locale ru
fi

if [[ "$MIGRATE" == 'true' ]]; then
  python manage.py migrate
fi

if [[ "$DEBUG" == 'true' ]]; then
  python manage.py print_settings
fi

if [[ "$DEVELOPMENT" == 'true' ]]; then
  python manage.py createsuperuserwithpassword --username=admin --password=123qweasd --email=foo@bar.com
  python manage.py runserver 0.0.0.0:5000
else
  gunicorn app.wsgi --bind 0.0.0.0:5000 --timeout 60 --log-file -
fi
