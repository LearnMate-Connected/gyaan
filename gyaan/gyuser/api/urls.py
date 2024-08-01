from django.urls import path

from gyuser.api.views import UserLoginViewset, PasswordViewset


urlpatterns = [
    path('user_signup/', UserLoginViewset.as_view({
        'post': 'user_signup'}), name='user_signup'),
    
    path('user_login/', UserLoginViewset.as_view({
        'put': 'username_login'}), name='username_login'),
     
    path('reset_password/', PasswordViewset.as_view({
        'put': 'reset_password'}), name='reset_password'),
    
]
