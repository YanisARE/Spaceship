from rest_framework import viewsets

from module.models import Module
from orbiteur.models import Orbiteur
from django.shortcuts import get_object_or_404

from module.serializers import ModuleSerializer


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

    def get_object(self):
        nom = self.kwargs.get("pk")
        return get_object_or_404(Module, nom=nom)
