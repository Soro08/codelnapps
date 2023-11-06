import os
from celery.schedules import (
    crontab,
)
from dotenv import (
    load_dotenv,
)

load_dotenv()
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND")

CELERY_IMPORTS = ("clnapp.tasks",)
CELERY_BEAT_SCHEDULE = {
    "assign_pionneer_badge": {
        "task": "clnapp.tasks.assign_pionneer_badge",
        "schedule": crontab(minute="*/1"),
    },
    "assign_star_badge": {
        "task": "clnapp.tasks.assign_star_badge",
        "schedule": crontab(minute="*/1"),
    },
}
