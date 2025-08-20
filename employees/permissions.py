# employee_app/permissions.py
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission: 
    - Admin users (is_staff=True) → full access (GET, POST, PUT, DELETE)
    - Non-admin users → read-only (GET, HEAD, OPTIONS)
    """

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            # Admin → allow everything
            if request.user.is_staff:
                return True
            # Normal user → only safe (read) methods
            return request.method in permissions.SAFE_METHODS
        return False
