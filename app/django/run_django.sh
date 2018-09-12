#!/bin/sh
/usr/src/app/manage.py makemigrations
/usr/src/app/manage.py migrate
/usr/local/bin/gunicorn app_core.wsgi:application -w 1 -b :8000 --reload --max-requests 3600
