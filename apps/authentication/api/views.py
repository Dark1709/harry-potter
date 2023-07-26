""" from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import RetrieveModelMixin

from .serializers import UserSerializer
from  apps.authentication.models import Authentication

class UserList(APIView):
    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            print("es valido".serializer.data)
            return Response(serializer.data)
        else:
            print("No es valido".serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
 """