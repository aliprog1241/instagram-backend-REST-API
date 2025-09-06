from django.contrib import admin
from django.contrib.admin import register
from relation.models import Relation

@register(Relation)
class RelationAdmin(admin.ModelAdmin):
    list_display = ("from_user", "to_user")

