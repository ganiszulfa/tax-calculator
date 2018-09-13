#!/bin/sh
/usr/src/app/manage.py makemigrations --no-input
/usr/src/app/manage.py migrate --no-input
/usr/src/app/manage.py collectstatic --no-input
/usr/local/bin/gunicorn app_core.wsgi:application -w 1 -b :8000 --reload --max-requests 3600
