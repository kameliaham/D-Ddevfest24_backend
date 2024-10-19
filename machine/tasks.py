from celery import shared_task
import time
from .views import subscribe_all_machines

@shared_task
def send_machine_data_webhook():
    """
    This task sends machine data webhook requests every 20 seconds.
    """
    subscribe_all_machines()
