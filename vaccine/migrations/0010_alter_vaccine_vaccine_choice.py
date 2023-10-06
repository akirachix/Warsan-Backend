# Generated by Django 3.2.6 on 2023-10-03 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0009_alter_vaccine_vaccine_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccine',
            name='vaccine_choice',
            field=models.CharField(choices=[('BCG', '  Recommended Age: Birth'), ('HepB', ' Recommended Age: Birth, 1-2 months, 6-18 months'), ('DTP', ' Recommended Age: 2 months, 4 months, 6 months, 15-18 months'), ('IPV', ' Recommended Age: 2 months, 4 months, 6-18 months'), ('HiB', ' Recommended Age: 2 months, 4 months, 6 months, 12-15 months'), ('PCV13', 'Recommended Age: 2 months, 4 months, 6 months, 12-15 months'), ('RV', ' Recommended Age: 2 months, 4 months'), ('MMR', ' Recommended Age: 12-15 months'), ('Varicella', 'Recommended Age: 12-15 months'), ('HepA', 'Recommended Age: 12-18 months'), ('MenACWY', ' Recommended Age: 12-15 months'), ('DTaP-IPV-HiB-HepB', '  Recommended Age: 2 months, 4 months, 6 months'), ('Influenza', ' Recommended Age: Annually from 6 months onwards')], max_length=100, null=True, unique=True),
        ),
    ]
