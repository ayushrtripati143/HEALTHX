# Generated by Django 4.0.4 on 2023-02-28 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient_appointment',
            old_name='addres',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='patient_appointment',
            name='emai',
        ),
    ]
