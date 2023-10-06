from django.shortcuts import redirect, render, get_object_or_404

from child.models import Child
from .models import Immunization_Record
from .forms import ImmunizationUploadForm

def view_immunization_record(request, record_id):

    
    immunization_record = get_object_or_404(Immunization_Record, id=record_id)

    vaccine = immunization_record.vaccine.all()
    print("Associated Vaccines:", [vaccine.vaccine_choice for vaccine in vaccine])  # Print associated vaccines

    
    return render(request, 'immunization_record_detail.html', {'immunization_record': immunization_record,'vaccine':vaccine})





def update_immunization_record(request, record_id):
    immunization_record = get_object_or_404(Immunization_Record, id=record_id)

    if request.method == 'POST':
        form = ImmunizationUploadForm(request.POST, instance=immunization_record)
        if form.is_valid():
            # Save the form with the changes to the database
            form.save()  # Add this line to save the changes

            return redirect('view_immunization_record', record_id=record_id)
    else:
        form = ImmunizationUploadForm(instance=immunization_record)

    return render(request, 'update_immunization_record.html', {'form': form, 'immunization_record': immunization_record})


def upload_immunization(request, child_id):
    child = Child.objects.get(id=child_id)

    if request.method == 'POST':
        form = ImmunizationUploadForm(request.POST)
        if form.is_valid():
            immunization_record = form.save(commit=False)

            # Associate the child and guardian with the immunization record
            immunization_record.child = child
            immunization_record.guardian = child.guardian

            # Save the immunization record to get an ID
            immunization_record.save()

            # Get the selected vaccines from the form
            selected_vaccines = form.cleaned_data.get('vaccine')

            # Clear any existing associations and set the selected vaccines
            immunization_record.vaccine.clear()
            immunization_record.vaccine.set(selected_vaccines)

            return redirect('guardian_detail', guardian_id=child.guardian.id)
    else:
        form = ImmunizationUploadForm()

    return render(request, 'create_immunization_record.html', {'form': form, 'child': child})
