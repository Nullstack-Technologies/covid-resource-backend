import django_filters
from django.db.models import Q
from django_filters import rest_framework as filters

from .models import Resource


class ResourceFilter(django_filters.FilterSet):

    search = filters.CharFilter(method='search_filter', label='Search By Title and Description')

    class Meta:
        model = Resource
        fields = (
            'city',
            'pin_code',
            'status',
            'search'
        )

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value)
            | Q(short_description__icontains=value)
            | Q(long_description__icontains=value)
        )

