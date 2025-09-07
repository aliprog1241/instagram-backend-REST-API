from rest_framework import serializers





class TagListSerializer(serializers.Serializer):
    title = serializers.CharField()
    id = serializers.IntegerField()

class TagDetailSerializer(TagListSerializer):
    posts = serializers.SerializerMethodField()


    def get_posts(self, obj):

        return obj.posts.count()