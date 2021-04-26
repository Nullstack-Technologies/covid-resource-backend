from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from rest_framework.authtoken.models import Token


# @receiver(post_save, sender=Token)
# def token_addition_signal(sender, **kwargs):
#     print('I was called')
#     print(sender, kwargs)

# @receiver(reset_password_token_created)
# def password_reset_token_created(sender, reset_password_token, *args, **kwargs):
#     """
#     Handles password reset tokens
#     When a token is created, an e-mail needs to be sent to the user
#     :param sender:
#     :param reset_password_token:
#     :param args:
#     :param kwargs:
#     :return:
#     """
#     # send an e-mail to the user
#     context = {
#         'current_user': reset_password_token.user,
#         'username': reset_password_token.user.username,
#         'email': reset_password_token.user.email,
#         'reset_password_url': "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
#     }
#
#     print(context)
