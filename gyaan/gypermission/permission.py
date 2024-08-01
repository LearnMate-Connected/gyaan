from rest_framework.permissions import IsAuthenticated


class DummyPermission(IsAuthenticated):
    def has_permission(self, request, view):
        print(request.user.id)
        print("AUthenticated======", request.user.is_authenticated)
        return bool(request.user and request.user.is_authenticated)