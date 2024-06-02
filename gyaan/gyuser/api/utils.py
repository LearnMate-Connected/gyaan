from django.db import transaction
from django.db.models import Q
from django.utils import timezone

from _gybase.api.utils import BaseApiUtils
from _gybase.validators import Validators

from gyuser.api.data_utils import UserDataUtils, ProfileDataUtils, ApprovalDataUtils

from gyuser.constants import PENDING, APPROVED, REJECTED, APPROVAL_STATUS_CHOICES


class UserProfileLoginUtils:
    user_data_class = UserDataUtils()
    profile_data_class = ProfileDataUtils()
    
    def user_signup(self, **kwargs):
        first_name = kwargs.get("first_name")
        if not first_name or not isinstance(first_name, str):
            return {"error": "Please send valid first name"}, 400
        if len(first_name) > 50:
            return {"error": "Please send first name within 50 chars"}, 400
        last_name = kwargs.get("last_name")
        if last_name and not isinstance(first_name, str) and len(last_name) > 50:
            return {"error": "Please send valid last name"}, 400
        email = kwargs.get("email")
        if (not email or not isinstance(email, str) or
                not Validators.email_validator(email)):
            return {"error": "Please send valid email"}, 400
        phone = kwargs.get("phone")
        if not phone or not Validators.phone_validator(phone):
            return {"error": "Please send valid phone number"}, 400
        username = kwargs.get("username")
        if not username or not isinstance(username, str):
            return {"error": "Please send a valid phone number"}, 400
        password = kwargs.get("password")
        if not password or not Validators.password_validator(password):
            return {"error": "Please send valid password"}, 400
        user_exist = self.user_data_class.filter_model(
            q=Q(username=username) | Q(email=email)).exists()
        if user_exist:
            return {"error": "User with entered details already exists"}, 400
        crt_user = {"username": username, "email": email,
                    "first_name": first_name, "last_name": last_name,
                    "is_staff": kwargs.get("is_staff", False),
                    "is_superuser": kwargs.get("is_superuser", False)}
        with transaction.atomic():
            created_user = self.user_data_class.create(**crt_user)
            created_user.set_password = password
            profile = created_user.profile
            created_user.save()
            profile.phone = phone
            profile.update_at = timezone.now()
            profile.save(update_fields = ["updated_at", "phone"])
        #TODO: Some logic to send the username and password to user email or phone
        #TODO: Remove sending password before going live
        return {"username": username, "password": password}, 200
    
    def username_login(self, user, **kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")
        if not (username and password):
            return {"error": "Please enter valid details and try again"}, 400
        if not Validators.password_validator(password):
            return {"error": "Please send a valid password"}, 400
        profile = self.profile_data_class.get(**{"username": "username"})
        if not profile:
            return {"error": "Please signup and try again"}, 400
        user = self.user_data_class.get(**{"username": username})
        if not user:
            return {"error": "User doesn't exist with username {}".format(username)}, 400
        if not (profile.block and user.is_active):
            return {"error": "This user is blocked or incativated. Please contact support team."}, 400
        if not user.check_password(username, password):
            return {"error": "Please enter valid username/password"}, 400
        
        user_dict = self.profile_data_class.get_fields_as_dict(user)
        profile_dict = self.user_data_class.get_fields_as_dict(profile)
        response = {**user_dict, **profile_dict}
        return response, 200
        

    def reset_password(self, user, **kwargs):
        username = kwargs.get("username")
        if not username or not isinstance(username, str):
            return {"error": "Please send a valid phone number"}, 400
        email = kwargs.get("email")
        if not email or not isinstance(email, str) or Validators.email_validator(email):
            return {"error": "Please send valid email"}, 400
        profile = self.profile_data_class.get(**{"username": "username"})
        user = self.user_data_class.get(**{"username": username})
        if not (user and profile):
            return {"error": "User doesn't exist with username {}".format(username)}, 400
        if not (profile.block and user.is_active):
            return {"error": "This user is blocked or incativated. Please contact support team."}, 400
        #TODO: Logic to send verification mail
        
        password = kwargs.get("password")
        if not password or Validators.password_validator(password):
            return {"error": "Please send valid password"}, 400
        user.set_password()
        user.updated_at = timezone.now()
        user.save(["password", "updated_at"])
        return {"message": "Password updated successfully",
                "username": username, "password": password}, 200
        

class PublisherApprovalUtils:
    
    user_data_class = UserDataUtils
    approval_data_class =ApprovalDataUtils
    
    def create_publisher_approval(self, user, **kwargs):
        if not user:
            return {"error": "Please send a valid user"}, 400
        email = kwargs.get("email")
        if not email:
            return {"error": "Please enter valid email id"}, 400
        username = kwargs.get("username")
        if not username:
            return {"error": "Please enter valid username"}, 400
        document_folder_link = kwargs.get("folder_link")
        if not document_folder_link:
            return {"error": "Please upload folder link containing required documents"}, 400
        user = self.user_data_class.get(**{"username": username})
        if not user:
            return {"error": "Please signup with username {}".format(username)}, 400
        if not (user.is_active and user.profile.block):
            return {"error": "This user is blocked or incativated. Please contact support team."}, 400
        self.approval_data_class.create(**{"user": user, "status": PENDING,
                                      "document_folder_link": document_folder_link})
        return {"message": "Approval for publisher status is created"}, 200
   
    def update_publisher_approval_status(self, user, **kwargs):
        approval_id = kwargs.get("approval_id")
        if not approval_id:
            return {"error": "Please send valid approval id"}, 400
        status = kwargs.get("status")
        if status not in dict(APPROVAL_STATUS_CHOICES):
            return {"error": "{} can't be status for approval".format(status)}, 400
        approval = self.approval_data_class.get(**{"id": approval_id})
        if not approval:
            return {"error": "There is no approval in system for approval id {}".format(approval_id)}, 400
        if approval._status in [APPROVED, REJECTED]:
            return {"error": "This request is already {}".format(approval.status)}, 400
        approval.status = status
        user_updated_fields = []
        if status == APPROVED:
            user.is_publisher = True
            user.updated_at = timezone.now()
            user_updated_fields.append("is_publisher")
        approval.updated_at = timezone.now()
        approval.approved_by = user.id
        approval.remarks = kwargs.get("remarks")
        with transaction.atomic:
            approval.save(["status", "approved_by", "updated_at"])
            if user_updated_fields:
                user_updated_fields.save(user_updated_fields)
        return {"message": "User request is {}d for publisher".format(status)}, 200
    
    def get_paginated_publisher_approval(self, page_number, limit, user, **kwargs):
        status = kwargs.get("status")
        if status and status not in dict(APPROVAL_STATUS_CHOICES):
            return {"error": "Invalid status"}, 400
        f_dict = {}
        if status:
            f_dict["status"] = status
        username = kwargs.get("username")
        if username:
            f_dict["username"] = username
        email = kwargs.get("email")
        if email:
            f_dict["email"] = email
        queryset = self.approval_data_class.filter_model(**f_dict).values(
            "user__username", "document_folder_link", "status", "approved_by", "remarks")
        paginated_data, pagination = BaseApiUtils.get_paginator(
            page_number, queryset, limit=limit
        )
        data = dict(data=paginated_data, pagination=pagination)
        return data, 200
    
    
        
            
                    
            