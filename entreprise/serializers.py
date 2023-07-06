from rest_framework import serializers
from entreprise.models import Entreprise

class EntrepriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entreprise
        fields = '__all__'  # Utiliser tous les champs du modèle.

