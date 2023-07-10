from rest_framework import viewsets, mixins
from .models import Orbiteur
from .serializers import OrbiteurSerializer


class OrbiteurViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Orbiteur.objects.all()
    serializer_class = OrbiteurSerializer

