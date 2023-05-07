from typing import Any

from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsCustomerOrReadOnly(BasePermission):
    """Custom permission for customer."""

    def has_permission(self, request: Any, view: Any) -> bool:
        return (
            request.method in permissions.SAFE_METHODS
            or request.user
            and request.user.is_staff
        )

    def has_object_permission(self, request: Any, view: Any, obj: Any) -> bool:
        return (
            obj.user == request.user and request.user.is_customer
        ) or request.user.is_superuser


class IsCarShowroomOrReadOnly(BasePermission):
    """Custom permission for owner Car-Showroom."""

    def has_permission(self, request: Any, view: Any) -> bool:
        return (
            request.method in permissions.SAFE_METHODS
            or request.user
            and request.user.is_staff
        )

    def has_object_permission(self, request: Any, view: Any, obj: Any) -> bool:
        return (
            obj.user == request.user and request.user.is_car_showroom
        ) or request.user.is_superuser


class IsProviderOrReadOnly(BasePermission):
    """Custom permission for provider."""

    def has_permission(self, request: Any, view: Any) -> bool:
        return (
            request.method in permissions.SAFE_METHODS
            or request.user
            and request.user.is_staff
        )

    def has_object_permission(self, request: Any, view: Any, obj: Any) -> bool:
        return (
            obj.user == request.user and request.user.is_provider
        ) or request.user.is_superuser
