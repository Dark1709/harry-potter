from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import LocationSerializer
from  apps.location.models import Location



class LocationAPIView(APIView):
    def get(self, request, *args, **kwargs):
        locations = Location.objects.all()
        serializer = LocationSerializer(instance=locations, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def put(self, request, pk, *args, **kwarg):
        model = Location.objects.get(pk=pk)
        serializer = LocationSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk, *args, **kwarg):
        location = Location.objects.get(pk=pk)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
