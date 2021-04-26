from django.contrib import admin

from generic.admin import StateAdminMixin, AuditAdminMixin
from .models import Entity


@admin.register(Entity)
class EntityAdmin(AuditAdminMixin, StateAdminMixin):
    autocomplete_fields = ['city']
    raw_id_fields = ['user']

