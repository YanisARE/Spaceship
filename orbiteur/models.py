from django.db import models

from pays.models import Pays


class Orbiteur(models.Model):
    PAYS_CHOICES = (
        ('US', 'United States'),
        ('FR', 'France'),
        ('CN', 'China'),
        ('RU', 'Russia'),
        ('IT', 'Italy'),
    )
    TYPE_CHOICES = (
        ('Communication', 'Communication'),
        ('Observation', 'Observation'),
        ('Métérologie', 'Métérologie'),
        ('Navigation', 'Navigation'),
        ('Recherche', 'Recherche'),
    )

    nom = models.CharField(max_length=200, default='Orbiteur')
    #pays = models.CharField(max_length=20, choices=PAYS_CHOICES) #changé en clé étrangère vers un pays
    pays = models.ForeignKey(Pays, on_delete=models.CASCADE)
    type = models.CharField(max_length=200, choices=TYPE_CHOICES)
    poids = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    description = models.TextField(max_length=2000, default='')

    def __str__(self):
        return self.nom
