from django.shortcuts import render
from django.shortcuts import render
from .forms import UsuarioForm, OficinaForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .usuario_logic.usuario_logic import get_oficinas, get_usuarios,create_oficina, create_user
from django.contrib.auth.decorators import login_required

#@login_required
def usuario_list(request):
    usuarios = get_usuarios()
    context = {
        'usuario_list': usuarios
    }
    return render(request, 'Usuario/usuario.html', context)

def oficina_list(request):
    oficinas = get_oficinas()
    context = {
        'oficina_list': oficinas
    }
    return render(request, 'Usuario/oficina.html', context)

def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            rta=create_user(form)
            if rta=='Usuario creado':
                messages.add_message(request, messages.SUCCESS, rta)
                print(messages)
                return HttpResponseRedirect(reverse('usuarioCreate'))
            else:
                messages.add_message(request, messages.ERROR, rta)
                print(messages)
                messages.error(request, "Error")
                return HttpResponseRedirect(reverse('usuarioCreate'))
        else:
            print(form.errors)
    else:
        form = UsuarioForm()

    context = {
        'form': form,
    }

    return render(request, 'Usuario/usuarioCreate.html', context)

def oficina_create(request):
    if request.method == 'POST':
        form = OficinaForm(request.POST)
        if form.is_valid():
            rta=create_oficina(form)
            if rta=='Oficina creado':
                messages.add_message(request, messages.SUCCESS, rta)
                print(messages)
                return HttpResponseRedirect(reverse('oficinaCreate'))
            else:
                messages.add_message(request, messages.ERROR, rta)
                print(messages)
                messages.error(request, "Error")
                return HttpResponseRedirect(reverse('oficinaCreate'))
        else:
            print(form.errors)
    else:
        form = OficinaForm()

    context = {
        'form': form,
    }

    return render(request, 'Usuario/oficinaCreate.html', context)