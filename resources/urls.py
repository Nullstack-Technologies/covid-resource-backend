from django.urls import path

from .views import *

urlpatterns = [
    path('', ResourceListView.as_view(), name="resource_list"),
]
