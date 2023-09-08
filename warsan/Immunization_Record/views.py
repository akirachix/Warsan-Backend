from django.shortcuts import render
from .forms import ImmunizationUploadForm
from .models import Immunization_Record
 
def immunization_upload_form(request):
    if request.method =='POST':
        form=Immunization_Record(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ImmunizationUploadForm()
    return render(request,"immunization/immunization_upload.html",{"form":form})

def immunization_list(request):
    immunization=Immunization_Record.objects.all()
    return render(request,"immunization/immunization_list.html",{"immunization":immunization})
