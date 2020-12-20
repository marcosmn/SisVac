# Generated by Django 3.1.4 on 2020-12-20 00:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estabelecimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co_unidade', models.IntegerField()),
                ('co_cnes', models.IntegerField()),
                ('nu_cnpj_mantenedora', models.IntegerField()),
                ('tp_pfpj', models.IntegerField()),
                ('nivel_dep', models.IntegerField()),
                ('no_razao_social', models.CharField(max_length=32)),
                ('no_fantasia', models.CharField(max_length=32)),
                ('no_logradouro', models.CharField(max_length=32)),
                ('nu_endereco', models.IntegerField()),
                ('no_complemento', models.CharField(max_length=32)),
                ('no_bairro', models.CharField(max_length=32)),
                ('co_cep', models.IntegerField()),
                ('co_regiao_saude', models.IntegerField()),
                ('co_micro_regiao', models.IntegerField()),
                ('co_distrito_sanitario', models.IntegerField()),
                ('co_distrito_administrativo', models.IntegerField()),
                ('nu_telefone', models.IntegerField()),
                ('nu_fax', models.IntegerField()),
                ('no_email', models.CharField(max_length=32)),
                ('nu_cpf', models.IntegerField()),
                ('nu_cnpj', models.IntegerField()),
                ('co_atividade', models.IntegerField()),
                ('co_clientela', models.IntegerField()),
                ('nu_alvara', models.IntegerField()),
                ('dt_expedicao', models.DateField()),
                ('tp_orgao_expedidor', models.IntegerField()),
                ('dt_val_lic_sani', models.DateField()),
                ('tp_lic_sani', models.IntegerField()),
                ('tp_unidade', models.IntegerField()),
                ('co_turno_atendimento', models.IntegerField()),
                ('co_estado_gestor', models.IntegerField()),
                ('co_municipio_gestor', models.IntegerField()),
                ('dt_atualizacao', models.DateField()),
                ('co_usuario', models.IntegerField()),
                ('co_cpfdiretorcln', models.IntegerField()),
                ('reg_diretorcln', models.IntegerField()),
                ('st_adesao_filantrop', models.CharField(max_length=32)),
                ('co_motivo_desab', models.IntegerField()),
                ('no_url', models.CharField(max_length=32)),
                ('nu_latitude', models.IntegerField()),
                ('nu_longitude', models.IntegerField()),
                ('dt_atu_geo', models.DateField()),
                ('no_usuario_geo', models.CharField(max_length=32)),
                ('co_natureza_jur', models.IntegerField()),
                ('tp_estab_sempre_aberto', models.CharField(max_length=1)),
                ('st_geracredito_gerente_sgif', models.CharField(max_length=32)),
                ('st_conexao_internet', models.CharField(max_length=1)),
                ('co_tipo_unidade', models.IntegerField()),
                ('no_fantasia_abrev', models.CharField(max_length=32)),
                ('tp_gestao', models.CharField(max_length=1)),
                ('dt_atualizacao_origem', models.DateField()),
                ('co_tipo_estabelecimento', models.IntegerField()),
                ('co_atividade_principal', models.IntegerField()),
                ('st_contrato_formalizado', models.CharField(max_length=1)),
                ('ds_natureza_jur', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('municipio_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('uf', models.IntegerField()),
                ('nome_uf', models.CharField(max_length=20)),
                ('codigo_municipio', models.IntegerField()),
                ('nome_municipio', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('paciente_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=254)),
                ('cpf', models.CharField(max_length=11, null=True, verbose_name='número do cpf')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vacina',
            fields=[
                ('vacina_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=255)),
                ('sigla', models.CharField(max_length=15)),
                ('doses', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Vacinacao',
            fields=[
                ('vacinacao_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('data_solicitacao', models.DateTimeField(auto_now_add=True)),
                ('data_agendamento', models.DateTimeField()),
                ('data_vacinacao', models.DateTimeField()),
                ('data_aprovado', models.DateTimeField()),
                ('privada', models.BooleanField()),
                ('vacinado', models.BooleanField()),
                ('estabelecimento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='vacinacao.estabelecimento')),
                ('paciente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='vacinacao.paciente')),
                ('vacina', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vacinacao.vacina')),
            ],
        ),
        migrations.CreateModel(
            name='LoteVacina',
            fields=[
                ('lote_vacina_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=255)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_validade', models.DateField()),
                ('quantidade', models.IntegerField()),
                ('quantidade_estoque', models.IntegerField()),
                ('vacina', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vacinacao.vacina')),
            ],
        ),
    ]
