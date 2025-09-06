from django.urls import path

from content.views import TagListApi

urlpatterns = [
    path('tags/', TagListApi.as_view(), name='tags-list'),
]