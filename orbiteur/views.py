from rest_framework import viewsets, mixins
from rest_framework.response import Response
from .models import Orbiteur
from .serializers import OrbiteurSerializer
import requests


class OrbiteurViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Orbiteur.objects.all()
    serializer_class = OrbiteurSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        api_key = "3NT2FE-AUZUVS-3LFRV9-52CO"

        try:
            response = requests.get(
                f'https://api.n2yo.com/rest/v1/satellite/positions/{instance.norad_id}/41.702/-76.014/0/2&apiKey={api_key}')
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(e)
            return Response(serializer.data)

        position_data = response.json()
        print(position_data)

        if 'positions' in position_data and len(position_data['positions']) > 0:
            position = position_data['positions'][0]
            instance.latitude = position['satlatitude']
            instance.longitude = position['satlongitude']
            print("LATITUDE,LONGITUDE: ", instance.latitude, instance.longitude)
            instance.save()
            serializer = self.get_serializer(instance)

        return Response(serializer.data)
