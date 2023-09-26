from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('file/', views.SnippetList.as_view()),
    path('file/<int:pk>/', views.SnippetDetail.as_view()),
    path('version/', views.VersionView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)