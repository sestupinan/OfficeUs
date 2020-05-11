from django.shortcuts import render
from .forms import UsuarioForm
import json
import io
from OfficeUs.settings import STATICFILES_DIRS
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.template import loader
from oficina.oficina_logic import oficina_logic as ol
from .usuario_logic.usuario_logic import *
from django.contrib.auth.decorators import login_required
from .fusioncharts import *

def armarGraficaOficina(id_grafico, id_en_html, id_oficina):
    d = str(STATICFILES_DIRS)[1:len(str(STATICFILES_DIRS))-1].replace("'","").replace("\\\\","/")
    d =d[0:len(d)-7]+'/OfficeUs'+d[len(d)-7:len(d)]
    with open(d+'/jsons/oficinas/'+ str(id_oficina)+'.json',"r",encoding="utf-8") as json_file: 
        dataSource = dict(json.load(json_file))
    line = FusionCharts("msline", id_grafico, "100%", "90%", id_en_html, "json", dataSource)
    return line

def armarEstadisticasInteresados(id,idhtml):
    d = str(STATICFILES_DIRS)[1:len(str(STATICFILES_DIRS))-1].replace("'","").replace("\\\\","/")
    d =d[0:len(d)-7]+'/OfficeUs'+d[len(d)-7:len(d)]
    with open(d+'/jsons/interesados/876.json',"r",encoding="utf-8") as json_file: 
        dataSource = dict(json.load(json_file))
    line = FusionCharts("msline", id, "100%", "90%", idhtml, "json", dataSource)
    return line

def armarHistorialDesocupacion():
    d = str(STATICFILES_DIRS)[1:len(str(STATICFILES_DIRS))-1].replace("'","").replace("\\\\","/")
    d =d[0:len(d)-7]+'/OfficeUs'+d[len(d)-7:len(d)]
    with open(d+'/jsons/desocupacion/876.json',"r",encoding="utf-8") as json_file: 
        dataSource = dict(json.load(json_file))
    line = FusionCharts("line", "myFourthChart", "100%", "90%", "desocupacion", "json", dataSource)
    return line

def armarPorcentajeMercado():
    d = str(STATICFILES_DIRS)[1:len(str(STATICFILES_DIRS))-1].replace("'","").replace("\\\\","/")
    d =d[0:len(d)-7]+'/OfficeUs'+d[len(d)-7:len(d)]
    with open(d+'/jsons/mercado/876.json',"r",encoding="utf-8") as json_file: 
        dataSource = dict(json.load(json_file))
    line = FusionCharts("pie2d", "myThirdChart", "100%", "90%", "mercado:)", "json", dataSource)
    return line


def armarEstadisticasCalificacion(id,idhtml):
    d = str(STATICFILES_DIRS)[1:len(str(STATICFILES_DIRS))-1].replace("'","").replace("\\\\","/")
    d =d[0:len(d)-7]+'/OfficeUs'+d[len(d)-7:len(d)]
    with open(d+'/jsons/calificacion/876.json',"r",encoding="utf-8") as json_file: 
        dataSource = dict(json.load(json_file))
    column2D = FusionCharts("column2d", id, "100%", "90%", idhtml, "json", dataSource)
    return column2D

def usuario_profile(request,id,opcion):
    pie = armarPorcentajeMercado()
    line2 = armarHistorialDesocupacion()
    d2 = armarEstadisticasCalificacion("mySecondChart","calificacionProm")
    template=loader.get_template('Usuario/profile.html')
    us=get_usuario(id)
    oficinas = dar_oficinas(id)
    try:
        id_oficina=opcion[opcion.index('=')+1:len(opcion)]
        idd=ol.get_oficina(int(id_oficina))
        opcion='estadisticas_oficina'
        historial = get_historial_dado_oficina(int(id_oficina))
        line = armarGraficaOficina("myChart", "ingresos", id_oficina)
        meses_cal = [estadisticas_mes("Ene", "calificacion",id_oficina),estadisticas_mes("Feb", "calificacion",id_oficina),estadisticas_mes("Mar", "calificacion",id_oficina),estadisticas_mes("Abr", "calificacion",id_oficina)]
        meses_ingresos = [estadisticas_mes("Ene", "cantidad",id_oficina),estadisticas_mes("Feb", "cantidad",id_oficina),estadisticas_mes("Mar", "cantidad",id_oficina),estadisticas_mes("Abr", "cantidad",id_oficina)]
    except:
        meses_cal= None
        meses_ingresos = None
        historial = None
        line = armarEstadisticasInteresados("myFirstChart","interesados")
        idd=None
    context={'meses_cal':meses_cal,'meses_ingresos':meses_ingresos,'historial2':historial,'oficina':idd,'user':us,'correo' : id,'opcion':opcion,'output': line.render(), 'calificacion':d2.render(),'mercado':pie.render(),"historial":line2.render(),'oficinas':oficinas }
    return HttpResponse(template.render(context,request))

#@login_required
def usuario_list(request):
    usuarios = get_usuarios()
    context = {'usuario_list': usuarios}
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
            else:
                messages.add_message(request, messages.ERROR, rta)
                print(messages)
                messages.error(request, "Error")
        else:
            print(form.errors)
    else:
        form = UsuarioForm()

    context = {'form': form,}
    return render(request, 'Usuario/usuarioCreate.html', context)