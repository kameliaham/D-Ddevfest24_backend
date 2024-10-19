from django.apps import AppConfig


class MachineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'machine'

    def ready(self):
        from .tasks import periodic_subscription
        periodic_subscription()

