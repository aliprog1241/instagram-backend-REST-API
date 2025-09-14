from django.urls import path
from content.views import (
    TagListApi, TagDetailApi, PostDetailAPI, TagCreateApiview,
    UserPostListApiview, UserPostReadOnlyViewSet
)

user_post_detail = UserPostReadOnlyViewSet.as_view({'get': 'retrieve'})
user_post_list = UserPostReadOnlyViewSet.as_view({'get': 'list'})

urlpatterns = [
    path('tags/', TagListApi.as_view(), name='tags-list'),
    path('tags/create/', TagCreateApiview.as_view(), name='tags-create'),
    path('tag/<int:pk>/', TagDetailApi.as_view(), name='tags-detail'),

    path('user/<str:username>/posts/', user_post_list, name='user-posts-list'),
    path('user/<str:username>/posts/<int:pk>/', user_post_detail, name='user-posts-detail'),
]
