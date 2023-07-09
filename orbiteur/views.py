from rest_framework import viewsets
from .models import Orbiteur
import requests
from rest_framework.response import Response
from .serializers import OrbiteurSerializer
from rest_framework.decorators import action


class OrbiteurViewSet(viewsets.ModelViewSet):
    queryset = Orbiteur.objects.all()
    serializer_class = OrbiteurSerializer

    def retrieve(self, request, *args, **kwargs): # récupère et met à jour les coodonnées de d'un orbiteur avce GET
        # Récupère l'objet (orbiteur) correspondant aux arguments fournis
        instance = self.get_object()
        # Initialise un serializer pour l'instance en question
        serializer = self.get_serializer(instance)
        # Définit la clé API pour l'API N2YO
        api_key = "3NT2FE-AUZUVS-3LFRV9-52CO"
        # Envoie une requête GET à l'API N2YO pour obtenir les positions de l'orbiteur
        response = requests.get(
            f'https://www.n2yo.com/rest/v1/satellite/positions/25544/41.702/-76.014/0/2?apiKey={api_key}')
        # Vérifie que la réponse est un succès (code de statut 200)
        if response.status_code == 200:
            # Récupère les positions de l'orbiteur à partir de la réponse
            position = response.json()['positions'][0]
            # Met à jour l'instance de l'orbiteur avec les nouvelles positions
            instance.latitude = position['satlatitude']
            instance.longitude = position['satlongitude']
            # Enregistre l'instance mise à jour dans la base de données
            instance.save()
        # Renvoie les données de l'instance (orbiteur) sous forme de réponse
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs): # appellé lors d'une requête requête PATCH
        # Récupère l'objet (orbiteur) correspondant aux arguments fournis
        instance = self.get_object()
        # Initialise un serializer pour l'instance en question avec les données de la requête
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        # Vérifie que les données fournies sont valides
        serializer.is_valid(raise_exception=True)
        # Enregistre l'instance mise à jour dans la base de données
        serializer.save()
        # Récupère l'instance de l'orbiteur à partir du serializer
        orbiteur = serializer.instance
        # Définit la clé API pour l'API N2YO
        api_key = "3NT2FE-AUZUVS-3LFRV9-52CO"
        # Envoie une requête GET à l'API N2YO pour obtenir les positions de l'orbiteur
        response = requests.get(
            f'https://www.n2yo.com/rest/v1/satellite/positions/25544/41.702/-76.014/0/2?apiKey={api_key}')
        # Récupère les données de la réponse
        data = response.json()
        # Récupère les positions de l'orbiteur à partir des données
        position = data['positions'][0]
        # Met à jour l'orbiteur avec les nouvelles positions
        orbiteur.latitude = position['satlatitude']
        orbiteur.longitude = position['satlongitude']
        # Enregistre l'orbiteur mis à jour dans la base de données
        orbiteur.save()
        # Renvoie les données de l'orbiteur sous forme de réponse
        return Response(serializer.data)

    @action(detail=False, methods=['post']) # utilisée dans Django REST Framework pour définir des méthodes
    # personnalisées qui devraient être routées et traitées différemment des méthodes standard CRUD
    # Définition de la méthode `update_all_coordinates`, qui prend `self` et `request` comme arguments.
    # `self` est une référence à l'instance de la classe, et `request` est l'objet de la requête HTTP entrante.
    def update_all_coordinates(self, request):

        # Boucle sur tous les objets Orbiteur existants dans la base de données.
        for orbiteur in Orbiteur.objects.all():

            # Définition de la clé API pour l'API N2YO.
            api_key = "3NT2FE-AUZUVS-3LFRV9-52CO"

            # Envoi d'une requête GET à l'API N2YO pour obtenir les informations de position du satellite
            # correspondant à `orbiteur.norad_id`.
            response = requests.get(
                f'https://www.n2yo.com/rest/v1/satellite/positions/{orbiteur.norad_id}/41.702/-76.014/0/2?apiKey={api_key}')

            # Vérification si la réponse de l'API était 200 OK.
            if response.status_code == 200:
                # Récupération des informations de position du satellite à partir de la réponse JSON de l'API.
                position = response.json()['positions'][0]

                # Mise à jour des attributs `latitude` et `longitude` de l'orbiteur avec les nouvelles coordonnées
                # obtenues à partir de l'API N2YO.
                orbiteur.latitude = position['satlatitude']
                orbiteur.longitude = position['satlongitude']

                # Sauvegarde des modifications apportées à l'orbiteur dans la base de données.
                orbiteur.save()

        # Retourne une réponse HTTP avec un message de statut indiquant que la mise à jour des coordonnées a été
        # effectuée.
        return Response({'status': 'coordinates updated'})

