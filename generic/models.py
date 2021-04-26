from django.db import models

from django.conf import settings
from imagekit.models import ProcessedImageField

from generic.validators import file_size_validator
from generic.managers import StateModelInactiveManager, StateModelActiveManager


class BaseModel(models.Model):
    """
        Base model for
        all the models.

        Some Operations that apply to all the tables
        may be placed over here.

        does nothing but let's all the other models
        extend it.
    """

    objects = models.Manager()

    class Meta:
        abstract = True

    @property
    def _pk(self):
        return f"⚙️ (Edit)"

    @property
    def _view(self):
        return f"👁️ (View)"


class AuditWithoutHistory(BaseModel):
    """
        Audit Model for the whole project.

        This has the audit fields.
        viz(Namely): created_at, updated_at,
        created_by, updated_by.

        Will be extended by models needing to audit there
        status of saves and updates
    """

    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='+',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='+',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )


class AuditModel(AuditWithoutHistory):
    """
        Add history to fields that need it
    """
    class Meta:
        abstract = True

    # history = HistoricalRecords(inherit=True)


class StateModel(BaseModel):
    """
        This models stores the state of a model.

        There are basically two states of every model
        1.) Active
        2.) Inactive

        A model entry can never be Deleted.
        It should always be deactivated
    """

    class Meta:
        abstract = True

    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'

    STATES = (
        (ACTIVE, ACTIVE),
        (INACTIVE, INACTIVE)
    )

    objects = models.Manager()  # Default Manager
    active = StateModelActiveManager()
    inactive = StateModelInactiveManager()

    status = models.CharField(max_length=8, choices=STATES, default=ACTIVE)

    def is_active(self):
        if self.status == self.ACTIVE:
            return True
        return False
    is_active.boolean = True

    def activate(self):
        self.status = self.ACTIVE

    def deactivate(self):
        self.status = self.INACTIVE


class SEOModel(BaseModel):

    class Meta:
        abstract = True

    seo_title = models.CharField(max_length=255, null=True, blank=True)
    seo_description = models.CharField(max_length=500, null=True, blank=True)
    seo_keywords = models.CharField(max_length=500, null=True, blank=True)
    seo_url = models.URLField(null=True, blank=True)
    seo_image = ProcessedImageField(
        upload_to="nullstack_technologies/images/%Y/%m/%d",
        format='JPEG',
        options={'quality': 60},
        validators=[
            file_size_validator
        ],
        null=True,
        blank=True
    )


# class City(AbstractCity):
#     pass

#
# class Region(AbstractRegion):
#     pass
#
#
# class Country(AbstractCountry):
#     pass


class LocationModel(BaseModel):
    """
        This is an abstract model to store
        the location of an entity, requirement, etc
    """

    class Meta:
        abstract = True

    city = models.ForeignKey('cities_light.SubRegion', on_delete=models.SET_NULL, null=True, related_name='+')
    address = models.CharField(max_length=300, null=True,)
    pin_code = models.CharField(max_length=10,)
