from rest_framework import serializers
from apps.character.models import Character
    
class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['pk', 'name', 'species', 'gender', 'house', 'school', 'birthdate', 'deathdate', 'bio']
    

class CharacterSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['pk']