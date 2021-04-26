from django.db.models import Q
from django_filters import rest_framework as filters

from authentication.models import Customer


class CustomerFilter(filters.FilterSet):

    search = filters.CharFilter(method='search_keyword')

    class Meta:
        model = Customer
        fields = ['search']

    # noinspection PyMethodMayBeStatic
    def search_keyword(self, queryset, name, value):
        if name == 'search' and value:
            return queryset.filter(
                Q(mobile_number__icontains=value) |
                Q(user__first_name__icontains=value)|
                Q(user__email__icontains=value)
            )
        return queryset
