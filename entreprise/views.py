from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins

from .filters import EntrepriseFilter
from .models import Entreprise
from .serializers import EntrepriseSerializer


class EntrepriseViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EntrepriseFilter
