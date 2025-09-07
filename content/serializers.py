from rest_framework import serializers

from content.models import Tag, Post
from location.serializers import LocationSerializer


#
# class TagListSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     id = serializers.IntegerField(read_only=True)
#
#     def create(self, validated_data):
#         instance = Tag.objects.create(**validated_data)
#         return instance
#
# class TagDetailSerializer(TagListSerializer):
#     posts = serializers.SerializerMethodField()
#
#
#     def get_posts(self, obj):
#
#         return obj.posts.count()

class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','title')


class TagDetailSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()
    class Meta:
        model = Tag
        fields = ('id','title')

    def get_posts(self, obj):
        return obj.posts.count()




class PostDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    location = LocationSerializer()




    class Meta:
        model = Post
        fields = ('caption','user', 'location')