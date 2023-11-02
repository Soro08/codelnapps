from celery import shared_task
from django.core.management import call_command

from .config import BaseTaskWithRetry


@shared_task(bind=True, base=BaseTaskWithRetry)
def assign_star_badge(self):
    print("Star Badges")


@shared_task(bind=True, base=BaseTaskWithRetry)
def assign_pionneer_badge(self):
    print("Pionneer Badges")
    # if not random.choice([0, 1]):
    #     raise Exception()
    # else:
    #     call_command(
    #         "mc",
    #     )
