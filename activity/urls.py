from django.urls import path

from activity.views import CommentListCreatAPIView

urlpatterns = [
    path('comment/create/', CommentListCreatAPIView.as_view(), name='comment-create'),

]