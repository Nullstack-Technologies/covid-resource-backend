from django.db import models


class StateModelActiveManager(models.Manager):
    """
        Custom Manager for Active Entries
    """

    def get_queryset(self):
        from .models import StateModel
        return super().get_queryset().filter(status=StateModel.ACTIVE)


class StateModelInactiveManager(models.Manager):
    """
        Custom Manager for Active Entries
    """

    def get_queryset(self):
        from .models import StateModel
        return super().get_queryset().filter(status=StateModel.INACTIVE)
