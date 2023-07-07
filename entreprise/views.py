from rest_framework import viewsets
from .models import Entreprise
from .serializers import EntrepriseSerializer


class EntrepriseViewSet(viewsets.ModelViewSet):
    queryset = Entreprise.objects.all()
    serializer_class = EntrepriseSerializer


