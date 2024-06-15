from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet


class NoAuthViewSet(ViewSet):

    class Meta:
        abstract = True


class SessionAuthViewSet(ViewSet):

    authentication_classes = (SessionAuthentication, )
    permission_classes = (IsAuthenticated, )

    class Meta:
        abstract = True


class AllAuthViewSet(ViewSet):
    #TODO: To be added
    authentication_classes = SessionAuthentication
    permission_classes = (IsAuthenticated, )

    class Meta:
        abstract = True

