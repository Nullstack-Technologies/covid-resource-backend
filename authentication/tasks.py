from django.utils import timezone

from authentication.utils import generate_otp
from communication.utils import fire_sms
from laundry_boys_backend import settings


# @task(name="generate_otp_for_verification")
def generate_otp_for_verification(user_pk):
    """
        Send Verification SMS to User
    """
    from authentication.models import Customer

    otp = generate_otp()
    user = Customer.objects.get(pk=user_pk)
    message = settings.OTP_TEXT_FOR_SENDING % str(otp)

    # do updating stuff regarding OTP
    user.otp_send_date_time = timezone.now()
    user.otp = otp
    user.no_of_otps_send += 1
    user.no_of_otp_validation_requests = 0
    user.save()

    print(message, user)
    fire_sms(phone_number=user.mobile_number, message=message)


# @task(name="accept_otp")
def accept_otp(profile_pk):
    """
        Task to accept Profile
        OTP Verification Request
    """
    from authentication.models import Customer

    profile = Customer.objects.get(pk=profile_pk)
    profile.is_mobile_verified = True
    profile.full_clean()
    profile.save(force_update=True)


# @task(name='logout_user_from_everywhere')
def logout_user_from_everywhere(user_pk):
    """
        Task to logout a user from all the instances
        he/she is logged in with
    """
    from authentication.models import User
    from rest_framework.authtoken.models import Token

    user = User.objects.get(pk=user_pk)

    # remove auth token if exists
    token = Token.objects.filter(user=user)
    if token:
        token = token[0]
        token.delete()

