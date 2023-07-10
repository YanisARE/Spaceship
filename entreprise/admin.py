from django.contrib import admin

from .models import Entreprise


class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ("nom", "pays")
    list_filter = ("nom", "pays")


admin.site.register(Entreprise, EntrepriseAdmin)
