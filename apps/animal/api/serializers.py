from rest_framework import serializers
from apps.animal.models import Animal
    
class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['pk', 'name', 'species', 'description']
    
class AnimalSerializer2(serializers.Serializer):
    pk = serializers.CharField(max_length=10, read_only= True)
    name = serializers.CharField(max_length=255)
    species = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    
    def create(self, validated_data):
        # new_animal = Animal.objects.create(
        #     name = validated_data.get("name"), 
        #     species = validated_data.get("species"),
        #     description = validated_data.get("description")           
        # )
        new_animal = Animal.objects.create(**validated_data)
        return new_animal
    
    def update(self, instance, validated_data):
        update_animal = instance
        update_animal.name = validated_data.get("name")
        update_animal.species = validated_data.get("species")
        update_animal.description = validated_data.get("description")
        update_animal.save()
        
        return update_animal