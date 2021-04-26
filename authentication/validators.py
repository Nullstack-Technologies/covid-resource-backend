import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


"""
    Validators to be used
    in The Laundry boys
"""

_AUTHOR_ = 'Nauman Arif'

# matches a generic name without unicode characters passed
generic_name_regular_expression = r"^[a-zA-Z, .'-]+$"

# validates a sequence of number taking two inputs
# i.e (lower count of digits, upper count of digits)
# used as ex- number_validator_regex %(1,2) matches
# minimum 1 digit and maximum 2 digits
number_validator_regex = r'^[0-9]{%s,%s}$'


# validates a given phone number (International + Country)
phone_number_validator_regex = r'^(\+\d{1,3})?\s?\d{8,13}'


# validator for name validation
# in this project
def name_validator(value):
    if not re.match(generic_name_regular_expression, value):
        raise ValidationError(_("Name entered is of incorrect format"))


# phone number validator
def phone_number_validator(number):
    if not re.match(phone_number_validator_regex, number):
        raise ValidationError(_("Provide a correct Phone number format"))

