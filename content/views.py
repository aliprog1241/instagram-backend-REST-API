from gc import get_objects

from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

from content.models import Tag, Post
from content.serializers import TagDetailSerializer, TagListSerializer, PostDetailSerializer
from lib.pagination import SmallPageNumberPagination, StandardPagination


class TagDetailApi(APIView):
    def get(self, request, pk, *args, **kwargs):
        tag = get_object_or_404(Tag, **{'pk':pk})
        serializer = TagDetailSerializer(tag, many=False)
        return Response( serializer.data, status=status.HTTP_200_OK)


class TagListApi(APIView):

    def get(self,request, *args, **kwargs):
        tags = Tag.objects.all()
        serializer = TagListSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self,request, *args, **kwargs):
        tags = Tag.objects.all()
        serializer = TagListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class TAglistApi(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer
    permission_classes = (IsAuthenticated, )
    pagination_class = SmallPageNumberPagination


class TagCreateApiview(APIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer


class PostDetailAPI(APIView):
    def get(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Post, **{'pk':pk})
        serializer = PostDetailSerializer(instance)
        return Response(serializer.data)


class UserPostListApiview(ListAPIView):
    queryset = Post.objects.all()
    lookup_url_kwarg = 'user_id'
    serializer_class = PostDetailSerializer
    pagination_class = StandardPagination
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user_id=self.kwargs[self.lookup_url_kwarg])
