# Generated by Django 3.0.3 on 2020-09-14 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campgrounds', '0002_auto_20200913_2359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campground',
            old_name='parent_id',
            new_name='parent_name',
        ),
    ]
