from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SnippetView

snippet_list = SnippetView.as_view({
    'post': 'create',
    'get': 'list'
})

snippet_detail = SnippetView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


# URL Patterns
urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('snippets/', snippet_list, name='snippet_list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet_detail'),
])