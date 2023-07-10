from django.contrib import admin

from orbiteur.models import Orbiteur


class OrbiteurAdmin(admin.ModelAdmin):
    list_display = ("nom", "pays", "poids", "longitude", "latitude")
    list_filter = ("nom", "pays",  "poids", "longitude", "latitude")

# Register your models here.
admin.site.register(Orbiteur,OrbiteurAdmin)
