from django.urls import path
from app.views import UserView, TaskView, TaskUpdateView

urlpatterns = [
    path('register/', UserView.as_view(), name='register'),
    path('tasks/', TaskView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', TaskUpdateView.as_view(), name='tasks-update'),
]
