""" from rest_framework import serializers
from apps.authentication.models import Authentication

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    
    def validate(self, attrs):
        name = attrs.get('name')
        email = attrs.get('email')
        if not "@" in email:
            raise serializers.validationError({"email": "El email debe ser valido"})
        
        if not "." in email.split("@")[1]:
            raise serializers.validationError({"email": "El email debe ser valido"})
        
        return super().validate(attrs)  
    
    def  to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation
    
    
     """