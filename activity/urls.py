from django.urls import path
from activity.views import CommentListCreatAPIView, CommentRetrieveAPIView

urlpatterns = [
    path('comment/create/', CommentListCreatAPIView.as_view(), name='comment-create'),
    path('comment/retrieve/<int:pk>/', CommentRetrieveAPIView.as_view(), name='comment-retrieve'),
]
