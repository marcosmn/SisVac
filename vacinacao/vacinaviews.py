from django.http import HttpResponse

from vacinacao.models import Agenda, Vacina, Municipio, Estabelecimento
from rest_framework import viewsets
from rest_framework import permissions
from vacinacao.serializers import VacinaSerializer, MunicipioSerializer, EstabelecimentoSerializer, AgendaSerializer
from rest_framework.response import Response
from rest_framework import status


class VacinaViewSet(viewsets.ModelViewSet):
    pagination_class = None
    queryset = Vacina.objects.all()
    serializer_class = VacinaSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class MunicipioViewSet(viewsets.ModelViewSet):
    pagination_class = None
    
    serializer_class = MunicipioSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        queryset = Municipio.objects.all()
        estado = self.request.query_params.get('estado', None)
        queryset = queryset.filter(uf=estado)
        return queryset

class EstadoViewSet(viewsets.ModelViewSet):
    pagination_class = None
    queryset = Municipio.objects.distinct('nome_uf')
    serializer_class = MunicipioSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

class EstabelecimentoViewSet(viewsets.ModelViewSet):
    pagination_class = None
    serializer_class = EstabelecimentoSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    def get_queryset(self):
        queryset = Estabelecimento.objects.all()
        municipio = self.request.query_params.get('municipio', None)
        queryset = queryset.filter(co_municipio_gestor=municipio)
        return queryset

class AgendaViewSet(viewsets.ModelViewSet):
    pagination_class = None
    serializer_class = AgendaSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    def get_queryset(self):
        queryset = Agenda.objects.all()
        idEstabelecimento = self.request.query_params.get('estabelecimento', None)
        estabelecimento = Estabelecimento.objects.get(co_unidade=idEstabelecimento)
        queryset = queryset.filter(estabelecimento=estabelecimento)
        return queryset