from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    groups = models.ManyToManyField(Group, related_name='custom_users')  # Groups associated with CustomUser
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')
    is_NGO = models.BooleanField(default=True)  # Add is_NGO attribute

class Healthworker(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = PhoneNumberField(unique=True, region='IR')
    location = models.CharField(max_length=100)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    groups = models.ManyToManyField(Group, related_name='healthworkers')  # Groups associated with Healthworker
    user_permissions = models.ManyToManyField(Permission, related_name='healthworkers')
    is_healthworker = models.BooleanField(default=True)  # Add is_healthworker attribute