from rest_framework import serializers
from apps.spell.models import Spell
    
class SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spell
        fields = ['pk', 'name', 'description']
    
    