from django.shortcuts import render

# Create your views here
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class HealthworkerLoginView(LoginView):
    template_name = 'healthworker_login.html'  
    success_url = reverse_lazy('retrieve_guardian')  
