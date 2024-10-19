#from background_task import background
from .services import subscribe_all_machines  # Assuming the subscribe function is in utils.py

#@background(schedule=86400)  # Reschedule this task every 24 hours (86400 seconds)
def periodic_subscription():
    subscribe_all_machines()  # Ensure all machines are subscribed to the webhook
