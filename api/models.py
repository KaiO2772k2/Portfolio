from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image')
    description = models.TextField()
    description_vn = models.TextField(null=True, blank=True)
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
    
class ProjectDetail(models.Model):
    name_type = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    date_vn = models.CharField(max_length=100, null=True, blank=True)
    description_long = models.TextField()
    description_long_vn = models.TextField(null=True, blank=True)
    link_be = models.TextField(null=True, blank=True)
    link_fe = models.TextField(null=True, blank=True)
    link_youtube = models.TextField(null=True, blank=True)
    features = models.TextField(null=True, blank=True)
    project = models.ForeignKey(Project, related_name='project_details', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_type