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

from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.conf import settings

@api_view(['POST'])
def contact_view(request):
    data = request.data
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')
    subject = data.get('subject')
    message = data.get('message')

    if not all([first_name, last_name, email, subject, message]):
        return Response({'error': 'Missing fields'}, status=status.HTTP_400_BAD_REQUEST)

    full_message = f"""
    From: {first_name} {last_name} <{email}>
    
    Message:
    {message}
    """

    try:
        send_mail(
            subject=subject,
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['nghiatran1527@gmail.com'],
            fail_silently=False,
        )
        return Response({'success': 'Email sent'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProjectMVS(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer 

    def get_queryset(self):
        return Project.objects.all()

    @action(detail=False, methods=['GET'], url_name='get_all_projects_api', url_path='get_all_projects_api')
    def get_all_projects_api(self, request):
        queryset = Project.objects.all()
        
        serializers = self.serializer_class(queryset, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)
        
    @action(detail=False, methods=['POST'], url_name='add_project_api', url_path='add_project_api')
    def add_project_api(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                model = serializer.add(request)
                if model:
                    return Response({"message": "Project added successfully"}, status=status.HTTP_201_CREATED)
                return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as error:
            print("add_project_api_error: ", error)
            return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=False, methods=['GET'], url_name='get_all_projects_with_languages', url_path='all_with_languages')
    def get_all_with_languages(self, request):
        try:
            projects = self.get_queryset().prefetch_related('languages')
            serializer = self.get_serializer(projects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            print("get_all_with_languages_error:", error)
            return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class LanguageMVS(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer 

    @action(detail=False, methods=['GET'], url_name='get_all_languages_api', url_path='get_all_languages_api')
    def get_all_languages_api(self, request):
        try:
            languages = Language.objects.all()
            serializer = self.serializer_class(languages, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            print("get_all_languages_api_error: ", error)
            return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action(detail=False, methods=['POST'], url_name='add_language_api', url_path='add_language_api')
    def add_language_api(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                model = serializer.add(request)
                if model:
                    return Response({"message": "Language added successfully"}, status=status.HTTP_201_CREATED)
                return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                # Trả về lỗi nếu dữ liệu không hợp lệ
                return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            print("add_language_api_error: ", error)
            return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)