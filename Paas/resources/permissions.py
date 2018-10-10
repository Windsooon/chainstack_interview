from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    message = 'Only owner can access the resource.'

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_authenticated and obj.owner == request.user
