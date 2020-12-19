import csv
from vacinacao.serializers import EstabelecimentoSerializer

class EstabelecimentoCsvUploader:
    def __init__(self, co_unidade, co_cnes, nu_cnpj_mantenedora):
        self.co_unidade = co_unidade
        self.co_cnes = co_cnes
        self.nu_cnpj_mantenedora = nu_cnpj_mantenedora

serializer = EstabelecimentoSerializer()
print(repr(serializer))