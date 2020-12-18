from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']

class CarteiraSerializer(serializers.Serializer):
    codigo = serializers.IntegerField(read_only=True)
    proprietario = serializers.CharField(max_length=100)
    quantidade_vacinas = serializers.IntegerField(read_only=True)