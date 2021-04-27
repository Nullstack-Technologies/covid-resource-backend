from django.db import models
from django_fsm import FSMField

from generic.models import AuditModel, LocationModel


class Requirement(AuditModel, LocationModel):
    """
        A Requirement Brought Forward by the people
    """

    class Meta:
        verbose_name = 'Requirement'
        verbose_name_plural = 'Requirements'

    STATES = ('New', 'Verified', 'Not Verified', 'In Progress', 'Completed', 'Cancelled')
    STATES = list(zip(STATES, STATES))

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=300)
    long_description = models.CharField(max_length=4096)
    status = FSMField(default=STATES[0], choices=STATES)
    deadline = models.DateTimeField(help_text='Time to Expire this requirement', null=True, blank=True)
    extra_information = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title
