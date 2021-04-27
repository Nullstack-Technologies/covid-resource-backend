from django.views.generic import ListView, DetailView

from .models import Requirement
from .filters import RequirementFilter

from django_filters.views import FilterView


class RequirementListView(FilterView):
    """
        Requirement List Detail
    """
    queryset = Requirement.objects.all()
    filterset_class = RequirementFilter
    template_name = 'requirement/requirement_list.html'
    paginate_by = 10
    context_object_name = 'requirements'


class RequirementDetailView(DetailView):
    """
        Requirement Detail
    """
    queryset = Requirement.objects.all()
    template_name = 'requirement/requirement.html'
    context_object_name = 'requirement'
    slug_field = 'slug'
