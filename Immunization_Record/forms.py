# views.py

# immunization_records/forms.py

# forms.py
from django import forms
from .models import Immunization_Record



class ImmunizationUploadForm(forms.ModelForm):
    class Meta:
        model = Immunization_Record
        fields = ['vaccine', 'date_of_administration', 'next_date_of_administration', 'status']
        exclude = ['date_of_administration']
        widgets = {
            'vaccine': forms.CheckboxSelectMultiple(),
        }

    # def save(self, commit=True):
    #     # Save the immunization record without committing to the database
    #     immunization_record = super().save(commit=False)

    #     if commit:
    #         immunization_record.save()

    #     # Update the many-to-many relationship for vaccines
    #     immunization_record.vaccine.set(self.cleaned_data['vaccine'])

    #     return immunization_record
