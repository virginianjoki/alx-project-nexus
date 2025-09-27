import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

app = Celery("myproject")

# Load settings from Django
app.config_from_object("django.conf:settings", namespace="CELERY")

# Discover tasks in apps
app.autodiscover_tasks()
