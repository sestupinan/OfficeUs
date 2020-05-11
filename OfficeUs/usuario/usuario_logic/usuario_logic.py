from django.db import models
from ..models import Usuario
from oficina.models import Oficina, Historial

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