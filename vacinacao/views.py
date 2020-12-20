#from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth.models import User, Group
from vacinacao.models import Vacinacao
from rest_framework import viewsets
from rest_framework import permissions
from vacinacao.serializers import UserSerializer, GroupSerializer, AgendamentoSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Vacinacao.objects.all().order_by('-data_agendamento')
    serializer_class = AgendamentoSerializer
    permission_classes = [permissions.IsAuthenticated]

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
