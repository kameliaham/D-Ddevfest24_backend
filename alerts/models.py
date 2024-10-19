from django.db import models
import uuid
from machine.models import Machine


class Alert(models.Model):
    alert_id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"Alert: {self.title} ({self.machine})"
