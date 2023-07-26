from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import RetrieveModelMixin

from .serializers import CharacterSerializer
from  apps.character.models import Character


class CharacterAPIView(APIView):
    def get(self, request, *args, **kwargs):
        characters = Character.objects.all()
        serializer = CharacterSerializer(instance=characters, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def put(self, request, pk, *args, **kwarg):
        model = Character.objects.get(pk=pk)
        serializer = CharacterSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk, *args, **kwarg):
        character = Character.objects.get(pk=pk)
        character.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
