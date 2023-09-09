from django.db import models




class Guardian(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    # fingerprint_data = models.TextField(default=None, null=True, blank=True)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def register_child(self, first_name, last_name, date_of_birth, gender):
        
        child = Child.objects.create(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender,
            guardian=self,
        )
        return child

    def get_children(self):
        
        return Child.objects.filter(guardian=self)

class Child(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateTimeField()
    gender = models.CharField(max_length=10)
    guardian = models.ForeignKey(Guardian, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Child of {self.guardian})"
