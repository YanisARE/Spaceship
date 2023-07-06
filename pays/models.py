from django.db import models


class Pays(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Pays'

    def __str__(self):
        return self.nom