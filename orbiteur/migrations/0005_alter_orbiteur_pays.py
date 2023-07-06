# Generated by Django 4.2.3 on 2023-07-06 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pays', '0003_alter_pays_options'),
        ('orbiteur', '0004_alter_orbiteur_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orbiteur',
            name='pays',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pays.pays'),
        ),
    ]
