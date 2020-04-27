from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from usuario.usuario_logic import usuario_logic as ul


def index(request):
	template=loader.get_template('iniciar_sesion.html')
	estado = 0
	print("mana nada")
	if request.method == 'POST':
		print("mana entra")
		try:
			ul.iniciar_sesion(request.POST['correo'],request.POST['contraseña'])
			estado = 1
		except:
			estado = -1
	context={'estado':estado}
	return HttpResponse(template.render(context,request))

