from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    CreatureSerializer,
    CreatureSerializer2
)
from  apps.creature.models import Creature

class CreatureModelViewSet(viewsets.GenericViewSet):  
    def get_queryset(self):
        queryset = Creature.objects.all()
        return queryset
    
    def get_serializer_class(self):
        if self.action == 'list':
            return CreatureSerializer2
        elif self.action in ['create', 'update']:
            return CreatureSerializer
    
    def list(self, request, *args, **kwargs):
        creatures = self.get_queryset()
        serializer = self.get_serializer_class()
        data = serializer(creatures, many=True)
        return Response(data.data)

        
