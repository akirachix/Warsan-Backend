from django import forms
from .models import Guardian, Child

class GuardianForm(forms.ModelForm):
    class Meta:
        model = Guardian
        fields = ['first_name', 'last_name', 'phone_number', 'location', 'fingerprint_data', 'fingerprint_details']
        widgets = {
            'fingerprint_data': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['first_name', 'last_name', 'father_full_name', 'date_of_birth', 'gender', 'guardian']

    def __init__(self, *args, **kwargs):
        super(ChildForm, self).__init__(*args, **kwargs)
        self.fields['guardian'].widget = forms.Select(attrs={'class': 'form-control'})
