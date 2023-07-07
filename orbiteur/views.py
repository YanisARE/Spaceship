from rest_framework import viewsets
from .models import Orbiteur
import requests
from rest_framework.response import Response
from .serializers import OrbiteurSerializer


class OrbiteurViewSet(viewsets.ModelViewSet):
    queryset = Orbiteur.objects.all()
    serializer_class = OrbiteurSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Fetching the position information
        api_key = "3NT2FE-AUZUVS-3LFRV9-52CO"
        response = requests.get(
            f'https://www.n2yo.com/rest/v1/satellite/positions/25544/41.702/-76.014/0/2?apiKey={api_key}')

        if response.status_code == 200:
            position = response.json()['positions'][0]
            instance.latitude = position['satlatitude']
            instance.longitude = position['satlongitude']
            instance.save()

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Updating the coordinates of the orbiter
        orbiter = serializer.instance
        if orbiter.nom.upper() == "SPACE STATION":
            api_key = "3NT2FE-AUZUVS-3LFRV9-52CO"
            response = requests.get(
                f'https://www.n2yo.com/rest/v1/satellite/positions/25544/41.702/-76.014/0/2?apiKey={api_key}')
            data = response.json()
            position = data['positions'][0]
            orbiter.x = position['satlatitude']
            orbiter.y = position['satlongitude']
            orbiter.save()

        return Response(serializer.data)
