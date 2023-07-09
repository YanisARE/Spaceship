from django.contrib import admin

from .models import Module


class ModuleAdmin(admin.ModelAdmin):
    ordering = ['prix']  # maintenant la page admin des modules est ordonné selon le prix
    # comme demandé dans l'exercice 2


admin.site.register(Module)
