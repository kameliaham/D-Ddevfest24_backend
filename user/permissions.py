from rest_framework.permissions import BasePermission

class IsManager(BasePermission):
    """
    Custom permission to only allow managers to access certain views.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.userprofile.role == 'Manager'
    

