# Generated by Django 3.2.6 on 2023-09-28 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Immunization_Record', '0002_alter_immunization_record_next_date_of_administration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='immunization_record',
            name='next_date_of_administration',
            field=models.DateTimeField(),
        ),
    ]
