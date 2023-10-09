from django.urls import path
from .views import TaskListCreateApiView,TaskDetailDeleteUpdateView

urlpatterns = [
     path('tasks',TaskListCreateApiView.as_view()),
     path('tasks/<int:pk>/',TaskDetailDeleteUpdateView.as_view()),
 
]