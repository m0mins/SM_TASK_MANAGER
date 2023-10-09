from django.urls import path
from .views import TaskListCreateApiView,TaskDetailDeleteUpdateView,PhotoListCreateAPIView,PhotoDetailDeleteUpdateView

urlpatterns = [
     path('tasks',TaskListCreateApiView.as_view()),
     path('tasks/<int:pk>/',TaskDetailDeleteUpdateView.as_view()),
     path('photo',PhotoListCreateAPIView.as_view()),
     path('photo/<int:pk>/',PhotoDetailDeleteUpdateView.as_view()),
 
]