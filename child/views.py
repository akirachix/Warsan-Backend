from django.shortcuts import redirect, render
from .forms import GuardianRegistrationForm, ChildRegistrationForm
from .models import Guardian
from location.models import Location

# def retrieve_guardian(request):
#     if request.method == 'POST':
#         phone_number = request.POST.get('phone_number')
#         try:
#             guardian = Guardian.objects.get(phone_number=phone_number)
#             return render(request, 'guardian_details.html', {'guardian': guardian})
#         except Guardian.DoesNotExist:
#             return render(request, 'guardian_not_found.html')
#     return render(request, 'guardian/retrieve_guardian.html')
def retrieve_guardian(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        try:
            guardian = Guardian.objects.get(phone_number=phone_number)
            return redirect('guardian_detail', guardian_id=guardian.id)
        except Guardian.DoesNotExist:
            # Guardian not found, redirect to the guardian registration form
            return redirect('register_guardian')  # Replace 'register_guardian' with your URL name for the registration form
    return render(request, 'guardian/retrieve_guardian.html')
def guardian_detail(request, guardian_id):
    guardian = Guardian.objects.get(pk=guardian_id)
    children = guardian.child_set.all()
    # Calculate child ages and add them to the children queryset
    children_with_age = []
    for child in children:
        child_age = child.calculate_age()
        children_with_age.append({'child': child, 'age': child_age})
    context = {
        'guardian': guardian,
        'children_with_age': children_with_age,
    }
    return render(request, 'guardian/guardian_detail.html', context)

def register_guardian(request):
    if request.method == 'POST':
        form = GuardianRegistrationForm(request.POST)
        if form.is_valid():
            guardian = form.save(commit=False)
            # Save the guardian
            guardian.save()
            # Redirect to the guardian details page
            return redirect('guardian_detail', guardian_id=guardian.id)  # Redirect to the guardian details page
    else:
        form = GuardianRegistrationForm()
    
    return render(request, 'guardian/register_guardian.html', {'form': form})
def register_child(request):
    if request.method == 'POST':
        form = ChildRegistrationForm(request.POST)
        if form.is_valid():
            child = form.save(commit=False)
            # Get or create the Location instance based on the selected region
            region = form.cleaned_data.get('location')
            if region:
                location, _ = Location.objects.get_or_create(region=region)
                child.location = location  # Assign the Location instance to the child
            # Save the child
            child.save()
            # Redirect to a success page or wherever needed
            return redirect('immunization_record_view', child_id=child.id)
    else:
        form = ChildRegistrationForm()
    # Pass the regions for the dropdown in the form
    regions = Location.REGIONS_CHOICES
    return render(request, 'guardian/register_child.html', {'form': form, 'regions': regions})
# def guardian_upload_form(request):
#     if request.method =='POST':
#         form=GuardianUploadForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form=GuardianUploadForm()
#     return render(request,"guardian/guardian_upload.html",{"form":form})