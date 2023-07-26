from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import RetrieveModelMixin

from .serializers import CreatureSerializer
from  apps.creature.models import Creature


class CreatureAPIView(APIView):
    def get(self, request, *args, **kwargs):
        creatures = Creature.objects.all()
        serializer = CreatureSerializer(instance=creatures, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = CreatureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def put(self, request, pk, *args, **kwarg):
        model = Creature.objects.get(pk=pk)
        serializer = CreatureSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk, *args, **kwarg):
        creature = Creature.objects.get(pk=pk)
        creature.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
