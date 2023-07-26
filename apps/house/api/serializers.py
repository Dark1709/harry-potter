from rest_framework import serializers
from apps.house.models import House
    
class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['pk','name', 'color', 'animal', 'founder']
    
    