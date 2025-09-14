from http.client import responses

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from activity.models import Comment, Like
from activity.serializer import CommentCreateSerializer, CommentListSerializer, PostLikeSerializer
from lib.permissions import HasPostPermissions


class CommentListCreatAPIView(ListCreateAPIView):
    queryset = Comment.objects.filter(reply_to__isnull=True)
    serializer_class = CommentCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GEt':
            return CommentListSerializer

        return self.serializer_class
class LikeListCreatAPIView(RetrieveAPIView):
    queryset = Like.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = [IsAuthenticated, HasPostPermissions]

    def post(self, request, pk, *args, **kwargs):
        object = self.get_object()
        return Response()

class CommentRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.serializer_class
        return CommentCreateSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)
