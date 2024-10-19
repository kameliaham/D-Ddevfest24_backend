from django.contrib.auth.models import User
from django.db import models
from machine.models import Machine 


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[('Manager', 'Manager'), ('Operator', 'Operator')], default='Operator')
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    first_login = models.BooleanField(default=True)
     
    def __str__(self):
        return self.user.username
    


class Task(models.Model):
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'userprofile__role': 'Operator'})
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_tasks", limit_choices_to={'userprofile__role': 'Manager'})
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)  # Link to Machine model
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()

    def __str__(self):
        return f"Task {self.id} for {self.assigned_to.username}"
