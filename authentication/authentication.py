from django.contrib.auth.models import User

from authentication.models import Customer


class EmailAuthBackend(object):
    """ Authenticate using an email address """

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class MobileAuthBackend(object):
    """ Authenticate using mobile number"""

    def authenticate(self, request, username=None, password=None):
        try:
            user = Customer.objects.get(mobile_number=username).user
            if user.check_password(password):
                return user
            return None
        except Customer.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None