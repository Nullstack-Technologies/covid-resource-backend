
"""
    Utility functions for The laundry Boys Authentication
"""
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from laundry_boys_backend import settings


def random_number_with_n_digits(n):

    from random import randint

    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def generate_otp():
    """
        Generation of OTP easy with this function
    """

    return random_number_with_n_digits(settings.OTP_LENGTH_OF_OTP)


def get_user_from_email_url(url):

    elements = url.split(b'//')

    pk = urlsafe_base64_decode(force_bytes(elements[1]))

    return str(pk)


def import_old_users_from_text(data):

    from django.contrib.auth import get_user_model
    from authentication.models import Customer
    from rolepermissions.roles import assign_role

    import pyotp

    User = get_user_model()

    for _ in data.split('\n')[:-1]:
        if _:
            try:
                first_name = _.split('|')[0]
                mobile_number = _.split('|')[1]
                email = _.split('|')[2]
                user = User.objects.create_user(
                    username=mobile_number,
                    email=email,
                    first_name=first_name,
                    is_active=True
                )
                assign_role(user, 'customer')

                profile = Customer.objects.create(
                    user=user,
                    mobile_number=mobile_number,
                    base32_hash=pyotp.random_base32()
                )
            except:
                print(first_name, email, mobile_number)
