from django.urls import path

from .views import *

urlpatterns = [
    path('', RequirementListView.as_view(), name="requirement_list"),
]
