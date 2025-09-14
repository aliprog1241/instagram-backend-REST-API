from django.urls import path
from activity.views import CommentListCreatAPIView, CommentRetrieveAPIView, LikeListCreatAPIView

urlpatterns = [
    path('comment/create/', CommentListCreatAPIView.as_view(), name='comment-create'),
    path('like/<int:pk>/create/', LikeListCreatAPIView.as_view(), name='like-create'),
    path('comment/retrieve/<int:pk>/', CommentRetrieveAPIView.as_view(), name='comment-retrieve'),
]
