# Generated by Django 3.0.3 on 2020-09-14 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campsite_checker', '0002_auto_20200913_2205'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Campgroundz',
        ),
        migrations.DeleteModel(
            name='Zonez',
        ),
    ]
