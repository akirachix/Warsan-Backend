# views.py

# immunization_records/forms.py

from django import forms
from .models import Immunization_Record

class ImmunizationRecordUpdateForm(forms.ModelForm):
    class Meta:
        model = Immunization_Record
        fields = ['vaccine', 'next_date_of_administration']
        widgets = {
            'vaccine': forms.SelectMultiple(attrs={'size': 5}),  # Adjust the 'size' attribute as needed
        }