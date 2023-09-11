from django.db import models
from django.contrib.auth.models import User



class Registrations(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    date_created = models.DateField(auto_now_add=True)  
    date_updated = models.DateField(auto_now=True)
    

