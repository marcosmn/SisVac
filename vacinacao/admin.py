from django.contrib import admin
from .models import Vacina, LoteVacina, Municipio, Estabelecimento, Vacinacao

from django.urls import path
from django import forms
import csv
from django.shortcuts import redirect, render
from vacinacao.serializers import EstabelecimentoSerializer

class CsvUploadForm(forms.Form):
    csv_file = forms.FileField()

admin.site.register(Vacina)
admin.site.register(LoteVacina)

#admin.site.register(Municipio)
@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    change_list_template = "custom_admin/csv_upload_form.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('upload-csv/', self.upload_csv),
        ]
        return my_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            reader = csv.reader(csv_file)
            # ...
            self.message_user(request, "Your csv file has been uploaded")
            return redirect("..")
        form = CsvUploadForm()
        payload = {"form": form}
        return render(
            request, "custom_admin/csv_form.html", payload
        )

#admin.site.register(Estabelecimento)
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
            csv_file = request.FILES['csv_file']
            for elemento in csv_file:
                print(elemento[2])
                #for contador in elemento:
                serializer = EstabelecimentoSerializer(data={'co_unidade': elemento[1]})
            self.message_user(request, "Your csv file has been uploaded")
            return redirect("..")
        form = CsvUploadForm()
        payload = {"form": form}
        return render(
            request, "custom_admin/csv_form.html", payload
        )

admin.site.register(Vacinacao)
