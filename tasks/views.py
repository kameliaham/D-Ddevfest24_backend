from rest_framework import generics, status
from rest_framework.response import Response
from user.permissions import IsOperatorOrReadOnly
from .models import Task
from .serializers import TaskSerializer


class TasksListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsOperatorOrReadOnly]

    def get(self):
        user = self.request.user
        if user.userprofile.role == 'Manager':
            return Task.objects.all()
        elif user.userprofile.role == 'Operator':
            return Task.objects.filter(machine__in=user.userprofile.machine_set.all())
        return Task.objects.none()


class TaskPostView(generics.CreateAPIView):
    serializer_class = TaskSerializer

    def post(self, machine, title, description):
        serializer = self.get_serializer(machine=machine, title=title, description=description)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TaskUpdateView(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsOperatorOrReadOnly]

    def patch(self, request, *args, **kwargs):
        task = self.get_object()
        if task.status == "not started":
            task.status = "pending"
        elif task.status == "pending":
            task.status = "completed"
        else:
            return Response({"detail": "Task is not in a modifiable status."}, status=status.HTTP_400_BAD_REQUEST)
        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

