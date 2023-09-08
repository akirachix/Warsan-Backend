

from django.db import models

class Vaccine(models.Model):

    name=models.CharField(max_length=32)
    target_disease = models.TextField()
    minimum_age = models.IntegerField()
    maximum_age =models.IntegerField()
    recommended_dose = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):          
        return self.name



