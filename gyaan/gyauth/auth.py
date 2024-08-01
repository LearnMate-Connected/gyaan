import binascii

from django.db import DatabaseError
from django.utils import timezone
from django.conf import settings
from rest_framework import exceptions
from rest_framework.authentication import (
    BaseAuthentication, TokenAuthentication, get_authorization_header)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.backends import TokenBackend

try:
    from hmac import compare_digest
except ImportError:
    def compare_digest(a, b):
        return a == b


# class UserAuthTokenAuthentication(BaseAuthentication):
#     """
#     This authentication scheme uses Knox AuthTokens for authentication.
#     Similar to DRF TokenAuthentication, it overrides a large amount of that
#     authentication scheme to cope with the fact that Tokens are not stored
#     in plaintext in the database
#     If successful
#     - `request.user` will be a django `User` instance
#     - `request.auth` will be an `AuthToken` instance
#     """
#
#     def authenticate(self, request):
#         auth = get_authorization_header(request).split()
#         prefix = settings.AUTH_HEADER_PREFIX.encode()
#         if not auth:
#             return None
#         if auth[0].lower() != prefix.lower():
#             # Authorization header is possibly for another backend
#             return None
#         if len(auth) == 1:
#             raise exceptions.AuthenticationFailed(
#                 detail='You are not allowed to perform this operation')
#         elif len(auth) > 2:
#             raise exceptions.AuthenticationFailed(
#                 detail='Invalid Token, key should not contained spaces')


class UserAuthTokenAuthentication(JWTAuthentication):
    def get_header(self, request):
        """
        Extracts the 'Authorization' header from the given request.
        """
        header = request.headers.get('Authorization')

        if header is None:
            return None
        print("in UserAuthTokenAuthentication====", header)
        # Instead of "Bearer", use "Token"
        if isinstance(header, str) and header.startswith('Token '):
            return "Bearer {}".format(header.split('Token ')[1])

        return None


