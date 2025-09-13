from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from activity.models import Comment


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('caption', 'post', 'reply_to')

    def validate_caption(self, attr):
        if len(attr) > 30:
            raise ValidationError(_('your caption should not be longer than 30 characters'))
        return attr
    def validate_reply_to(self, attr):
        if attr.reply_to is not None:
            raise ValidationError(_('You cannot specify a reply to a post'))
        return attr

    def validate(self, attrs):
        attrs['created_time'] = timezone.now()
        return attrs

class CommentReplyListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')

    class Meta:
        model = Comment
        fields = ('id', 'caption')


class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    class Meta:
        model = Comment
        fields = ('id', 'user','caption', 'post', 'reply_to')
        read_only_fields = ('user',)
