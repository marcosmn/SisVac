from vacinacao.models import Paciente
from django.contrib.auth.models import Group
from django.conf import settings
from django.core.mail import send_mail
from django.conf import settings


def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'google-oauth2':
        try:
            paciente = Paciente.objects.get(email=response.get('email'))
        except Paciente.DoesNotExist:
            paciente = Paciente.objects.create(
                email=response.get('email'),
                nome=response.get('first_name'),
                user=user,
            )
            grupoPaciente = Group.objects.get(name=settings.GRUPOS["paciente"])
            user.groups.add(grupoPaciente)
            subject = 'Cadastro na Carteira de Vacinação Virtual do SUS'
            message = 'Você foi cadastrado com sucesso na Carteira de Vacinação Virtual do SUS'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [response.get('email'), ]
            send_mail(subject, message, email_from, recipient_list)
