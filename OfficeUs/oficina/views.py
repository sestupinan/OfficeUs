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

def get_oficina_dado_id(request,ide):
    template=loader.get_template('oficina/detail.html')
    oficina = get_oficina(ide)
    direccion = str(oficina.ubicacion).split(",")
    lista11 = {"Parqueadero incluido":0,"Ubicación cerca del transporte público":1}
    lista12 = {"Wifi de alta velocidad":oficina.wifi,"Aire acondicionado":oficina.aire,"Calefacción":oficina.calefaccion,"Lockers personales":oficina.locker,"Vista al exterior":oficina.vista}
    lista13 = {"Fotocopiadora":oficina.fotocopiadora,"Impresora":oficina.impresora,"Monitor dual":oficina.monitordual, "Monitor único": oficina.monitorunico,"Proyector":oficina.proyector, "Scanner":oficina.scanner}
    lista14 = {"Café  gratis":oficina.cafe,"Agua para beber gratis":oficina.agua,"Área de Chill-out":oficina.chillout, "Zona Dog-friendly":oficina.dog, "Eventos":oficina.eventos}
    context= {'calle':direccion[0],'carrera':direccion[1],'numero':direccion[2],'lista1':lista11,'lista2':lista12,'lista3':lista13,'lista4': lista14,'oficina':oficina}
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


