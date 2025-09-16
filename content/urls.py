from django.urls import path
from content.views import (
    TagListApi, TagDetailApi, PostDetailAPI,
    TagCreateApiview, UserPostViewSet
)

user_post_list = UserPostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

user_post_detail = UserPostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('tags/', TagListApi.as_view(), name='tags-list'),
    path('tags/create/', TagCreateApiview.as_view(), name='tags-create'),
    path('tag/<int:pk>/', TagDetailApi.as_view(), name='tags-detail'),

    path('user/<str:username>/post/', user_post_list, name='user-posts-list'),
    path('user/<str:username>/post/<int:pk>/', user_post_detail, name='user-posts-detail'),
]
