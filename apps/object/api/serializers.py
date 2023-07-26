from rest_framework import serializers
from apps.object.models import Object
    
class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = ['pk', 'name', 'description']
    
    