from django.shortcuts import redirect, render
from .forms import GuardianUploadForm
from .models import Guardian
 
def guardian_upload_form(request):
    if request.method =='POST':
        form=GuardianUploadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=GuardianUploadForm()
    return render(request,"guardian/guardian_upload.html",{"form":form})



