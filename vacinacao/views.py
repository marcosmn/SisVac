#from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth.models import User, Group
from vacinacao.models import Vacinacao, Paciente
from rest_framework import viewsets
from rest_framework import permissions
from vacinacao.serializers import UserSerializer, GroupSerializer, AgendamentoSerializer
from vacinacao.serializers import CarteiraSerializer, FilaDeEsperaSerializer
import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from vacinacao.teste import retornarPosicao

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Vacinacao.objects.all().order_by('-data_agendamento')
    serializer_class = AgendamentoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        usuario = self.request.user
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(paciente=usuario.paciente)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarteiraViewSet(viewsets.ModelViewSet):
    serializer_class = CarteiraSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    def get_queryset(self):
        usuario = self.request.user
        queryset = Vacinacao.objects.filter(paciente=usuario.paciente).order_by('-data_agendamento')
        return queryset

class FilaDeEsperaViewSet(viewsets.ModelViewSet):
    queryset = Vacinacao.objects.filter(data_agendamento__date=datetime.date.today()).filter(vacinado=False).order_by('-data_agendamento')
    serializer_class = FilaDeEsperaSerializer
    permission_classes = [permissions.IsAdminUser]

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = FilaDeEsperaSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
