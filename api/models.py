from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/')
    description = models.TextField()
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