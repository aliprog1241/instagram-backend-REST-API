from rest_framework.permissions import BasePermission
from  relation.models import Relation



class RelationExists(BasePermission):
    def has_permission(self, request, view):
        Relation.oblects.filter(from_user=request.user, to_user=view.kwargs['user_id']).exists()
        return True