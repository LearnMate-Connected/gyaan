from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from gyuser.api.utils import UserProfileLoginUtils


class UserLoginViewset:
    view_class = UserProfileLoginUtils()
    
    def username_login(self, request, **kwargs):
        resp, status_code = self.view_class.username_login(request, **kwargs)
        return Response(resp, status=status_code)
    
    def user_signup(self, request):
        resp, status_code = self.view_class.user_signup(request, **kwargs)
        return Response(resp, status=status_code)
    
    def reset_password(self, request, **kwargs):
        resp, status_code = self.view_class.reset_password(request, **kwargs)
        return Response(resp, status=status_code)