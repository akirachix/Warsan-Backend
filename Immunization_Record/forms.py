# views.py

# immunization_records/forms.py

from django import forms
from .models import ImmunizationRecord

class ImmunizationRecordForm(forms.ModelForm):
    class Meta:
        model = ImmunizationRecord
        fields = "__all__"
