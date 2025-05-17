from rest_framework import serializers
from api.models import *
from rest_framework.parsers import MultiPartParser, FormParser

class ProjectDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    project_id = serializers.IntegerField(required=False)

    class Meta:
        model = ProjectDetail
        fields = ['id', 'name_type', 'date', 'description_long', 'link_be', 'link_fe', 'features', 'project_id']

    
class LanguageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Language
        fields = ['id', 'name']

    def add(self, request):
        try: 
            name = request.data['name']
            project_id = request.data['project']  # Lấy ID của project từ dữ liệu
            project = Project.objects.get(id=project_id)  # Lấy đối tượng Project từ ID

            return Language.objects.create(
                name=name,
                project=project
            )
        except KeyError as e:
            print(f"LanguageSerializer_add_error: Missing field {e}")
            return None
        except Project.DoesNotExist:
            print("LanguageSerializer_add_error: Project does not exist")
            return None
        except Exception as error:
            print("LanguageSerializer_add_error: ", error)
            return None
    
    def delete(self, request):
        try:
            id = request.data['id']
            language = Language.objects.get(id=id)
            language.delete()
            return True
        except Exception as error:
            print("LanguageSerializer_delete_error: ", error)
            return False
        
    def update(self, request):
        try:
            id = request.data['id']
            name = request.data['name']
            project_id = request.data['project_id']
            language = Language.objects.get(id=id)
            language.name = name
            language.project_id = project_id
            language.save()
            return True
        except Exception as error:
            print("LanguageSerializer_update_error: ", error)
            return False
        
class ProjectSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    languages = LanguageSerializer(many=True, read_only=True)
    project_details = ProjectDetailSerializer(many=True, read_only=True)
    parser_classes = [MultiPartParser, FormParser] 

    class Meta:
        model = Project
        fields = ['id', 'name', 'image', 'description', 'link', 'created_at', 'updated_at', 'languages', 'project_details']

    def add(self, request):
        try: 
            name = request.data['name']
            image = request.data['image']
            description = request.data['description']
            link = request.data['link']
            return Project.objects.create(
                name=name,
                image=image,
                description=description,
                link=link
            )
        except Exception as error:
            print("ProjectSerializer_add_error: ", error)
            return None
        
    def delete(self, request):
        try:
            id = request.data['id']
            project = Project.objects.get(id=id)
            project.delete()
            return True
        except Exception as error:
            print("ProjectSerializer_delete_error: ", error)
            return False
        
    def update(self, request):
        try:
            id = request.data['id']
            name = request.data['name']
            image = request.data['image']
            description = request.data['description']
            link = request.data['link']
            project = Project.objects.get(id=id)
            project.name = name
            project.image = image
            project.description = description
            project.link = link
            project.save()
            return True
        except Exception as error:
            print("ProjectSerializer_update_error: ", error)
            return False
