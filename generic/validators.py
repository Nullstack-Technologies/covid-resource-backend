import re
from datetime import datetime

from django.conf import settings
from django.core.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _
# from rest_framework.exceptions import ValidationError


__author__ = 'Nauman Arif'


# validate file size
from generic.regular_expressions import phone_number_validator_regex


def file_size_validator(_file):
    try:
        if _file:
            if _file.size > settings.MAX_UPLOAD_SIZE:
                raise ValidationError(
                    {
                        'file': _('File Size Exceeds the limit (Max Allowed size- 2.5 MB)')
                    }
                )
    except:
        pass


# datetime validator
def date_format_validator(date):
    try:
        datetime.strptime(str(date), '%Y-%m-%d')
    except ValidationError:
        raise ValidationError(_('The date format supplied is wrong. It Should be YYYY-MM-DD'))


def validate_file_extension(value, file_extensions):
    """
        Validate file extensions manually.
    """
    import os
    ext = os.path.splitext(value.name)[1][1:]
    if not ext.lower() in file_extensions:
        raise ValidationError({
         'file':  _('Unsupported file extension. Allowed: %s') % str(file_extensions)
        })


# phone number validator
def phone_number_validator(number):
    if not re.match(phone_number_validator_regex, number):
        raise ValidationError(_("Provide a correct Phone number format"))
