import django_filters
from .models import Entreprise


class EntrepriseFilter(django_filters.FilterSet):
    class Meta:
        model = Entreprise
        fields = ['nom', 'pays']
