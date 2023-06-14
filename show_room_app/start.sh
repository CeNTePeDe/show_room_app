#!/bin/bash/
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input
gunicorn show_room_app.wsgi:application --bind 0.0.0.0:8000