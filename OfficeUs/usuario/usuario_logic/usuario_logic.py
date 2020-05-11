from django.db import models
from ..models import Usuario
import json
from oficina.models import Oficina, Historial

def calcular_promedio(lista,atributo):
	suma = 0
	if lista != None:
		if len(lista)>0:
			for elemento in lista:
				d = json.loads(str(elemento).replace("'", "\""))
				suma+=int(d[atributo])
			if atributo == "cantidad":
				return suma
			else:
				return suma/len(lista)
		else:
			return 0
	else:
		return 0

def estadisticas_mes(mes, atributo):
	return calcular_promedio(Historial.objects.filter(fecha_hora__icontains=mes),atributo)

def get_historial_dado_oficina(id):
	return Historial.objects.filter(oficina=id)

def get_usuario(ide):
	return Usuario.objects.get(id=ide)

def iniciar_sesion(correo, password):
	return Usuario.objects.get(contraseña=password,correo=correo)

def get_usuarios():
    usuarios = Usuario.objects.all()
    return (usuarios)

def create_user(form):
    user = form.save()
    user.save()
    return ('Usuario creado')

def dar_oficinas(id_user):
	return Oficina.objects.filter(duenio=id_user)