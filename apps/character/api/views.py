from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    CharacterSerializer, 
    CharacterSerializer2
)
from  apps.character.models import Character



class CharacterModelViewSet(viewsets.ModelViewSet):
    model = Character
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer2
    permission_classes = [IsAuthenticated, ]  
    
    def get_permissions(self): #lista de permisos que retorna booleanos
        return super().get_permissions()
    
    def check_permissions(self, request): #valida los booleanos que retorne get permissions
        return super().check_permissions(request)
    
    
    
    
    
    
    ##Necesario con GenericViewSet
    # def get_queryset(self):
    #     queryset = Character.objects.all()
    #     return queryset
    
    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return CharacterSerializer2
    #     elif self.action in ['create', 'update']:
    #         return CharacterSerializer
    
    # def list(self, request, *args, **kwargs):
    #     characters = self.get_queryset()
    #     serializer = self.get_serializer_class()
    #     data = serializer(characters, many=True)
    #     return Response(data.data)


# class CharacterAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         characters = Character.objects.all()
#         serializer = CharacterSerializer(instance=characters, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, *args, **kwargs):
#         serializer = CharacterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
    
#     def put(self, request, pk, *args, **kwarg):
#         model = Character.objects.get(pk=pk)
#         serializer = CharacterSerializer(model, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#     def delete(self, request, pk, *args, **kwarg):
#         character = Character.objects.get(pk=pk)
#         character.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
