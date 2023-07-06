from django.db import models
from entreprise.models import Entreprise

class Module(models.Model):
    fonction = models.CharField(max_length=100)
    prix = models.IntegerField()
    date_ajout = models.DateField()
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)

    def __str__(self):
        return self.fonction
