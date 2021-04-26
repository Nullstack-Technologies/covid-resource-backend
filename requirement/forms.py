from ckeditor.widgets import CKEditorWidget
from django import forms

from .models import Requirement


class RequirementForm(forms.ModelForm):
    long_description = forms.CharField(widget=CKEditorWidget())
    short_description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Requirement
        fields = '__all__'
