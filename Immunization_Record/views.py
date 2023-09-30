from django.shortcuts import redirect, render, get_object_or_404
from .models import Immunization_Record
from .forms import ImmunizationRecordUpdateForm

def view_immunization_record(request, record_id):

    
    immunization_record = get_object_or_404(Immunization_Record, id=record_id)
    
    
    return render(request, 'immunization_record_detail.html', {'immunization_record': immunization_record})

def update_immunization_record(request, record_id):
    immunization_record = get_object_or_404(Immunization_Record, id=record_id)

    if request.method == 'POST':
        form = ImmunizationRecordUpdateForm(request.POST, instance=immunization_record)
        if form.is_valid():
            form.save()
            return redirect('view_immunization_record', record_id=record_id)
    else:
        form = ImmunizationRecordUpdateForm(instance=immunization_record)

    return render(request, 'update_immunization_record.html', {'form': form, 'immunization_record': immunization_record})