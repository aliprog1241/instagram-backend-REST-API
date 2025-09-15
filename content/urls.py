from django.urls import path, include

from rest_framework.routers import SimpleRouter

from content.views import TagListApi, TagDetailApi, PostDetailAPI, TagCreateApiview,UserPostListApiview, UserPostViewSet


router = SimpleRouter()
router.register('post', UserPostViewSet, basename='user-post')

# user_post_detail = UserPostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})
# user_post_list = UserPostViewSet.as_view({'get': 'list', 'post': 'create'})


urlpatterns = [
    path('tags/', TagListApi.as_view(), name='tags-list'),
    path('tags/create/', TagCreateApiview.as_view(), name='tags-create'),
    path('tag/<int:pk>/', TagDetailApi.as_view(), name='tags-detail'),

#     path('user/<str:username>/posts/', user_post_list, name='user-posts-list'),
    path('user/<str:username>/', include(router.urls)),
]
