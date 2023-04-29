from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsCustomerOrReadOnly(BasePermission):
    """Custom permission for customer."""

    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS or request.user and request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user and request.user.is_customer:
            return True
        return False


class IsCarShowroomOrReadOnly(BasePermission):
    """Custom permission for owner Car-Showroom."""

    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS or request.user and request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user and request.user.is_car_showroom:
            return True
        return False


class IsProviderOrReadOnly(BasePermission):
    """Custom permission for provider."""

    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS or request.user and request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user and request.user.is_provider:
            return True
        return False
