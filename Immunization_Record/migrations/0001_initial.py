# Generated by Django 3.2.6 on 2023-10-04 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('child', '0002_auto_20231004_0934'),
        ('vaccine', '0012_alter_vaccine_vaccine_choice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Immunization_Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_administration', models.DateField(auto_now_add=True, null=True)),
                ('next_date_of_administration', models.DateField()),
                ('status', models.CharField(choices=[('Taken', 'Taken'), ('Missed', 'Missed')], default='Not administered', max_length=20)),
                ('child', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='child.child')),
                ('guardian', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='child.guardian')),
                ('vaccine', models.ManyToManyField(to='vaccine.Vaccine')),
            ],
        ),
    ]
