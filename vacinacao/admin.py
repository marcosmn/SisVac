from django.contrib import admin
from .models import Vacina, LoteVacina, Municipio, Estabelecimento
from .models import Vacinacao, VinculoProfissional, Profissional, Paciente, Agenda

from django.urls import path
from django import forms
import csv
from django.shortcuts import redirect, render
from io import TextIOWrapper

class CsvUploadForm(forms.Form):
    csv_file = forms.FileField()

admin.site.register(Vacina)
#class VacinaAdmin(admin.ModelAdmin):

@admin.register(LoteVacina)
class LoteVacinaAdmin(admin.ModelAdmin):
    change_list_template = "custom_admin/ver_lotevacinas.html"
    list_filter = ("vacina", )

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('/', self.lotesAtivos),
        ]
        return my_urls + urls
    
    def lotesAtivos(self, request):
        #quantidade=0
        #for p in LoteVacina.objects.raw('SELECT * FROM vacinacao_lotevacina WHERE quantidade_estoque > 0'):
        #    quantidade+=1
        #print(quantidade)
        #self.message_user(request, quantidade)
        return redirect("..")

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    change_list_template = "custom_admin/csv_upload_form.html"
    list_filter = ("uf", )

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('upload-csv/', self.upload_csv),
        ]
        return my_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = TextIOWrapper(request.FILES['csv_file'].file, encoding='utf-8')
            reader = csv.reader(csv_file)
            verificador = True
            for elemento in reader:
                if verificador:
                    verificador = False
                    continue
                municipio = Municipio.objects.get_or_create(
                    uf = elemento[0],
                    nome_uf = elemento[1],
                    codigo_municipio = elemento[2],
                    nome_municipio = elemento[3]
                )
            self.message_user(request, "Your csv file has been uploaded")
            return redirect("..")
        form = CsvUploadForm()
        payload = {"form": form}
        return render(
            request, "custom_admin/csv_form.html", payload
        )

@admin.register(Estabelecimento)
class EstabelecimentoAdmin(admin.ModelAdmin):
    change_list_template = "custom_admin/csv_upload_form.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('upload-csv/', self.upload_csv),
        ]
        return my_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = TextIOWrapper(request.FILES['csv_file'].file, encoding='utf-8')
            reader = csv.reader(csv_file)
            verificador = True
            for elemento in reader:
                if verificador:
                    verificador = False
                    continue
                estabelecimento = Estabelecimento.objects.get_or_create(
                    co_unidade = elemento[0],
                    co_cnes = elemento[1],
                    nu_cnpj_mantenedora = elemento[2],
                    tp_pfpj = elemento[3],
                    nivel_dep = elemento[4],
                    no_razao_social = elemento[5],
                    no_fantasia = elemento[6],
                    no_logradouro = elemento[7],
                    nu_endereco = elemento[8],
                    no_complemento = elemento[9],
                    no_bairro = elemento[10],
                    co_cep = elemento[11],
                    co_regiao_saude = elemento[12],
                    co_micro_regiao = elemento[13],
                    co_distrito_sanitario = elemento[14],
                    co_distrito_administrativo = elemento[15],
                    nu_telefone = elemento[16],
                    nu_fax = elemento[17],
                    no_email = elemento[18],
                    nu_cpf = elemento[19],
                    nu_cnpj = elemento[20],
                    co_atividade = elemento[21],
                    co_clientela = elemento[22],
                    nu_alvara = elemento[23],
                    dt_expedicao = elemento[25],
                    tp_orgao_expedidor = elemento[25],
                    dt_val_lic_sani = elemento[26],
                    tp_lic_sani = elemento[27],
                    tp_unidade = elemento[28],
                    co_turno_atendimento = elemento[29],
                    co_estado_gestor = elemento[30],
                    co_municipio_gestor = elemento[31],
                    dt_atualizacao = elemento[32],
                    co_usuario = elemento[33],
                    co_cpfdiretorcln = elemento[34],
                    reg_diretorcln = elemento[35],
                    st_adesao_filantrop = elemento[36],
                    co_motivo_desab = elemento[37],
                    no_url = elemento[38],
                    nu_latitude = elemento[39],
                    nu_longitude = elemento[40],
                    dt_atu_geo = elemento[41],
                    no_usuario_geo = elemento[42],
                    co_natureza_jur = elemento[43],
                    tp_estab_sempre_aberto = elemento[44],
                    st_geracredito_gerente_sgif = elemento[45],
                    st_conexao_internet = elemento[46],
                    co_tipo_unidade = elemento[47],
                    no_fantasia_abrev = elemento[48],
                    tp_gestao = elemento[49],
                    dt_atualizacao_origem = elemento[50],
                    co_tipo_estabelecimento = elemento[51],
                    co_atividade_principal = elemento[52],
                    st_contrato_formalizado = elemento[53],
                    ds_natureza_jur = elemento[54]
                )
            self.message_user(request, "Your csv file has been uploaded")
            return redirect("..")
        form = CsvUploadForm()
        payload = {"form": form}
        return render(
            request, "custom_admin/csv_form.html", payload
        )

admin.site.register(Agenda)

@admin.register(Vacinacao)
class VacinacaoAdmin(admin.ModelAdmin):
    list_filter = ("data_agendamento", )

admin.site.register(VinculoProfissional)

admin.site.register(Profissional)

admin.site.register(Paciente)

#quantidade=0
#for p in LoteVacina.objects.raw('SELECT * FROM vacinacao_lotevacina WHERE quantidade_estoque > 0'):
#    quantidade+=1
#admin.site.site_header = "Quantidade de lotes ativos: " + str(quantidade)