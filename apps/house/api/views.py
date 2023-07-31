from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    HouseSerializer,
    HouseSerializer2
)
from  apps.house.models import House

class HouseModelViewSet(viewsets.GenericViewSet):  
    def get_queryset(self):
        queryset = House.objects.all()
        return queryset
    
    def get_serializer_class(self):
        if self.action == 'list':
            return HouseSerializer2
        elif self.action in ['create', 'update']:
            return HouseSerializer
    
    def list(self, request, *args, **kwargs):
        houses = self.get_queryset()
        serializer = self.get_serializer_class()
        data = serializer(houses, many=True)
        return Response(data.data)
    
    
        
