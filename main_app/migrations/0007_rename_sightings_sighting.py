# Generated by Django 4.1.1 on 2022-10-06 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_sightings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sightings',
            new_name='Sighting',
        ),
    ]