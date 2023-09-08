from django import forms
from .models import Immunization_Record

class ImmunizationUploadForm(forms.ModelForm):
    class Meta:
        model=Immunization_Record
        fields="__all__"