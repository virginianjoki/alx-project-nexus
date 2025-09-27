import time
from celery import shared_task


@shared_task
def send_welcome_email(email):
    time.sleep(5)  # simulate long task
    return f"Email sent to {email}"
