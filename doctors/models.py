from django.db import models

from generic.models import AuditModel, LocationModel

from django_fsm import FSMField


# class Doctor(AuditModel, LocationModel):
#     """
#         A Doctor is an entity
#         that provides consultation
#     """