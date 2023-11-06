from rest_framework import (
    permissions,
)


class AuthorOrReadOnly(permissions.BasePermission):
    """
    All users have permission to view data
    Only authenticated users can create an object
    Only the author has permission to modify or delete an object
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated or request.method in permissions.SAFE_METHODS

    def has_object_permission(
        self,
        request,
        view,
        obj,
    ):
        return obj.author == request.user or request.method in permissions.SAFE_METHODS
