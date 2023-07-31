from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ObjectSerializer
from  apps.object.models import Object


class ObjectAPIView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Object.objects.all()
        serializer = ObjectSerializer(instance=objects, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = ObjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def put(self, request, pk, *args, **kwarg):
        model = Object.objects.get(pk=pk)
        serializer = ObjectSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk, *args, **kwarg):
        object = Object.objects.get(pk=pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
