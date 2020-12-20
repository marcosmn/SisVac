from django.contrib.auth.models import User
from django.db import models
import uuid




class Vacina(models.Model):
    vacina_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descricao = models.CharField(max_length=255)
    sigla = models.CharField(max_length=15)
    doses = models.IntegerField(default=1)

class LoteVacina(models.Model):
    lote_vacina_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(max_length=255)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_validade = models.DateField()
    quantidade = models.IntegerField()
    quantidade_estoque = models.IntegerField()
    vacina = models.ForeignKey(Vacina, on_delete=models.PROTECT)

class Estabelecimento(models.Model):
    co_unidade = models.CharField(max_length=32)
    co_cnes = models.CharField(max_length=32)
    nu_cnpj_mantenedora = models.CharField(max_length=32)
    tp_pfpj = models.CharField(max_length=2)
    nivel_dep = models.CharField(max_length=2)
    no_razao_social = models.CharField(max_length=32)
    no_fantasia = models.CharField(max_length=32)
    no_logradouro = models.CharField(max_length=32)
    nu_endereco = models.CharField(max_length=32)
    no_complemento = models.CharField(max_length=32)
    no_bairro = models.CharField(max_length=32)
    co_cep = models.CharField(max_length=32)
    co_regiao_saude = models.CharField(max_length=32)
    co_micro_regiao = models.CharField(max_length=32)
    co_distrito_sanitario = models.CharField(max_length=32)
    co_distrito_administrativo = models.CharField(max_length=32)
    nu_telefone = models.CharField(max_length=32)
    nu_fax = models.CharField(max_length=32)
    no_email = models.CharField(max_length=32)
    nu_cpf = models.CharField(max_length=32)
    nu_cnpj = models.CharField(max_length=32)
    co_atividade = models.CharField(max_length=32)
    co_clientela = models.CharField(max_length=32)
    nu_alvara = models.CharField(max_length=32)
    dt_expedicao = models.CharField(max_length=32)
    tp_orgao_expedidor = models.CharField(max_length=32)
    dt_val_lic_sani = models.CharField(max_length=32)
    tp_lic_sani = models.CharField(max_length=32)
    tp_unidade = models.CharField(max_length=32)
    co_turno_atendimento = models.CharField(max_length=32)
    co_estado_gestor = models.CharField(max_length=32)
    co_municipio_gestor = models.CharField(max_length=32)
    dt_atualizacao = models.CharField(max_length=32)
    co_usuario = models.CharField(max_length=32)
    co_cpfdiretorcln = models.CharField(max_length=32)
    reg_diretorcln = models.CharField(max_length=32)
    st_adesao_filantrop = models.CharField(max_length=32)
    co_motivo_desab = models.CharField(max_length=32)
    no_url = models.CharField(max_length=32)
    nu_latitude = models.CharField(max_length=32)
    nu_longitude = models.CharField(max_length=32)
    dt_atu_geo = models.CharField(max_length=32)
    no_usuario_geo = models.CharField(max_length=32)
    co_natureza_jur = models.CharField(max_length=32)
    tp_estab_sempre_aberto = models.CharField(max_length=1)
    st_geracredito_gerente_sgif = models.CharField(max_length=32)
    st_conexao_internet = models.CharField(max_length=1)
    co_tipo_unidade = models.CharField(max_length=32)
    no_fantasia_abrev = models.CharField(max_length=32)
    tp_gestao = models.CharField(max_length=1)
    dt_atualizacao_origem = models.CharField(max_length=32)
    co_tipo_estabelecimento = models.CharField(max_length=32)
    co_atividade_principal = models.CharField(max_length=32)
    st_contrato_formalizado = models.CharField(max_length=1)
    ds_natureza_jur = models.CharField(max_length=32)
    funcionarios = models.ManyToManyField(Profissional, through='Vinculo')

class Municipio(models.Model):
    uf = models.IntegerField()
    nome_uf = models.CharField(max_length=20)
    codigo_municipio = models.IntegerField()
    nome_municipio = models.CharField(max_length=100)

class Paciente(models.Model):
    paciente_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=254)
    nome = models.CharField(max_length=254,  null=True)
    fone = models.CharField(max_length=20,  null=True)
    endereco = models.CharField(max_length=20,  null=True)
    cep = models.CharField(max_length=20,  null=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    cpf = models.CharField(verbose_name="número do cpf", max_length=11,  null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT, null=True)

class Vacinacao(models.Model):
    vacinacao_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    data_agendamento = models.DateTimeField()
    data_vacinacao = models.DateTimeField()
    data_aprovado = models.DateTimeField()
    privada = models.BooleanField()
    vacinado = models.BooleanField()
    vacina = models.ForeignKey(Vacina, on_delete=models.PROTECT)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.PROTECT)

class Vinculo(models.Model):
    vinculo_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data_entrada = models.DateTimeField()
    data_saida = models.DateTimeField()
    vinculado = models.BooleanField()
    profissional = models.ForeignKey(Profissional, on_delete=models.PROTECT)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.PROTECT)

class Profissional(models.Model):
    profissional_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class Meta:
        permissions = (
            ('aplicar_vacina', "Pode aplicar vacina"),
            ('aprovar_vacina', "Pode aprovar vacina")
        )