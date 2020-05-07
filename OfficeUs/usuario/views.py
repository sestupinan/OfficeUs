from django.shortcuts import render
from .forms import UsuarioForm
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.template import loader
from .usuario_logic.usuario_logic import *
from django.contrib.auth.decorators import login_required

#@login_required
def usuario_profile(request,id,opcion):
    template=loader.get_template('Usuario/profile.html')
    us=get_usuario(id)
    context={'user':us,'correo' : id,'opcion':opcion}
    return HttpResponse(template.render(context,request))


#@login_required
def usuario_list(request):
    usuarios = get_usuarios()
    context = {
        'usuario_list': usuarios
    }
    return render(request, 'Usuario/usuario.html', context)

def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            rta=create_user(form)
            if rta=='Usuario creado':
                messages.add_message(request, messages.SUCCESS, rta)
                print(messages)
                return HttpResponseRedirect('/oficinas/get%0?m=2')
                return render(request, 'iniciar_sesion.html')
            else:
                messages.add_message(request, messages.ERROR, rta)
                print(messages)
                messages.error(request, "Error")
        else:
            print(form.errors)
    else:
        form = UsuarioForm()

    context = {
        'form': form,
    }

    return render(request, 'Usuario/usuarioCreate.html', context)