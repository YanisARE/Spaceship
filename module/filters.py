import django_filters
from .models import Module


class ModuleFilter(django_filters.FilterSet):
    class Meta:
        model = Module
        fields = ['nom', 'fonction', 'prix', 'date_ajout', 'entreprise']