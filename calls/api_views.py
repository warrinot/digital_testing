from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from calls.models import Call
from calls.serializers import CallSerializer


class CallApiViewSet(viewsets.ModelViewSet):
    queryset = Call.objects.all()
    serializer_class = CallSerializer
    authentication_classes = [BasicAuthentication, ]
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly, ]
    filterset_fields = ['phone_number', 'theme__name']
