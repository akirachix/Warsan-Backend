from django.contrib.auth.models import AbstractUser, Permission,Group
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from location.models import Location
from django.core.mail import send_mail


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')
    is_NGO = models.BooleanField(default=True)
    def __str__(self):
        return self.first_name
    
class Healthworker(AbstractUser):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    hospital = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='healthworkers')
    user_permissions = models.ManyToManyField(Permission, related_name='healthworkers')
    is_healthworker = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True) 

 
    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def send_verification_email(self):
        verification_link = reverse('verify_email', kwargs={'token': str(self.verification_token)})
        subject = 'Verify your email'
        message = f'Please click the link to verify your email: {verification_link}'
        send_mail(subject, message, 'noreply@warsan.xyz', [self.email])  
        



