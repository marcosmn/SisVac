from django.contrib.auth.models import User, Group
from rest_framework import serializers
from vacinacao.models import Vacinacao

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CarteiraSerializer(serializers.Serializer):
    codigo = serializers.IntegerField(read_only=True)
    proprietario = serializers.CharField(max_length=100)
    quantidade_vacinas = serializers.IntegerField(read_only=True)

class AgendamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vacinacao
        fields = ['data_solicitacao', 'data_agendamento', 'vacina', 'paciente', 'estabelecimento']