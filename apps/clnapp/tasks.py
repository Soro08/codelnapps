from celery import shared_task, Task
from django.core.management import call_command
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


class BaseTaskWithRetry(Task):
    autoretry_for = (Exception, KeyError)
    retry_kwargs = {"max_retries": 7, "countdown": 5}


@shared_task(bind=True, base=BaseTaskWithRetry)
def assign_star_badge(self):
    logger.info("The sample task just ran.")


@shared_task(bind=True, base=BaseTaskWithRetry)
def assign_pionneer_badge(self):
    logger.info("The sample task just ran.")
    # if not random.choice([0, 1]):
    #     raise Exception()
    # else:
    #     call_command(
    #         "mc",
    #     )
