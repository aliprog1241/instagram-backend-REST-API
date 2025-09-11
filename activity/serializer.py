from rest_framework import serializers

from activity.models import Comment


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('caption', 'post', 'reply_to')
