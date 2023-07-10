from rest_framework import viewsets, mixins
from .models import Entreprise
from .serializers import EntrepriseSerializer


class EntrepriseViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer
