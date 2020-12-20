from rest_framework import generics, viewsets
from rest_framework.views import APIView
from vacinacao import serializers
from vacinacao.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.models import User
from django.core.serializers import serialize 


class UserLoginViewSet(APIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        if(request.user.is_authenticated==True):
            return  Response({
                'logado' : True,
                'username': request.user.username,
                'email': request.user.email,
                'grupos': request.user.groups.values_list('name',flat = True)
            })
        else:
            return  Response({
                'logado' : False
            })


