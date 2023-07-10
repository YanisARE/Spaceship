from django.contrib import admin

from .models import Pays


class PaysAdmin(admin.ModelAdmin):
    list_display = ["nom"]


admin.site.register(Pays, PaysAdmin)
