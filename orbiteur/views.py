from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from .filters import OrbiteurFilter
from .models import Orbiteur
from .serializers import OrbiteurSerializer
import requests


# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated


class OrbiteurViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Orbiteur.objects.all()
    serializer_class = OrbiteurSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrbiteurFilter

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # indique que ce contenue est protégé

    # @api_view(['GET'])
    # @permission_classes([IsAuthenticated])
    # def retrieve(self, request, *args, **kwargs):
    #     response = super().retrieve(request, *args, **kwargs)
    #
    #     obj = self.get_object()
    #
    #     api_key = "3NT2FE-AUZUVS-3LFRV9-52CO"
    #
    #     try:
    #         satellite_response = requests.get(
    #             f'https://api.n2yo.com/rest/v1/satellite/positions/{obj.norad_id}/41.702/-76.014/0/2?apiKey={api_key}')
    #         satellite_response.raise_for_status()
    #     except requests.exceptions.RequestException as e:
    #         print(e)
    #         return response
    #
    #     position_data = satellite_response.json()
    #     print(position_data)
    #
    #     if 'positions' in position_data and len(position_data['positions']) > 0:
    #         position = position_data['positions'][0]
    #         obj.latitude = position['satlatitude']
    #         obj.longitude = position['satlongitude']
    #         print("LATITUDE,LONGITUDE: ", obj.latitude, obj.longitude)
    #         obj.save()
    #
    #         # Re-serialize the object with the updated data
    #         serializer = self.get_serializer(obj)
    #         response = Response(serializer.data)
    #
    #     return response
    def retrieve(self, request, *args, **kwargs):
        api_key = '3NT2FE-AUZUVS-3LFRV9-52CO'
        instance = self.get_object()

        try:
            # Make a request to the N2YO API to get the satellite data
            satellite_response = requests.get(
                f'https://api.n2yo.com/rest/v1/satellite/positions/{instance.norad_id}/41.702/-76.014/0/2?apiKey='
                f'{api_key}')
            satellite_response.raise_for_status()
            satellite_data = satellite_response.json()

            # Get the latitude and longitude from the satellite data
            latitude = satellite_data['positions'][0]['satlatitude']
            longitude = satellite_data['positions'][0]['satlongitude']

            # Update the instance's latitude and longitude
            instance.latitude = latitude
            instance.longitude = longitude
            instance.save()

            serializer = self.get_serializer(instance)
            return Response(serializer.data)

        except requests.exceptions.HTTPError as errh:
            return Response({"error": "An HTTP error occurred: " + str(errh)}, status=400)
        except requests.exceptions.ConnectionError as errc:
            return Response({"error": "A Connection error occurred: " + str(errc)}, status=400)
        except requests.exceptions.Timeout as errt:
            return Response({"error": "A Timeout error occurred: " + str(errt)}, status=400)
        except requests.exceptions.RequestException as err:
            return Response({"error": "An unexpected error occurred: " + str(err)}, status=400)
