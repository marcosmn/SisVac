# Generated by Django 3.1.4 on 2020-12-20 01:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacinacao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='cep',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='endereco',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='fone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='municipio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='vacinacao.municipio'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='nome',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]