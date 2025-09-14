from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from activity.models import Comment
from content.models import Post


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('caption', 'post', 'reply_to')

    def validate_caption(self, attr):
        if len(attr) > 30:
            raise ValidationError(_('your caption should not be longer than 30 characters'))
        return attr

    def validate_reply_to(self, attr):

        if attr and attr.reply_to is not None:
            raise ValidationError(_('You cannot reply to a reply'))
        return attr

    def validate(self, attrs):
        attrs['created_time'] = timezone.now()
        return attrs


class CommentRepliesListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')

    class Meta:
        model = Comment
        fields = ('id', 'caption', 'user')


class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'user', 'caption', 'replies')

    def get_replies(self, obj):
        qs = obj.replies.all()[:10]
        serializer = CommentRepliesListSerializer(qs, many=True)
        return serializer.data


class PostLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('post' ,)
