from django.db import models
from ..models import Usuario
from ..models import Oficina

#Get todas las oficinas
def get_oficinas():
    oficinas = Oficina.objects.all()
    return (oficinas)

def create_oficina(form):
    oficina = form.save()
    oficina.save()
    return ()

#Get todas las usuarios
def get_usuarios():
    usuarios = Usuario.objects.all()
    return (usuarios)

def create_user(form):
    user = form.save()
    user.save()
    return ()