from django.db import models
from django.utils.text import slugify
from pays.models import Pays


class Orbiteur(models.Model):
    PAYS_CHOICES = (
        ('US', 'United States'),
        ('FR', 'France'),
        ('CN', 'China'),
        ('RU', 'Russia'),
        ('JP', 'Japon'),
        ('CA', 'Canada'),
        ('EU', 'Europe'),
    )
    TYPE_CHOICES = (
        ('Communication', 'Communication'),
        ('Observation', 'Observation'),
        ('Métérologie', 'Métérologie'),
        ('Navigation', 'Navigation'),
        ('Recherche', 'Recherche'),
    )

    nom = models.CharField(max_length=200, default='Orbiteur')
    # pays = models.CharField(max_length=20, choices=PAYS_CHOICES) #changé en clé étrangère vers un pays
    pays = models.ForeignKey(Pays, on_delete=models.CASCADE)
    type = models.CharField(max_length=200, choices=TYPE_CHOICES)
    poids = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    description = models.TextField(max_length=2000, default='')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)

    def __str__(self):
        return self.nom

    slug = models.SlugField(null=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)
