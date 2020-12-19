from django.contrib.auth.models import User
from rest_framework import serializers
from vacinacao.models import Vacinacao, Estabelecimento

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']

class CarteiraSerializer(serializers.Serializer):
    codigo = serializers.IntegerField(read_only=True)
    proprietario = serializers.CharField(max_length=100)
    quantidade_vacinas = serializers.IntegerField(read_only=True)

class AgendamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vacinacao
        fields = ['data_solicitacao', 'data_agendamento', 'vacina', 'user_id', 'estabelecimento']

class EstabelecimentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estabelecimento
        fields = ['co_unidade', 'co_cnes', 'nu_cnpj_mantenedora', 'tp_pfpj', 'nivel_dep', 'no_razao_social', 
        'no_fantasia', 'no_logradouro', 'nu_endereco', 'no_complemento', 'no_bairro', 'co_cep', 'co_regiao_saude', 
        'co_micro_regiao', 'co_distrito_sanitario', 'co_distrito_administrativo', 'nu_telefone', 'nu_fax', 
        'no_email', 'nu_cpf', 'nu_cnpj', 'co_atividade', 'co_clientela', 'nu_alvara', 'dt_expedicao', 
        'tp_orgao_expedidor', 'dt_val_lic_sani', 'tp_lic_sani', 'tp_unidade', 'co_turno_atendimento', 
        'co_estado_gestor', 'co_municipio_gestor', 'dt_atualizacao', 'co_usuario', 'co_cpfdiretorcln', 
        'reg_diretorcln', 'st_adesao_filantrop', 'co_motivo_desab', 'no_url', 'nu_latitude', 'nu_longitude', 
        'dt_atu_geo', 'no_usuario_geo', 'co_natureza_jur', 'tp_estab_sempre_aberto', 'st_geracredito_gerente_sgif', 
        'st_conexao_internet', 'co_tipo_unidade', 'no_fantasia_abrev', 'tp_gestao', 'dt_atualizacao_origem', 
        'co_tipo_estabelecimento', 'co_atividade_principal', 'st_contrato_formalizado', 'ds_natureza_jur']
