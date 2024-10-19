from rest_framework import permissions


class IsManager(permissions.BasePermission):
    """
    Custom permission to only allow managers to access certain views.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.userprofile.role == 'Manager'


class IsOperatorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow operators and managers
    to access certain views.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.userprofile.role == 'Manager' or request.user.userprofile.role == 'Operator')
