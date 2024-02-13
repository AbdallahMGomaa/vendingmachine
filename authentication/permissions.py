from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import BasePermission

from authentication.models import Role


class IsBuyerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user is None or isinstance(request.user, AnonymousUser):
            return False
        roles = Role.objects.filter(user=request.user, name=Role.RoleNames.BUYER)
        return roles


class IsSellerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user is None or isinstance(request.user, AnonymousUser):
            return False
        roles = Role.objects.filter(user=request.user, name=Role.RoleNames.SELLER)
        return roles
