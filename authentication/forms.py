from django import forms
from rolepermissions.roles import assign_role

from authentication.models import User


class UserCreationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'groups'
        )

