from rest_framework import serializers

from activity.models import Comment
from content.serializers import PostDetailSerializer


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('caption', 'post', 'reply_to')

class CommentListSerializer(serializers.ModelSerializer):
    post = PostDetailSerializer()
    user = serializers.CharField(source='user.username')
    class Meta:
        model = Comment
        fields = ('id', 'user','caption', 'post', 'reply_to')
        read_only_fields = ('user',)
