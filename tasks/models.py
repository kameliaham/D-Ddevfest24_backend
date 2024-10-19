from django.db import models

from machine.models import Machine


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    #assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'userprofile__role': 'Operator'})
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)  # Link to Machine model
    status = models.CharField(max_length=50, choices=[('not_started', 'not started'), ('pending', 'pending'), ('completed', 'completed')], default='not started')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Task {self.id} about {self.machine.name}"
