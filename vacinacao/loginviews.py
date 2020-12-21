from vacinacao.models import Paciente
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from vacinacao import serializers
from vacinacao.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.models import User
from django.core.serializers import serialize
from rest_framework import status
from django.contrib.auth import logout


class UserLoginViewSet(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        if(request.user.is_authenticated == True):
            return Response({
                'logado': True,
                'username': request.user.username,
                'email': request.user.email,
                'grupos': request.user.groups.values_list('name', flat=True)
            })
        else:
            return Response({
                'logado': False
            })


class UserDadosViewSet(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        if(request.user.is_authenticated == True):
            try:
                paciente = Paciente.objects.get(user=request.user)
                return Response({
                    'nome': paciente.nome,
                    'fone': paciente.fone,
                    'cpf': paciente.cpf,
                    'data_nascimento': paciente.data_nascimento,
                    'endereco' : paciente.endereco,
                    'bairro' : paciente.bairro,
                    'cep': paciente.cep,
                    'email': request.user.email,
                })
            except Paciente.DoesNotExist:
                return Response({
                    'erro': 'Dados não encontrados'
                })
        else:
            return Response({
                'erro': 'Usuário não logado'
            })


class UserLogout(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        logout(request)
        return Response({
            'logado': False
        })
