from celery import Task


class BaseTaskWithRetry(Task):
    autoretry_for = (Exception, KeyError)
    retry_kwargs = {"max_retries": 7, "countdown": 5}
