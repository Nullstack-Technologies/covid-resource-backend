"""
    Regular Expressions tested to work as validators for some forms
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

phone_number_validator_regex = r'^\+?1?\d{9,15}$'

indian_phone_number_validator_regex = r'^\+91[0-9]{10,11}$'

# validate a year input
year_validator_regex = number_validator_regex % (4, 4)
