from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from todo_api.models import Task
from todo_api.serializers import TaskSerializer


class TaskView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, id):
        tasks = Task.objects.all()
        tasks_serializer = TaskSerializer(tasks, many=True)
        return Response(tasks_serializer.data)

    def post(self, request, id):
        new_task = TaskSerializer(data=request.data)
        if new_task.is_valid():
            new_task.save()
            return Response({'status': 'Added'})
        return Response({'status': 'Error'})

    def put(self, request, id):
        new_flag_due = request.data.get('flag_due')
        status_task = Task.objects.filter(id=id).update(flag_due=new_flag_due)
        if status_task == 1:
            return Response({'status': 'Updated'})
        return Response({'status': 'Error'})
