import django_filters
from .models import Pays


class PaysFilter(django_filters.FilterSet):
    class Meta:
        model = Pays
        fields = ['nom']