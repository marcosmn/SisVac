#from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth.models import User, Group
from vacinacao.models import Vacinacao, Paciente, Agenda
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
    queryset = Agenda.objects.all().order_by('-data_agendamento').order_by('-hora')
    serializer_class = AgendamentoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        usuario = self.request.user
        Vacinacao.objects.create(
            data_solicitacao=datetime.date.today(), 
            data_agendamento=request.data,
            vacina='BCG',
            paciente='BCG',
            estabelecimento='BCG',
        )
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
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
