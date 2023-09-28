from django.db import models

class Vaccine(models.Model):
    VACCINE_CHOICES = [
        ('BCG', 'BCG - Tuberculosis - Recommended Age: Birth'),
        ('HepB', 'Hepatitis B - Hepatitis B - Recommended Age: Birth, 1-2 months, 6-18 months'),
        ('DTP', 'DTP - Diphtheria, Tetanus, Pertussis - Recommended Age: 2 months, 4 months, 6 months, 15-18 months'),
        ('IPV', 'IPV  - Polio - Recommended Age: 2 months, 4 months, 6-18 months'),
        ('HiB', 'HiB - Haemophilus influenzae type b - Recommended Age: 2 months, 4 months, 6 months, 12-15 months'),
        ('PCV13', 'PCV13- Pneumococcal disease - Recommended Age: 2 months, 4 months, 6 months, 12-15 months'),
        ('RV', 'RV - Rotavirus - Recommended Age: 2 months, 4 months'),
        ('MMR', 'MMR- Measles, Mumps, Rubella - Recommended Age: 12-15 months'),
        ('Varicella', 'Varicella - Chickenpox - Recommended Age: 12-15 months'),
        ('HepA', 'Hepatitis A - Hepatitis A - Recommended Age: 12-18 months'),
        ('MenACWY', 'MenACWY- Meningococcal disease - Recommended Age: 12-15 months'),
        ('DTaP-IPV-HiB-HepB', 'DTaP-IPV-HiB-HepB - Diphtheria, Tetanus, Pertussis, Polio, Haemophilus influenzae type b, Hepatitis B - Recommended Age: 2 months, 4 months, 6 months'),
        ('Influenza', 'Influenza - Influenza (Seasonal) - Recommended Age: Annually from 6 months onwards'),
    ]

    vaccine_choice = models.CharField(max_length=32, choices=VACCINE_CHOICES, unique=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_vaccine_choice_display()

    def get_recommended_age(self):
        age_map = {
            'BCG': 'Birth',
            'HepB': 'Birth, 1-2 months, 6-18 months',
            'DTP': '2 months, 4 months, 6 months, 15-18 months',
            'IPV': '2 months, 4 months, 6-18 months',
            'HiB': '2 months, 4 months, 6 months, 12-15 months',
            'PCV13': '2 months, 4 months, 6 months, 12-15 months',
            'RV': '2 months, 4 months',
            'MMR': '12-15 months',
            'Varicella': '12-15 months',
            'HepA': '12-18 months',
            'MenACWY': '12-15 months',
            'DTaP-IPV-HiB-HepB': '2 months, 4 months, 6 months',
            'Influenza': 'Annually from 6 months onwards',
        }

        recommended_age = age_map.get(self.vaccine_choice)
        if recommended_age is None:
            recommended_age = 'N/A'  

        return recommended_age