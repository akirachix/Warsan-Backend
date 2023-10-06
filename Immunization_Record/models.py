from django.db import models
from vaccine.models import Vaccine
from child.models import Child

from child.models import Guardian

class Immunization_Record(models.Model):
    child = models.OneToOneField(Child, on_delete=models.CASCADE, null=True)
    vaccine = models.ManyToManyField(Vaccine)
    guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE, null=True)
    date_of_administration = models.DateField(null=True, blank=True ,auto_now_add=True)
    next_date_of_administration = models.DateField()  
    status = models.CharField(max_length=20, choices=[('Taken', 'Taken'), ('Missed', 'Missed')], default='Not administered')

    def __str__(self):
      vaccine_choices = ", ".join([vaccine.vaccine_choice for vaccine in self.vaccine.all()])
      return f'Immunization Record - {self.child.first_name} {self.child.last_name} - Vaccines: {vaccine_choices}'
