from django.shortcuts import render
from .forms import UsuarioForm
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.template import loader
from oficina.oficina_logic import oficina_logic as ol
from .usuario_logic.usuario_logic import *
from django.contrib.auth.decorators import login_required
from .fusioncharts import *

def armarEstadisticasInteresados(id,idhtml):
    dataSource = {
    "chart": {
    "theme": "fusion",
    "yAxisName": "Cantidad",
    "xAxisName": "Mes",
    "yaxisminValue": "0","yaxismaxValue": "500",
    "caption":"Número de interesados vs Número de personas{br}que ven las oficinas de la empresa"
    },
    "categories": [{"category": [
    {"label": "Ene"},
    {"label": "Feb"},
    {"label": "Mar"},
    {"label": "Abr"},
    ]}],
    "dataset": [{"seriesname": "Interesados","data": [
    {"value": "105"},
    {"value": "123"},
    {"value": "100"},
    {"value": "450"}
    ]},
    {
    "seriesname": "Visitantes","data": [
    {"value": "245"},
    {"value": "232"},
    {"value": "221"},
    {"value": "207"}
    ]
    }
    ]}
    line = FusionCharts("msline", id, "100%", "90%", idhtml, "json", dataSource)
    return line

def armarHistorialDesocupacion():
    dataSource={
    "chart": {
        "theme": "fusion",
        "caption": "Tasa de desocupación en el tiempo",
        "subCaption": "últimos 4 meses",
        "xAxisName": "mes",
        "yAxisName": "Tasa de desocupación",
        "lineThickness": "2",
        "yaxisminValue": "0","yaxismaxValue": "100"
    },
    "data": [
        {
            "label": "Enero",
            "value": "15"
        },
        {
            "label": "Febrero",
            "value": "25"
        },
        {
            "label": "Marzo",
            "value": "34"
        },
        {
            "label": "Abril",
            "value": "23"
        }
    ],
    "trendlines": [
        {
            "line": [
                {
                    "startvalue": "18",
                    "color": "#29C3BE",
                    "displayvalue": "Tasa promedio",
                    "valueOnRight": "1",
                    "thickness": "2"
                }
            ]
        }
    ]}
    line = FusionCharts("line", "myFourthChart", "100%", "90%", "desocupacion", "json", dataSource)
    return line

def armarPorcentajeMercado():
    dataSource={
    "chart": {
        "subCaption": "último mes",
        "caption": "Porcentaje de mercado de la empresa",
        "showPercentInTooltip": "0",
        "decimals": "1",
        "useDataPlotColorForLabels": "1",
        "theme": "fusion"
    },
    "data": [{
            "label": "Espacio{br}coworking",
            "value": "13"
        },
        {
            "label": "Otras",
            "value": "87"
        }
    ]}
    line = FusionCharts("pie2d", "myThirdChart", "100%", "90%", "mercado:)", "json", dataSource)
    return line


def armarEstadisticasCalificacion(id,idhtml):
    dataSource={
    "chart": {"caption":"Calificación de las oficinas en el tiempo","xAxisName": "Semana","yAxisName": "calificación promedio",
        "theme": "fusion","yaxisminValue": "0","yaxismaxValue": "5",
    },
    "data": [
        {
            "label": "Mar 16",
            "value": "4"
        },
        {
            "label": "Mar 23",
            "value": "3"
        },
        {
            "label": "Mar 30",
            "value": "4"
        },
        {
            "label": "Abr 6",
            "value": "4"
        },
        {
            "label": "Abr 13",
            "value": "3"
        },
        {
            "label": "Abr 20",
            "value": "4"
        },
        {
            "label": "Abr 27",
            "value": "5"
        },
        {
            "label": "May 4",
            "value": "4"
        }
    ]}
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
        print("ID OFICINA LA QUE", idd)
        opcion='estadisticas_oficina'
        line = armarEstadisticasInteresados("myChart","ingresos")
    except:
        line = armarEstadisticasInteresados("myFirstChart","interesados")
        idd=None
    print("ID OFICINA", idd)
    context={'oficina':idd,'user':us,'correo' : id,'opcion':opcion,'output': line.render(), 'calificacion':d2.render(),'mercado':pie.render(),"historial":line2.render(),'oficinas':oficinas }
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