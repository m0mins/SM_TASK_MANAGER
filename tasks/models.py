from django.db import models

# Create your models here.

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return self.title


class Photo(models.Model):
    task = models.ForeignKey(Task, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    
    def __str__(self):
        return str(self.image)
