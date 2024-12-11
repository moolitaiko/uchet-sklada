from rest_framework.permissions import BasePermission
from .models import Owner, Seller


class IsOwner(BasePermission):

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.user.is_staff or request.user.is_superuser:
                return True
            try:
                owner = Owner.objects.get(user=request.user.id)
                return True
            except Owner.DoesNotExist:
                return False

        return False


class IsSeller(BasePermission):

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.user.is_staff or request.user.is_superuser:
                return True
            try:
                seller = Seller.objects.get(user=request.user.id)
                return True
            except Seller.DoesNotExist:
                return False

        return False



