# Generated by Django 4.2.3 on 2023-07-07 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orbiteur', '0009_orbiteur_modules'),
    ]

    operations = [
        migrations.AddField(
            model_name='orbiteur',
            name='norad_id',
            field=models.IntegerField(default=0),
        ),
    ]
