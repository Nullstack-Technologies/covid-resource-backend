from django.contrib import admin, messages
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from generic.models import StateModel


class AuditAdminMixin(admin.ModelAdmin):
    """
        Audit admin mixin adds the default
        admin fields that are present in
        django
    """

    readonly_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']

    def save_model(self, request, obj, form, change):
        # Overriding the save model to
        # save details not shown in the form
        if not obj.created_by:
            # if the original creator is not present update him
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


class StateAdminMixin(admin.ModelAdmin):
    """
        State mixin for admin panels.
        Will add state changing filters and
        actions to the admin panel
    """

    actions = ['activate', 'deactivate']

    def is_active(self, obj):
        if obj.status == StateModel.ACTIVE:
            return True
        return False
    is_active.boolean = True

    def activate(self, request, queryset):
        """
            Activate a given set of models
        """

        if not queryset.filter(status=StateModel.ACTIVE):
            queryset.update(status=StateModel.ACTIVE)
            self.message_user(
                request,
                format_html(_('Activated %s Entries(s)'
                              % str(queryset.count()))),
                extra_tags='safe',
                level=messages.SUCCESS
            )
        else:
            self.message_user(
                request,
                format_html(_('Some Entries are already activated!')),
                extra_tags='safe',
                level=messages.ERROR
            )
    activate.short_description = 'Activate selected entries'

    def deactivate(self, request, queryset):
        """
            Deactivate given set of models
        """

        if not queryset.filter(status=StateModel.INACTIVE):
            queryset.update(status=StateModel.INACTIVE)
            self.message_user(
                request,
                format_html(_('De-Activated %s Entries(s)'
                              % str(queryset.count()))),
                extra_tags='safe',
                level=messages.SUCCESS
            )
        else:
            self.message_user(
                request,
                format_html(_('Some Entries are already deactivated!')),
                extra_tags='safe',
                level=messages.ERROR
            )

    deactivate.short_description = 'DE-Activate selected entries'
