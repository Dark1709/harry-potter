from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import SpellSerializer
from  apps.spell.models import Spell


class SpellAPIView(APIView):
    def get(self, request, *args, **kwargs):
        spells = Spell.objects.all()
        serializer = SpellSerializer(instance=spells, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = SpellSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def put(self, request, pk, *args, **kwarg):
        model = Spell.objects.get(pk=pk)
        serializer = SpellSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk, *args, **kwarg):
        spell = Spell.objects.get(pk=pk)
        spell.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
