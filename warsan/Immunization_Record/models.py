from django.db import models

class Immunization_Record(models.Model): 
    date_of_administaration=models.DateTimeField()
    next_date_of_administration= models.DateTimeField()
   