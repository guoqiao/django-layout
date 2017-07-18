#!/bin/bash
python manage.py migrate --fake-initial
python manage.py loaddata test_users
python manage.py runserver 0.0.0.0:8000
