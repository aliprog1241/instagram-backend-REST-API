
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from content.models import Tag



class TagDetailApi(APIView):
    def get(self, request, pk, *args, **kwargs):
        tags = Tag.objects.filter(pk=pk)

        if not tags.exists():
            return Response('not found',status=status.HTTP_404_NOT_FOUND)

        tag = tags.first()

        return Response(
            {
                'id': tag.id,
                'title': tag.title,
                'posts': tag.posts.count(),
            },   status=status.HTTP_200_OK)


class TagListApi(APIView):

    def get(self,request, *args, **kwargs):
        tags = Tag.objects.all()


        data = list()
        for tag in tags:
            data.append({
                'id': tag.id,
                'title': tag.title,
                'posts': tag.posts.count(),
            })

        return Response(data, status=status.HTTP_200_OK)
