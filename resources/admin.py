from django.contrib import admin

from .models import Resource

from generic.admin import AuditAdminMixin


@admin.register(Resource)
class ResourceAdmin(AuditAdminMixin):
    pass
