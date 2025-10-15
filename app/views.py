from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
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
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        
        if serializer.validated_data.get('assigned_to') and serializer.instance.status == 'open':
            serializer.save(status='assigned')
        
        elif serializer.validated_data.get('status') == 'completed':
            serializer.save()
        else:
            serializer.save()
