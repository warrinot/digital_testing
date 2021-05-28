from django_filters import rest_framework as filters
from calls.models import Call


class CallFilter(filters.FilterSet):
    min_timestamp_started = filters.DateTimeFilter(
        field_name='timestamp_started',
        lookup_expr='gte'
    )
    max_timestamp_started = filters.DateTimeFilter(
        field_name='timestamp_started',
        lookup_expr='lte'
    )

    class Meta:
        model = Call
        fields = ['min_timestamp_started',
                  'max_timestamp_started',
                  'phone_number',
                  'is_finished',
                  'theme__name',
                  ]
