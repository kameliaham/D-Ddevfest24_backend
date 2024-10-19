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
