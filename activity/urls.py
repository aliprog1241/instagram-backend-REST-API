from django.urls import path

from activity.views import CommentCreatApiView

urlpatterns = [
    path('comment/create/', CommentCreatApiView.as_view(), name='comment-create'),

]