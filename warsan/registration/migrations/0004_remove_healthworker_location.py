# Generated by Django 3.2.6 on 2023-09-15 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20230915_0430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='healthworker',
            name='location',
        ),
    ]