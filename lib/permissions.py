from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission
from  relation.models import Relation

User = get_user_model()

class RelationExists(BasePermission):

    message = "you have not followed this account"
    def has_permission(self, request, view):
        return  Relation.objects.filter(from_user=request.user, to_user__username=view.kwargs['username']).exists()



class HasPostPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):

        return Relation.objects.filter(from_user=request.user, to_user=obj.user).exists() | request.user == obj.user
