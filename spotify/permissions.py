from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsArtistOrReadOnly(BasePermission):

    def has_permission(self, request, view):

    
        if request.method in SAFE_METHODS:
            return True

    
        return (
            request.user.is_authenticated
            and request.user.role == "artist"
        )

    def has_object_permission(self, request, view, obj):

        
        if request.method in SAFE_METHODS:
            return True

        if hasattr(obj, "albums"):
            return obj.albums.artist == request.user


        if hasattr(obj, "artist"):
            return obj.artist == request.user

        return False

class IsAuthenticatedReadOnly(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.method in SAFE_METHODS
        )