from django.shortcuts import redirect, render, get_object_or_404

from child.models import Child
from .models import Immunization_Record
from .forms import ImmunizationUploadForm

def view_immunization_record(request, record_id):

    
    immunization_record = get_object_or_404(Immunization_Record, id=record_id)

    vaccine = immunization_record.vaccine.all()
    print("Associated Vaccines:", [vaccine.vaccine_choice for vaccine in vaccine]) 

    
    return render(request, 'immunization_record_detail.html', {'immunization_record': immunization_record,'vaccine':vaccine})




# views.py


def update_immunization_record(request, record_id):
    immunization_record = get_object_or_404(Immunization_Record, id=record_id)

    if request.method == 'POST':
        form = ImmunizationUploadForm(request.POST, instance=immunization_record)
        if form.is_valid():
            updated_record = form.save()

            # Redirect to the immunization record view with the updated record
            return redirect('view_immunization_record', record_id=updated_record.id)
    else:
        # Populate the form with the existing data
        form = ImmunizationUploadForm(instance=immunization_record)

    return render(request, 'update_immunization_record.html', {'form': form, 'immunization_record': immunization_record})

def upload_immunization(request, child_id):
    child = Child.objects.get(id=child_id)

    if request.method == 'POST':
        form = ImmunizationUploadForm(request.POST)
        if form.is_valid():
            immunization_record = form.save(commit=False)

            immunization_record.child = child
            immunization_record.guardian = child.guardian

            immunization_record.save()

            selected_vaccines = form.cleaned_data.get('vaccine')

            immunization_record.vaccine.clear()
            immunization_record.vaccine.set(selected_vaccines)

            return redirect('guardian_detail', guardian_id=child.guardian.id)
    else:
        form = ImmunizationUploadForm()

    return render(request, 'create_immunization_record.html', {'form': form, 'child': child})
