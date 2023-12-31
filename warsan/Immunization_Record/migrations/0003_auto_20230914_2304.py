# Generated by Django 3.2.6 on 2023-09-14 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0002_alter_vaccine_name_alter_vaccine_recommended_dose_and_more'),
        ('child', '0003_alter_child_date_of_birth'),
        ('Immunization_Record', '0002_auto_20230911_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='immunization_record',
            name='child',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='child.child'),
        ),
        migrations.AddField(
            model_name='immunization_record',
            name='vaccine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vaccine.vaccine'),
        ),
    ]
