from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from gyuser.api.utils import UserProfileLoginUtils, PublisherApprovalUtils


class UserLoginViewset:
    view_class = UserProfileLoginUtils()
    
    def username_login(self, request, **kwargs):
        resp, status_code = self.view_class.username_login(request.user, **kwargs)
        return Response(resp, status=status_code)
    
    def user_signup(self, request, **kwargs):
        resp, status_code = self.view_class.user_signup(**kwargs)
        return Response(resp, status=status_code)
    
    def reset_password(self, request, **kwargs):
        resp, status_code = self.view_class.reset_password(request.user, **kwargs)
        return Response(resp, status=status_code)

class PublisherApprovalViewset:
    view_class = PublisherApprovalUtils
    
    def create_publisher_approval(self, request, **kwargs):
        resp, status_code = self.view_class.create_publisher_approval(
            request.user, **kwargs)
        return Response(resp, status=status_code)
    
    def update_publisher_approval_status(self, request, **kwargs):
        resp, status_code = self.view_class.update_publisher_approval_status(
            request.user, **kwargs)
        return Response(resp, status=status_code)
    
    def get_paginated_publisher_approval(self, request, **kwargs):
        data = request.query_params.dict()
        page_number = data.pop('page', 1)
        limit = data.pop('limit', 10)
        resp, status_code = self.view_class.get_paginated_publisher_approval(
            page_number, limit, request.user, **kwargs)
        return Response(resp, status=status_code)
