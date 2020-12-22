from django.contrib.auth.models import User, Group
from rest_framework import serializers
from vacinacao.models import Municipio, Vacinacao, Estabelecimento, Paciente, Agenda, Vacina

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CarteiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacinacao
        fields = ['data_solicitacao', 'data_agendamento', 'data_vacinacao', 'data_aprovado' , 
        'privada', 'vacinado', 'vacina', 'paciente', 'estabelecimento']

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ['data_agendamento', 'hora', 'vacina', 'estabelecimento']

class FilaDeEsperaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacinacao
        fields = ['vacinacao_id', 'vacinado', 'vacina', 'paciente', 'estabelecimento']

class VacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacina
        fields = ['vacina_id', 'descricao', 'sigla', 'doses']

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = ['id', 'uf', 'nome_uf', 'codigo_municipio', 'nome_municipio']

class EstabelecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estabelecimento
        fields = ['co_unidade', 'no_fantasia', 'co_municipio_gestor']

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ['agenda_id', 'data_agendamento', 'hora', 'vacina', 'estabelecimento']