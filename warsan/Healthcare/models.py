from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class HealthWorker(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField(unique=True, region='IR')  
    hospital = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'

