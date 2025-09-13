from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from activity.models import Comment
from content.serializers import PostDetailSerializer


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('caption', 'post', 'reply_to')

    def validate_caption(self, attrs):
        if len(attrs['caption']) > 30:
            raise ValidationError(_('your caption should not be longer than 30 characters'))
        return attrs
    def validate_reply_to(self, attr):
        if attr.reply_to is not None:
            raise ValidationError(_('You cannot specify a reply to a post'))
        return attr

    def validate(self, attrs):
        return attrs


class CommentListSerializer(serializers.ModelSerializer):
    post = PostDetailSerializer()
    user = serializers.CharField(source='user.username')
    class Meta:
        model = Comment
        fields = ('id', 'user','caption', 'post', 'reply_to')
        read_only_fields = ('user',)
