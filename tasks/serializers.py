from rest_framework import serializers
from .models import Photo,Task
 
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields=["id","title","description","due_date","priority","is_complete","created_at","last_updated_at"]

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'task', 'image')