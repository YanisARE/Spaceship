# from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from .models import Pays

from pays.serializers import PaysSerializer


class PaysViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Pays.objects.all()
    serializer_class = PaysSerializer

    # def get_object(self):
    #     nom = self.kwargs.get("pk")
    #     return get_object_or_404(Pays, nom=nom)
