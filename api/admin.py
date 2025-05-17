from django.contrib import admin
from .models import Project, Language, ProjectDetail

# Register your models here.

admin.site.register(Project)
admin.site.register(Language)
admin.site.register(ProjectDetail)