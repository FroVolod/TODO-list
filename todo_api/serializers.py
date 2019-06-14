from rest_framework import serializers

from todo_api.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'date_creation', 'date_due', 'flag_due')
