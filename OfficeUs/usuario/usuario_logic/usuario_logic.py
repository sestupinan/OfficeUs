from django.db import models
from ..models import Usuario

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