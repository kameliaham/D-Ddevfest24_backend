from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    machine = serializers.StringRelatedField()

    class Meta:
        model = Task
        fields = ['id', 'description', 'machine', 'status', 'created_at']
