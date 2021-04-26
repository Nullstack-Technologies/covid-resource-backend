from django.contrib import admin

from generic.admin import AuditAdminMixin
from .forms import RequirementForm
from .models import Requirement


@admin.register(Requirement)
class RequirementAdmin(AuditAdminMixin):
    form = RequirementForm
