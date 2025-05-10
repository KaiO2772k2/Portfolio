from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image')
    description = models.TextField()
    link = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Language(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, related_name='languages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name