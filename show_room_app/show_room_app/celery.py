import os

from celery import Celery

from show_room_app import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "show_room_app.settings")

app = Celery("show_room_app")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()
