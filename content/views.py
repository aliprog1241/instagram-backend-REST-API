
from rest_framework.views import APIView
from rest_framework.response import Response

from content.models import Tag




class TagListApi(APIView):

    def get(self,request, *args, **kwargs):
        tags = Tag.objects.all().values('title')
        return Response(tags)

