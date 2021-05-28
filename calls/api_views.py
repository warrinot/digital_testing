from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import filters
from calls.models import Call
from calls.serializers import CallSerializer
from calls.filters import CallFilter
from calls.paginations import CallPagination
from django_filters.rest_framework import DjangoFilterBackend


# Если нам требуется только чтение, наследуемся от viewsets.ReadOnlyModelViewSet
class CallApiViewSet(viewsets.ModelViewSet):
    """
    Api звонков
    """
    queryset = Call.objects.all()
    serializer_class = CallSerializer
    authentication_classes = [BasicAuthentication, ]
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly, ]
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    lookup_field = 'guid'
    filterset_class = CallFilter
    ordering_fields = ['id']
    pagination_class = CallPagination
