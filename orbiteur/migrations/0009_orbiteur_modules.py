# Generated by Django 4.2.3 on 2023-07-07 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0003_rename_mom_module_nom'),
        ('orbiteur', '0008_remove_orbiteur_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='orbiteur',
            name='modules',
            field=models.ManyToManyField(related_name='orbiteurs', to='module.module'),
        ),
    ]
