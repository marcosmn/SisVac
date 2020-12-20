#from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth.models import User, Group
from vacinacao.models import Vacinacao, Paciente
from rest_framework import viewsets
from rest_framework import permissions
from vacinacao.serializers import UserSerializer, GroupSerializer, AgendamentoSerializer
from vacinacao.serializers import CarteiraSerializer, FilaDeEsperaSerializer
import datetime

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Vacinacao.objects.all().order_by('-data_agendamento')
    serializer_class = AgendamentoSerializer
    permission_classes = [permissions.IsAuthenticated]

class CarteiraViewSet(viewsets.ModelViewSet):
    serializer_class = CarteiraSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        usuario = self.request.user
        queryset = Vacinacao.objects.filter(paciente=usuario.paciente).order_by('-data_agendamento')
        return queryset

class FilaDeEsperaViewSet(viewsets.ModelViewSet):
    queryset = Vacinacao.objects.filter(data_agendamento=datetime.date.today()).order_by('-data_agendamento')
    serializer_class = FilaDeEsperaSerializer
    permission_classes = [permissions.IsAuthenticated]

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
