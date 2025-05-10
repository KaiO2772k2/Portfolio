from django.urls import path

from .views import *
from . import views

get_all_projects_api = ProjectMVS.as_view({
    'get': 'get_all_projects_api'
})

add_project_api = ProjectMVS.as_view({
    'post': 'add_project_api'
})

urlpatterns = [
    path('get_all_projects_api/', get_all_projects_api, name='get_all_projects_api'),
    path('add_project_api/', add_project_api, name='add_project_api'),
]