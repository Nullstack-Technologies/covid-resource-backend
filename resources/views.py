from django.views.generic import DetailView

from .models import Resource
from .filters import ResourceFilter

from django_filters.views import FilterView


class ResourceListView(FilterView):
    """
        Resource List Detail
    """
    queryset = Resource.objects.all()
    filterset_class = ResourceFilter
    template_name = 'resources/resource_list.html'
    paginate_by = 10
    context_object_name = 'resources'


class ResourceDetailView(DetailView):
    """
        Resource Detail
    """
    queryset = Resource.objects.all()
    template_name = 'resources/resource.html'
    context_object_name = 'resource'
    slug_field = 'slug'
