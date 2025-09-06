from django.contrib import admin
from django.contrib.admin import register
from location.models import  Location

@register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("title", "points")





