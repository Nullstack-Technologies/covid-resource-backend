# Generated by Django 3.2 on 2021-04-26 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0002_rename_enitity_entity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entity',
            name='city',
        ),
    ]