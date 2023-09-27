from django import forms
from .models import  Guardian,Child
from location.models import Location

# class GuardianUploadForm(forms.ModelForm):
#     class Meta:
#         model=Guardian
#         fields="__all__"



class GuardianRegistrationForm(forms.ModelForm):
    class Meta:
        model = Guardian
        fields = ['first_name', 'last_name', 'location', 'phone_number', 'status']

class ChildRegistrationForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender']       