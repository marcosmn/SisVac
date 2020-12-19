from django.contrib import admin

from .models import Vacina, LoteVacina, Municipio, Estabelecimento, Vacinacao

admin.site.register(Vacina)
admin.site.register(LoteVacina)
admin.site.register(Municipio)
admin.site.register(Estabelecimento)
admin.site.register(Vacinacao)