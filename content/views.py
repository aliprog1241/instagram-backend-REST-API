from itertools import permutations
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from activity.serializers import LikeSerializer
from content.models import Tag, Post
from content.serializers import TagDetailSerializer, TagListSerializer, PostDetailSerializer
from lib.pagination import SmallPageNumberPagination
from lib.permissions import RelationExists
from rest_framework import throttling

# -------------------- TAG VIEWS --------------------

class TagDetailApi(APIView):
    def get(self, request, pk, *args, **kwargs):
        tag = get_object_or_404(Tag, pk=pk)
        serializer = TagDetailSerializer(tag)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TagListApi(APIView):
    def get(self, request, *args, **kwargs):
        tags = Tag.objects.all()
        serializer = TagListSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = TagListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class TagCreateApiview(APIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer


class TAglistApi(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = SmallPageNumberPagination


# -------------------- POST VIEWS --------------------

class PostDetailAPI(RetrieveAPIView):
    permission_classes = [IsAuthenticated, RelationExists]
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()


class UserPostListApiview(ListAPIView):
    queryset = Post.objects.all()
    lookup_url_kwarg = 'user_id'
    serializer_class = PostDetailSerializer
    pagination_class = SmallPageNumberPagination
    permission_classes = [IsAuthenticated, RelationExists]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user_id=self.kwargs[self.lookup_url_kwarg])


class UserPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    pagination_class = SmallPageNumberPagination
    permission_classes = [IsAuthenticated, RelationExists]
    throttle_classes = [UserRateThrottle]

    def get_queryset(self):
        qs = super().get_queryset()
        username = self.kwargs.get('username')
        if username:
            qs = qs.filter(user__username=username)
        return qs

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, RelationExists]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'get_likes_list':
            return LikeSerializer
        return self.serializer_class

    @action(detail=True, methods=['get'])
    def get_likes_list(self, request, *args, **kwargs):
        post = self.get_object()
        queryset = post.likes.all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
