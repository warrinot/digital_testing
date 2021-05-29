from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework import permissions
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
    lookup_field = 'guid'
    authentication_classes = [BasicAuthentication, ]
    permission_classes = [permissions.IsAuthenticated, ]
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_class = CallFilter
    ordering_fields = ['id']
    pagination_class = CallPagination
