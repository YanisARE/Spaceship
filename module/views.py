from rest_framework import viewsets, mixins

from module.models import Module
# from django.shortcuts import get_object_or_404

from module.serializers import ModuleSerializer


class ModuleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

    # def get_object(self):
    #     nom = self.kwargs.get("pk")
    #     return get_object_or_404(Module, nom=nom)
