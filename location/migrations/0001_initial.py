# Generated by Django 3.2.6 on 2023-09-28 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('Banadir', 'Banadir'), ('Bari', 'Bari'), ('Bay', 'Bay'), ('Galguduud', 'Galguduud'), ('Gedo', 'Gedo'), ('Hiran', 'Hiran'), ('Jubbada_Dhexe', 'Jubbada Dhexe'), ('Jubbada_Hoose', 'Jubbada Hoose'), ('Mudug', 'Mudug'), ('Nugaal', 'Nugaal'), ('Sanaag', 'Sanaag'), ('Shabeellaha_Dhexe', 'Shabeellaha Dhexe'), ('Shabeellaha_Hoose', 'Shabeellaha Hoose'), ('Sool', 'Sool'), ('Togdheer', 'Togdheer'), ('Woqooyi_Galbeed', 'Woqooyi Galbeed'), ('Awdal', 'Awdal'), ('Bakool', 'Bakool'), ('Lower_Juba', 'Lower Juba')], default='Banadir', max_length=32, unique=True)),
                ('longitude', models.FloatField(default=0.0)),
                ('latitude', models.FloatField(default=0.0)),
            ],
            options={
                'db_table': 'Location',
            },
        ),
    ]
