# Generated by Django 3.2.6 on 2023-09-14 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_NGO',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='healthworker',
            name='is_healthworker',
            field=models.BooleanField(default=True),
        ),
    ]
