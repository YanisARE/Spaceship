from rest_framework import serializers
from orbiteur.models import Orbiteur

class OrbiteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orbiteur
        fields = '__all__'  # sert à utiliser tous les champs du modèle.
