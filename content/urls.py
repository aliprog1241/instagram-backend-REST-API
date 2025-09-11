from django.urls import path

from content.views import TagListApi, TagDetailApi, PostDetailAPI, TagCreateApiview

urlpatterns = [
    path('tags/', TagListApi.as_view(), name='tags-list'),
    path('tags/create/', TagCreateApiview.as_view(), name='tags-create'),
    path('tag/<int:pk>/', TagDetailApi.as_view(), name='tags-detail'),
    path('post/<int:pk>/', PostDetailAPI.as_view(), name='posts-detail'),
]