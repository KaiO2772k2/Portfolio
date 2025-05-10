from django.shortcuts import render
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Q, Count
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.forms.models import model_to_dict
import re
from rest_framework.parsers import MultiPartParser, FormParser

from api.models import *
from .serializers import *

# Create your views here.

class ProjectMVS(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer 

    @action(detail=False, methods=['GET'], url_name='get_all_projects_api', url_path='get_all_projects_api')
    def get_all_projects_api(self, request):
        try:
            projects = Project.objects.all()
            serializer = ProjectSerializer(projects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            print("get_all_projects_api_error: ", error)
            return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=False, methods=['POST'], url_name='add_project_api', url_path='add_project_api')
    def add_project_api(self, request):
        try:
            serializer = ProjectSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            print("add_project_api_error: ", error)
            return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)