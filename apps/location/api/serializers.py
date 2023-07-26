from rest_framework import serializers
from apps.location.models import Location
    
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['pk', 'name', 'description']
    
    