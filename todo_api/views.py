from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.db.models import F

from todo_api.models import Task
from todo_api.serializers import TaskSerializer, TaskEditSerializer


class TaskView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, id):
        tasks = Task.objects.all().order_by('order')
        tasks_serializer = TaskSerializer(tasks, many=True)
        return Response(tasks_serializer.data)

    def post(self, request, id):
        new_task = TaskSerializer(data=request.data)
        if new_task.is_valid():
            Task.objects.all().update(order=F('order') + 1)
            new_task.save()
            return Response({'status': 'Added'})
        return Response({'status': 'Error'})

    def patch(self, request, id):
        serializer_event = TaskEditSerializer(data=request.data)
        if serializer_event.is_valid():
            new_index = serializer_event.data.get('new_index')
            old_index = serializer_event.data.get('old_index')
            if new_index or old_index:
                task_old = Task.objects.filter(order=old_index).first()
                if old_index < new_index:
                    order_task = Task.objects \
                                        .filter(order__lte=new_index) \
                                        .filter(order__gt=old_index) \
                                        .update(order=F('order') - 1)
                elif old_index > new_index:
                    order_task = Task.objects \
                                        .filter(order__gte=new_index) \
                                        .filter(order__lte=old_index) \
                                        .update(order=F('order') + 1)
                order_task += Task.objects \
                                        .filter(id=task_old.id) \
                                        .update(order=new_index)
                if order_task >= 1:
                    return Response({'status': 'Updated'})
                return Response({'status': 'Error'})
            else:
                status_task = Task.objects \
                            .filter(id=id) \
                            .update(
                                is_done=serializer_event.data['new_is_done']
                                )
                if status_task == 1:
                    return Response({'status': 'Updated'})
                return Response({'status': 'Error'})
            return Response({'status': 'No data'})
        return Response({'status': 'No data valid'})
