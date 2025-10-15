from rest_framework import generics
from rest_framework.permissions import AllowAny
from app.models import Task
from app.serializers import UserSerializer, TaskSerializer

class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

 
class TaskView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all().order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskUpdateView(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
