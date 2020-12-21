# TESTE DE PERMISSOES
#content_type = ContentType.objects.get(app_label='vacinacao', model='Profissional')
#permission = Permission.objects.create(codename='aplicar_vacina', name='Pode aplicar vacina', content_type=content_type)
#user = User.objects.get(username='testador')
#group = Group.objects.get(name='profissional')
#group.permissions.add(permission)
#user.groups.add(group)
# EXEMPLO DE USO
#   if user.has_perm('aplicar_vacina'):
#       ...

from vacinacao.models import Vacinacao
import datetime

def agendarVacinacao(dataAgendada, vacinacaoPrivada, keyVacina, keyPaciente, keyEstabelecimento):
    print("Agendando vacinação")
    vacinacao = Vacinacao.objects.get_or_create(
        data_agendamento = dataAgendada,
        privada = vacinacaoPrivada,
        vacinado = False,
        vacina = keyVacina,
        paciente = keyPaciente,
        estabelecimento = keyEstabelecimento
    )

def aprovarVacinacao(keyVacinacao):
    print("Aprovando vacinação")
    vacinacao = Vacinacao.objects.get(id=keyVacinacao)
    vacinacao.data_aprovado = datetime.now()
    vacinacao.save()

def aplicarVacinacao(keyVacinacao):
    print("Aplicando vacinação")
    vacinacao = Vacinacao.objects.get(id=keyVacinacao)
    vacinacao.data_vacinacao = datetime.now()
    vacinacao.vacinado = True
    vacinacao.save()

def retornarPosicao(keyPaciente):
    elementos = Vacinacao.objects.filter(data_agendamento__date=datetime.date.today()).filter(vacinado=False)
    posicao = 0
    for elemento in elementos:
        if elemento.paciente == keyPaciente:
            return posicao
        posicao+=1
    return -1