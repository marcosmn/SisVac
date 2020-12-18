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
    data_validade = models.DateField()
    quantidade = models.IntegerField()
    quantidade_estoque = models.IntegerField()
    vacina = models.ForeignKey(Vacina, on_delete=models.PROTECT)


