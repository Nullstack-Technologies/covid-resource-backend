from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext, gettext_lazy as _

from rolepermissions.roles import assign_role

from allauth.account.forms import (
    LoginForm as AALoginForm,
    SignupForm as AASignupForm
)

from captcha.fields import ReCaptchaField

from authentication.validators import phone_number_validator
from entity.models import Entity

User = get_user_model()


class LoginForm(AALoginForm):
    pass
    # captcha = ReCaptchaField()

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         print(visible.name)


class SignupForm(AASignupForm):
    entity_type = forms.ChoiceField(choices=Entity.ENTITY_TYPES)
    name = forms.CharField(max_length=100)
    mobile_number = forms.CharField(max_length=13, validators=[
        phone_number_validator
    ])

    field_order = ['name', 'email', 'username', 'entity_type', 'mobile_number',  'password', 'confirm_password']

    def clean_mobile_number(self):
        value = self.cleaned_data["mobile_number"]
        if Entity.active.filter(mobile_number=value):
            raise forms.ValidationError(
                _('Mobile Number Already Exists!')
            )
        return value

    def save(self, request):
        user = super().save(request)
        entity = Entity.objects.create(
            user=user,
            mobile_number=self.cleaned_data.pop('mobile_number'),
            name=self.cleaned_data.pop('name'),
            entity_type=self.cleaned_data.pop('entity_type'),
        )
        assign_role(user, 'entity')
        print(user, entity)
        return user
