from django.contrib.auth.models import User
from django.db import models
import uuid

class Paciente(models.Model):
    paciente_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(verbose_name="número do cpf", max_length=11)
    data_cadastro = models.DateField()


class Vacina(models.Model):
    vacina_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descricao = models.CharField(max_length=255)
    sigla = models.CharField(max_length=15)
    doses = models.IntegerField(default=1)

class LoteVacina(models.Model):
    lote_vacina_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(max_length=255)
    data_validade = models.DateField()
    quantidade = models.IntegerField()
    quantidade_estoque = models.IntegerField()
    vacina = models.ForeignKey(Vacina, on_delete=models.PROTECT)

class Municipio(models.Model):
    uf = models.IntegerField()
    nome_uf = models.CharField(max_length=20)
    codigo_municipio = models.IntegerField()
    nome_municipio = models.CharField(max_length=100)

class Estabelecimento(models.Model):
    co_unidade = models.IntegerField()
    nome_fantasi = models.CharField(max_length=32)
    co_cnes = models.IntegerField()
    nu_cnpj_mantenedora = models.IntegerField()
    tp_pfpj = models.IntegerField()
    nivel_dep = models.IntegerField()
    no_razao_social = models.CharField(max_length=32)
    no_fantasia = models.CharField(max_length=32)
    no_logradouro = models.CharField(max_length=32)
    nu_endereco = models.IntegerField()
    no_complemento = models.CharField(max_length=32)
    no_bairro = models.CharField(max_length=32)
    co_cep = models.IntegerField()
    co_regiao_saude = models.IntegerField()
    co_micro_regiao = models.IntegerField()
    co_distrito_sanitario = models.IntegerField()
    co_distrito_administrativo = models.IntegerField()
    nu_telefone = models.IntegerField()
    nu_fax = models.IntegerField()
    no_email = models.CharField(max_length=32)
    nu_cpf = models.IntegerField()
    nu_cnpj = models.IntegerField()
    co_atividade = models.IntegerField()
    co_clientela = models.IntegerField()
    nu_alvara = models.IntegerField()
    dt_expedicao = models.DateField()
    tp_orgao_expedidor = models.IntegerField()
    dt_val_lic_sani = models.DateField()
    tp_lic_sani = models.IntegerField()
    tp_unidade = models.IntegerField()
    co_turno_atendimento = models.IntegerField()
    co_estado_gestor = models.IntegerField()
    co_municipio_gestor = models.IntegerField()
    dt_atualizacao = models.DateField()
    co_usuario = models.IntegerField()
    co_cpfdiretorcln = models.IntegerField()
    reg_diretorcln = models.IntegerField()
    st_adesao_filantrop = models.CharField(max_length=32)
    co_motivo_desab = models.IntegerField()
    no_url = models.CharField(max_length=32)
    nu_latitude = models.IntegerField()
    nu_longitude = models.IntegerField()
    dt_atu_geo = models.DateField()
    no_usuario_geo = models.CharField(max_length=32)
    co_natureza_jur = models.IntegerField()
    tp_estab_sempre_aberto = models.CharField(max_length=1)
    st_geracredito_gerente_sgif = models.CharField(max_length=32)
    st_conexao_internet = models.CharField(max_length=1)
    co_tipo_unidade = models.IntegerField()
    no_fantasia_abrev = models.CharField(max_length=32)
    tp_gestao = models.CharField(max_length=1)
    dt_atualizacao_origem = models.DateField()
    co_tipo_estabelecimento = models.IntegerField()
    co_atividade_principal = models.IntegerField()
    st_contrato_formalizado = models.CharField(max_length=32)
    ds_natureza_jur = models.CharField(max_length=32)

class Vacinacao(models.Model):
    vacinacao_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data_solicitacao = models.DateField()
    data_agendamento = models.DateField()
    data_vacinacao = models.DateField()
    data_aprovado = models.DateField()
    privada = models.BooleanField()
    vacinado = models.BooleanField()
    vacina = models.ForeignKey(Vacina, on_delete=models.PROTECT)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, null=True)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.PROTECT, null=True)
