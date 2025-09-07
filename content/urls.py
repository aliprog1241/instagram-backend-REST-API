from django.urls import path

from content.views import TagListApi, TagDetailApi, PostDetailAPI

urlpatterns = [
    path('tags/', TagListApi.as_view(), name='tags-list'),
    path('tag/<int:pk>/', TagDetailApi.as_view(), name='tags-detail'),
    path('post/<int:pk>/', PostDetailAPI.as_view(), name='posts-detail'),
]