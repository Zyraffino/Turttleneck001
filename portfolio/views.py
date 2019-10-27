from django.shortcuts import render

from rest_framework import viewsets
from .serializers import SnippetSerializer
from .models import Snippet
from rest_framework import permissions

# Create your views here.
class SnippetView(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save()