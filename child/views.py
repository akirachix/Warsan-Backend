from django.shortcuts import redirect, render
from .forms import GuardianRegistrationForm, ChildRegistrationForm
from .models import Guardian,Child
from django.urls import reverse
from django.http import HttpResponseRedirect
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
        print("Form errors:", form.errors)  # Debug: Print form errors
        if form.is_valid():
            print("Form is valid")  # Debug: Confirm form is valid
            guardian = form.save(commit=False)
            # Get the selected region from the form
            region = form.cleaned_data.get('location')
            print("Selected region:", region)  # Debug: Print selected region
            if region:
                # Get or create the Location instance based on the selected region
                location, _ = Location.objects.get_or_create(region=region)
                print("Location instance:", location)  # Debug: Print location instance
                if isinstance(location, Location):
                    guardian.location = location  # Assign the Location instance to the guardian
                else:
                    # Handle the case where location is not an instance of Location
                    raise ValueError("Invalid location instance")
            # Save the guardian
            guardian.save()
            # Print the saved guardian's ID for debugging
            print("Saved guardian ID:", guardian.id)
            # Redirect to the guardian details page
            return redirect('guardian_details', guardian_id=guardian.id)
    else:
        form = GuardianRegistrationForm()
    # Pass the regions for the dropdown in the form
    regions = Location.REGIONS_CHOICES
    print("Regions:", regions)  # Debug: Print regions
    return render(request, 'guardian/register_guardian.html', {'form': form, 'regions': regions})

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
            return redirect('child_registration_success')
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






