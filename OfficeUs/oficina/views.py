from django.shortcuts import render
from .forms import OficinaForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
from .oficina_logic.oficina_logic import *

# Create your views here.

def get(request,pagina):
	template=loader.get_template('oficina/get.html')
	lista = get_oficinas(pagina)
	context= {'lista':lista,'pagina':pagina+1,'num_atras':pagina,'num_alante':pagina+2}
	return HttpResponse(template.render(context,request))

def get_oficina_dado_keyword(request,keyword,pagina):
    template=loader.get_template('oficina/get.html')
    lista = get_oficinas_dado_una_palabra_clave(keyword,pagina)
    context= {'lista':lista,'pagina':pagina}
    return HttpResponse(template.render(context,request))

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


