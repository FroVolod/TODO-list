from rest_framework import serializers

from todo_api.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'date_creation', 'is_done', 'order')


class TaskEditSerializer(serializers.Serializer):
    new_is_done = serializers.BooleanField(required=False)
    old_index = serializers.IntegerField(required=False)
    new_index = serializers.IntegerField(required=False)
