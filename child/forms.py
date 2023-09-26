from django import forms
from .models import  Guardian

class GuardianUploadForm(forms.ModelForm):
    class Meta:
        model=Guardian
        fields="__all__"