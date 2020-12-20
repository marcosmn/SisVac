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