from django.contrib import admin
from django.contrib.admin import register
from activity.models import Comment,Like

@register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ("caption", "user","post", "reply_to")


@register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user","post")

