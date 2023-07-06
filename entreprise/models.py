from django.db import models

from pays.models import Pays


class Entreprise(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    pays = models.ForeignKey(Pays, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom