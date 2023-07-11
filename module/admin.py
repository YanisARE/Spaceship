from django.contrib import admin
from .models import Module


class ModuleAdmin(admin.ModelAdmin):
     #ordering = ['prix']  # maintenant la page admin des modules est ordonné selon le prix
     list_display = ("nom","fonction","prix","date_ajout","entreprise")
     list_filter = ("nom","fonction","prix","date_ajout","entreprise")
     search_fields = ["nom","fonction","prix","date_ajout","entreprise"]

admin.site.register(Module,ModuleAdmin)
