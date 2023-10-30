from django.db import models

class Vaccine(models.Model):
    VACCINE_CHOICES = [
        ('BCG', 'BCG - Tuberculosis'),
        ('HepB', 'Hepatitis B'),
        ('DTP', 'DTP - Diphtheria, Tetanus, Pertussis'),
        ('IPV', 'IPV  - Polio'),
        ('HiB', 'HiB - Haemophilus influenzae type b'),
        ('PCV13', 'PCV13- Pneumococcal disease'),
        ('RV', 'RV - Rotavirus'),
        ('MMR', 'MMR- Measles, Mumps, Rubella'),
        ('Varicella', 'Varicella - Chickenpox'),
        ('HepA', 'Hepatitis A'),
        ('MenACWY', 'MenACWY- Meningococcal disease'),
        ('DTaP-IPV-HiB-HepB', 'DTaP-IPV-HiB-HepB - Diphtheria, Tetanus, Pertussis, Polio, Haemophilus influenzae type b, Hepatitis B'),
        ('Influenza', 'Influenza (Seasonal)'),
    ]

    vaccine_choice = models.CharField(max_length=32, choices=VACCINE_CHOICES, unique=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_vaccine_choice_display()
