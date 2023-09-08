from django.db import models

class Guardian(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    fingerprint_data = models.TextField(default=None, null=True, blank=True)
    fingerprint_details = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Child(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_full_name = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField()
    gender = models.CharField(max_length=10)
    guardian = models.OneToOneField(Guardian, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Child of {self.guardian})"
