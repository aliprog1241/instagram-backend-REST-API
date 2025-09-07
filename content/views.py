from gc import get_objects

from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from content.models import Tag
from content.serializers import TagDetailSerializer, TagListSerializer


class TagDetailApi(APIView):
    def get(self, request, pk, *args, **kwargs):
        tag = get_object_or_404(Tag, **{'pk':pk})
        serializer = TagDetailSerializer(tag, many=False)
        return Response( serializer.data, status=status.HTTP_200_OK)


class TagListApi(APIView):

    def get(self,request, *args, **kwargs):
        tags = Tag.objects.all()

        #wrong way!!!!!
        # data = list()
        # for tag in tags:
        #     data.append({
        #         'id': tag.id,
        #         'title': tag.title,
        #         'posts': tag.posts.count(),
        #     })
        serializer = TagListSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self,request, *args, **kwargs):
        tags = Tag.objects.all()
        serializer = TagListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)