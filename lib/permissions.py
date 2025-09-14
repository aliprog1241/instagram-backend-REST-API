from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission
from  relation.models import Relation

User = get_user_model()

class RelationExists(BasePermission):
    def has_permission(self, request, view):
        user = User.objects.filter(id=view.kwargs['user_id']).first()
        if user:

            relation_exists = Relation.objects.filter(from_user=request.user, to_user=view.kwargs['user_id']).exists()
            return relation_exists

        return False