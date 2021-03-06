from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('requirements/', include('requirement.urls'), name="requirements"),
    path('resources/', include('resources.urls'), name="resource"),
    path('', TemplateView.as_view(template_name="pages/home.html"), name="home"),
]
