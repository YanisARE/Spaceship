# Generated by Django 4.2.3 on 2023-07-06 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0002_module_mom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='module',
            old_name='mom',
            new_name='nom',
        ),
    ]
