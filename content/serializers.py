from rest_framework import serializers

from content.models import Tag


class TagListSerializer(serializers.Serializer):
    title = serializers.CharField()
    id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        instance = Tag.objects.create(**validated_data)
        return instance

class TagDetailSerializer(TagListSerializer):
    posts = serializers.SerializerMethodField()


    def get_posts(self, obj):

        return obj.posts.count()