from rest_framework import serializers
from .models import Snippet, Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'description', 'pub_date')

class SnippetSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    class Meta:
        model = Snippet
        fields = (
            'project',
            'file_name',
            'language',
            'style',
            'linenos',
            'snippet',
            'created_at',
        )
        read_only_fields = ('file_name','created_at',)