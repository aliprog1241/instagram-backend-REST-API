from django.urls import path

from content.views import TagListApi, TagDetailApi

urlpatterns = [
    path('tags/', TagListApi.as_view(), name='tags-list'),
    path('tag/<int:pk>/', TagDetailApi.as_view(), name='tags-detail'),
]