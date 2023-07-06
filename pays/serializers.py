from rest_framework import serializers
from pays.models import Pays

class PaysSerializer(serializers.ModelSerializer):
	class Meta : 
		model = Pays
		fields = '__all__' # tous les champs

