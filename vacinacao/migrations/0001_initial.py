# Generated by Django 3.1.4 on 2020-12-21 21:40

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
                ('co_unidade', models.CharField(max_length=255)),
                ('co_cnes', models.CharField(max_length=255)),
                ('nu_cnpj_mantenedora', models.CharField(max_length=255)),
                ('tp_pfpj', models.CharField(max_length=255)),
                ('nivel_dep', models.CharField(max_length=255)),
                ('no_razao_social', models.CharField(max_length=255)),
                ('no_fantasia', models.CharField(max_length=255)),
                ('no_logradouro', models.CharField(max_length=255)),
                ('nu_endereco', models.CharField(max_length=255)),
                ('no_complemento', models.CharField(max_length=255)),
                ('no_bairro', models.CharField(max_length=255)),
                ('co_cep', models.CharField(max_length=255)),
                ('co_regiao_saude', models.CharField(max_length=255)),
                ('co_micro_regiao', models.CharField(max_length=255)),
                ('co_distrito_sanitario', models.CharField(max_length=255)),
                ('co_distrito_administrativo', models.CharField(max_length=255)),
                ('nu_telefone', models.CharField(max_length=255)),
                ('nu_fax', models.CharField(max_length=255)),
                ('no_email', models.CharField(max_length=255)),
                ('nu_cpf', models.CharField(max_length=255)),
                ('nu_cnpj', models.CharField(max_length=255)),
                ('co_atividade', models.CharField(max_length=255)),
                ('co_clientela', models.CharField(max_length=255)),
                ('nu_alvara', models.CharField(max_length=255)),
                ('dt_expedicao', models.CharField(max_length=255)),
                ('tp_orgao_expedidor', models.CharField(max_length=255)),
                ('dt_val_lic_sani', models.CharField(max_length=255)),
                ('tp_lic_sani', models.CharField(max_length=255)),
                ('tp_unidade', models.CharField(max_length=255)),
                ('co_turno_atendimento', models.CharField(max_length=255)),
                ('co_estado_gestor', models.CharField(max_length=255)),
                ('co_municipio_gestor', models.CharField(max_length=255)),
                ('dt_atualizacao', models.CharField(max_length=255)),
                ('co_usuario', models.CharField(max_length=255)),
                ('co_cpfdiretorcln', models.CharField(max_length=255)),
                ('reg_diretorcln', models.CharField(max_length=255)),
                ('st_adesao_filantrop', models.CharField(max_length=255)),
                ('co_motivo_desab', models.CharField(max_length=255)),
                ('no_url', models.CharField(max_length=255)),
                ('nu_latitude', models.CharField(max_length=255)),
                ('nu_longitude', models.CharField(max_length=255)),
                ('dt_atu_geo', models.CharField(max_length=255)),
                ('no_usuario_geo', models.CharField(max_length=255)),
                ('co_natureza_jur', models.CharField(max_length=255)),
                ('tp_estab_sempre_aberto', models.CharField(max_length=255)),
                ('st_geracredito_gerente_sgif', models.CharField(max_length=255)),
                ('st_conexao_internet', models.CharField(max_length=255)),
                ('co_tipo_unidade', models.CharField(max_length=255)),
                ('no_fantasia_abrev', models.CharField(max_length=255)),
                ('tp_gestao', models.CharField(max_length=255)),
                ('dt_atualizacao_origem', models.CharField(max_length=255)),
                ('co_tipo_estabelecimento', models.CharField(max_length=255)),
                ('co_atividade_principal', models.CharField(max_length=255)),
                ('st_contrato_formalizado', models.CharField(max_length=255)),
                ('ds_natureza_jur', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('nome', models.CharField(max_length=254, null=True)),
                ('fone', models.CharField(max_length=20, null=True)),
                ('endereco', models.CharField(max_length=254, null=True)),
                ('bairro', models.CharField(max_length=254, null=True)),
                ('cep', models.CharField(max_length=20, null=True)),
                ('data_nascimento', models.CharField(max_length=30, null=True)),
                ('cpf', models.CharField(max_length=11, null=True, verbose_name='número do cpf')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('municipio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='vacinacao.municipio')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('profissional_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=254, null=True)),
                ('salario', models.IntegerField(null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
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
            name='VinculoProfissional',
            fields=[
                ('vinculo_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('data_entrada', models.DateTimeField()),
                ('data_saida', models.DateTimeField()),
                ('vinculado', models.BooleanField()),
                ('estabelecimento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vacinacao.estabelecimento')),
                ('profissional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vacinacao.profissional')),
            ],
        ),
        migrations.CreateModel(
            name='Vacinacao',
            fields=[
                ('vacinacao_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('data_solicitacao', models.DateTimeField(auto_now_add=True)),
                ('data_agendamento', models.DateTimeField()),
                ('data_vacinacao', models.DateTimeField(null=True)),
                ('data_aprovado', models.DateTimeField(null=True)),
                ('privada', models.BooleanField(default=False)),
                ('vacinado', models.BooleanField(default=False)),
                ('estabelecimento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vacinacao.estabelecimento')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vacinacao.paciente')),
                ('vacina', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vacinacao.vacina')),
            ],
            options={
                'permissions': (('aplicar_vacina', 'Pode aplicar vacina'), ('aprovar_vacina', 'Pode aprovar vacina')),
            },
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
        migrations.AddField(
            model_name='estabelecimento',
            name='funcionarios',
            field=models.ManyToManyField(through='vacinacao.VinculoProfissional', to='vacinacao.Profissional'),
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('agenda_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('data_agendamento', models.DateField()),
                ('hora', models.IntegerField()),
                ('estabelecimento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vacinacao.estabelecimento')),
                ('vacina', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vacinacao.vacina')),
            ],
        ),
    ]
