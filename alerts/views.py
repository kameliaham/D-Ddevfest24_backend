from rest_framework import generics, status
from rest_framework.response import Response
from user.permissions import IsOperatorOrReadOnly, IsManager
from .models import Alert
from .serializers import AlertSerializer


class AlertListView(generics.ListAPIView):
    serializer_class = AlertSerializer
    permission_classes = [IsOperatorOrReadOnly]

    def get(self):
        user = self.request.user
        if user.userprofile.role == 'Manager':
            return Alert.objects.all()
        elif user.userprofile.role == 'Operator':
            return Alert.objects.filter(machine__in=user.userprofile.machine_set.all())
        return Alert.objects.none()


class AlertPostView(generics.CreateAPIView):
    serializer_class = AlertSerializer

    def post(self, machine, title, description):
        serializer = self.get_serializer(machine=machine, title=title, description=description)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AlertDeleteView(generics.DestroyAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [IsManager]  # Only authenticated users can access this view

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
