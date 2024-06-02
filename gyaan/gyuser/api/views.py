from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from gyuser.api.utils import UserProfileLoginUtils, PublisherApprovalUtils


class UserLoginViewset(ViewSet):
    view_class = UserProfileLoginUtils()
    
    def username_login(self, request):
        resp, status_code = self.view_class.username_login(request.user, **request.data)
        return Response(resp, status=status_code)
    
    def user_signup(self, request):
        resp, status_code = self.view_class.user_signup(**request.data)
        return Response(resp, status=status_code)
    
    def reset_password(self, request):
        resp, status_code = self.view_class.reset_password(request.user, **request.data)
        return Response(resp, status=status_code)


class PublisherApprovalViewset(ViewSet):
    view_class = PublisherApprovalUtils
    
    def create_publisher_approval(self, request):
        resp, status_code = self.view_class.create_publisher_approval(
            request.user,**request.data)
        return Response(resp, status=status_code)
    
    def update_publisher_approval_status(self, request):
        resp, status_code = self.view_class.update_publisher_approval_status(
            request.user, **request.data)
        return Response(resp, status=status_code)
    
    def get_paginated_publisher_approval(self, request):
        data = request.query_params.dict()
        page_number = data.pop('page', 1)
        limit = data.pop('limit', 10)
        resp, status_code = self.view_class.get_paginated_publisher_approval(
            page_number, limit, request.user, **data)
        return Response(resp, status=status_code)
