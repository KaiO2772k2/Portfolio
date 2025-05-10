from rest_framework import serializers
from api.models import *

class ProjectSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Project
        fields = '__all__'

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

    
class LanguageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Language
        fields = '__all__'

    def add(self, request):
        try: 
            name = request.data['name']
            project_id = request.data['project_id']
            return Language.objects.create(
                name=name,
                project_id=project_id
            )
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