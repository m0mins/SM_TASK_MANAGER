from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Task
from .serializers import TaskSerializer
from rest_framework import generics

# Create your views here.

class TaskListCreateApiView(generics.ListCreateAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer

class TaskDetailDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail": "Resource successfully deleted."}, status=status.HTTP_204_NO_CONTENT)
