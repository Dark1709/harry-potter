from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import AnimalSerializer, AnimalSerializer2
from  apps.animal.models import Animal


class AnimalAPIView(APIView):
    def get(self, request, *args, **kwargs):
        animals = Animal.objects.all()
        serializer = AnimalSerializer(instance=animals, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = AnimalSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def put(self, request, pk, *args, **kwarg):
        model = Animal.objects.get(pk=pk)
        serializer = AnimalSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk, *args, **kwarg):
        animal = Animal.objects.get(pk=pk)
        animal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
