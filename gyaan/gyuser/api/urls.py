from django.urls import path

from gyuser.views import UserLoginViewset


urlpatterns = [
    path('user_signup/', UserLoginViewset.as_view({
        'put': 'user_signup'}), name='user_signup'),
    
    path('username_login/', UserLoginViewset.as_view({
        'put': 'username_login'}), name='username_login'),
     
    path('reset_password/', UserLoginViewset.as_view({
        'put': 'reset_password'}), name='reset_password'),
    
]
