from django.db import models
from entreprise.models import Entreprise


class Module(models.Model):
    nom = models.CharField(max_length=100, unique=True, default='sans nom, inconnu ou non renseigné')
    fonction = models.CharField(max_length=100)
    prix = models.IntegerField()
    date_ajout = models.DateField()
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
