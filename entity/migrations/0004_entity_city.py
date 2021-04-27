# Generated by Django 3.2 on 2021-04-26 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0003_remove_entity_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='cities_light.subregion'),
        ),
    ]
