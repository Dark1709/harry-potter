from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import RetrieveModelMixin

from .serializers import  HouseSerializer
from  apps.house.models import House

class HouseAPIView(APIView):
    def get(self, request, *args, **kwargs):
        houses = House.objects.all()
        serializer = HouseSerializer(instance=houses, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def put(self, request, pk, *args, **kwarg):
        model = House.objects.get(pk=pk)
        serializer = HouseSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk, *args, **kwarg):
        house = House.objects.get(pk=pk)
        house.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
