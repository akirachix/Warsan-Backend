from django.views.generic.edit import CreateView
from .models import Guardian, Child
from .forms import GuardianForm, ChildForm

class GuardianCreateView(CreateView):
    model = Guardian
    form_class = GuardianForm
    template_name = 'childguardianmanager/guardian_form.html'
    success_url = '/success/' 

class ChildCreateView(CreateView):
    model = Child
    form_class = ChildForm
    template_name = 'Child_Guadian.html'
    success_url = '/success/'
