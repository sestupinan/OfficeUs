from django.db import models
from ..models import Usuario

#Get todos los usuarios
def iniciar_sesion(correo, password):
	return Usuario.objects.get(contraseña=password,correo=correo)

def get_usuarios():
    usuarios = Usuario.objects.all()
    return (usuarios)

def create_user(form):
    user = form.save()
    user.save()
    return ()