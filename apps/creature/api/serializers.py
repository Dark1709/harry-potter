from rest_framework import serializers
from apps.creature.models import Creature
    
class CreatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creature
        fields = ['pk', 'name', 'species', 'description']
    
    