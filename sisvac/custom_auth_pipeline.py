from vacinacao.models import Paciente

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
      