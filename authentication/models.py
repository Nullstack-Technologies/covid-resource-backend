from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch import receiver


class User(AbstractUser):
    """
        Override the User Model
    """
    pass


@receiver(pre_save, sender=User)
def update_username_from_email(sender, instance, **kwargs):
    user_email = instance.email
    username = user_email
    instance.username = username
