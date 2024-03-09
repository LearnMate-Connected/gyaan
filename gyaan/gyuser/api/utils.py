from django.db import transaction
from django.utils import timezone

from _gybase.validators import Validators

from data_utils import UserDataUtils, ProfileDataUtils




class UserProfileLoginUtils:
    user_data_class = UserDataUtils()
    profile_data_class = ProfileDataUtils()
    
    def user_signup(self, request, **kwargs):
        first_name = kwargs.get("first_name")
        if not first_name or not isinstance(first_name, str):
            return {"error": "Please send valid first name"}, 400
        if len(first_name) > 50:
            return {"error": "Please send first name within 50 chars"}, 400
        last_name = kwargs.get("last_name")
        if last_name and not isinstance(first_name, str):
            return {"error": "Please send valid last name"}, 400
        if len(last_name) > 50:
            return {"error": "Please send last name within 50 chars"}, 400
        email = kwargs.get("email")
        if not email or not isinstance(email, str) or Validators.email_validator(email):
            return {"error": "Please send valid email"}, 400
        phone = kwargs.get("phone")
        if not phone or not Validators.phone_validator(phone):
            return {"error": "Please send valid phone number"}, 400
        username = kwargs.get("username")
        if not username or not isinstance(username, str):
            return {"error": "Please send a valid phone number"}, 400
        password = kwargs.get("password")
        if not password or Validators.password_validator(password):
            return {"error": "Please send valid password"}, 400
        if self.user_data_class(**{"username": username}):
            return {"error": "User with username {} already exists".format(username)}, 400
        if self.user_data_class(**{"email": email}):
            return {"error": "User with email {} already exists".format(email)}, 400
        if self.profile_data_class(**{"phone": phone}):
            return {"error": "User with email {} already exists".format(email)}, 400
        crt_user = {"username": username, "email": email,
            "first_name": first_name, "last_name": last_name}
        with transaction.atomic():
            created_user = self.data_class.create_user(**crt_user)
            created_user.set_password = password
            created_user.save(["password"])
            profile = created_user.profile
            profile.phone = phone
            profile.update_at = timezone.now()
            profile.save(update_fields = ["updated_at", "phone"])
        #TODO: 
        return {"username": username, "password": password}, 200
    
    def username_login(self, request, **kwargs):
        pass
    
    def reset_password(self, request, **kwargs):
        pass