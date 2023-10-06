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
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'guardian']
        

    def __init__(self, *args, **kwargs):
        guardian_id = kwargs.pop('guardian_id', None)
        super().__init__(*args, **kwargs)
        if guardian_id:
            self.fields['guardian'].initial = guardian_id