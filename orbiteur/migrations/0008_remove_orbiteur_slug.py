# Generated by Django 4.2.3 on 2023-07-07 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orbiteur', '0007_orbiteur_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orbiteur',
            name='slug',
        ),
    ]
