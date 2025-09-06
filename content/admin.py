from django.contrib import admin
from django.contrib.admin import register
from content.models import Post, PostMedia, Tag, PostTag, TaggedUser

@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('caption', 'user', 'location')


@register(PostMedia)
class PostMediaAdmin(admin.ModelAdmin):
    list_display = ("media_type",)






