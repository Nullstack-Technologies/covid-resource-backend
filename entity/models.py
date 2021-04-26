from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from imagekit.models import ProcessedImageField

from generic.models import LocationModel, AuditModel, StateModel
from generic.validators import phone_number_validator, file_size_validator

User = get_user_model()


class Entity(LocationModel, AuditModel, StateModel):
    """
        This model is used for
        profile model for an Entity.

        Used for mainly customers registered
        in the TheLaundryBoys
    """

    class Meta:
        verbose_name = _('Organization or Individual')
        verbose_name_plural = _('Organizations or Individuals')

    INDIVIDUAL = 0
    ORGANIZATION = 1

    ENTITY_TYPES = (
        (INDIVIDUAL, 'Individual',),
        (ORGANIZATION, 'Organization')
    )

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name='+')
    name = models.CharField(max_length=200, unique=True)
    id_proof = models.FileField(
        upload_to='khidmat/organization/proof/%Y/%m/%d',
        validators=[
            file_size_validator
        ],
        null=True,
        blank=True
    )
    logo = ProcessedImageField(
        upload_to="khidmat/organization/logos/%Y/%m/%d",
        format='JPEG',
        options={'quality': 60},
        validators=[
            file_size_validator
        ],
        null=True,
        blank=True
    )
    mobile_number = models.CharField(
        _("Mobile Number"),
        validators=[phone_number_validator],
        max_length=13,
        unique=True
    )
    alternative_mobile_number = models.CharField(
        _("Alternative Mobile Number"),
        validators=[phone_number_validator],
        max_length=13,
        unique=True,
        null=True,
        blank=True
    )
    entity_type = models.PositiveSmallIntegerField(choices=ENTITY_TYPES, default=INDIVIDUAL)

    def __str__(self):
        return f"{self.name} | {self.entity_type}"
