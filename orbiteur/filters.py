import django_filters
from .models import Orbiteur


class OrbiteurFilter(django_filters.FilterSet):
    class Meta:
        model = Orbiteur
        fields = ['nom', 'norad_id', 'poids', 'type', 'latitude', 'longitude']
