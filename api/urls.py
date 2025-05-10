from django.urls import path

from .views import *
from . import views

get_all_projects_api = ProjectMVS.as_view({
    'get': 'get_all_projects_api'
})

add_project_api = ProjectMVS.as_view({
    'post': 'add_project_api'
})

get_all_languages_api = LanguageMVS.as_view({
    'get': 'get_all_languages_api'
})

add_language_api = LanguageMVS.as_view({
    'post': 'add_language_api'
})

get_all_with_languages = ProjectMVS.as_view({  
    'get': 'get_all_with_languages'
})   

urlpatterns = [
    path('get_all_projects_api/', get_all_projects_api, name='get_all_projects_api'),
    path('add_project_api/', add_project_api, name='add_project_api'),
    path('get_all_languages_api/', get_all_languages_api, name='get_all_languages_api'),
    path('add_language_api/', add_language_api, name='add_language_api'), 
    path('get_projects_by_language/', get_all_with_languages, name='get_projects_by_language'),
]