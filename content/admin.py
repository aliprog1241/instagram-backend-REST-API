from django.contrib import admin
from django.contrib.admin import register
from content.models import Post, PostMedia, Tag, PostTag, TaggedUser

@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('caption', 'user', 'location')


@register(PostMedia)
class PostMediaAdmin(admin.ModelAdmin):
    list_display = ("media_type",)


@register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("title",)


@register(PostTag)
class PostTagAdmin(admin.ModelAdmin):
    list_display = ("tag",)

@register(TaggedUser)
class TaggedUserAdmin(admin.ModelAdmin):
    list_display = ("user",)



