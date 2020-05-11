
from .forms import OficinaForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
from .oficina_logic.oficina_logic import *
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
# Create your views here.

def get(request,pagina):
    template=loader.get_template('oficina/get.html')
    lista = get_oficinas(pagina)
    context= {'lista':lista,'pagina':pagina+1,'num_atras':pagina,'num_alante':pagina+2,'request':request.user}
    return HttpResponse(template.render(context,request))

def get_oficina_dado_id(request,ide):
    template=loader.get_template('oficina/detail.html')
    oficina = get_oficina(ide)


    comments = oficina.comments
    print(oficina.comments)
    new_comment = None
    
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = oficina
            # Save the comment to the database
            new_comment.save()

    else:
        comment_form = CommentForm()
      


    direccion = str(oficina.ubicacion).split(",")
    lista11 = {"Parqueadero incluido":0,"Ubicación cerca del transporte público":1}
    lista12 = {"Wifi de alta velocidad":oficina.wifi,"Aire acondicionado":oficina.aire,"Calefacción":oficina.calefaccion,"Lockers personales":oficina.locker,"Vista al exterior":oficina.vista}
    lista13 = {"Fotocopiadora":oficina.fotocopiadora,"Impresora":oficina.impresora,"Monitor dual":oficina.monitordual, "Monitor único": oficina.monitorunico,"Proyector":oficina.proyector, "Scanner":oficina.scanner}
    lista14 = {"Café  gratis":oficina.cafe,"Agua para beber gratis":oficina.agua,"Área de Chill-out":oficina.chillout, "Zona Dog-friendly":oficina.dog, "Eventos":oficina.eventos}
    lista15 = {'post': oficina,'comments': comments,'new_comment': new_comment, 'comment_form': comment_form}
    context= {'calle':direccion[0],'carrera':direccion[1],'numero':direccion[2],'lista1':lista11,'lista2':lista12,'lista3':lista13,'lista4': lista14,'lista5':lista15,'oficina':oficina, 'comment_form': comment_form}
    

    
    return HttpResponse(template.render(context,request))


def get_oficina_dado_keyword(request,keyword,pagina):
    template=loader.get_template('oficina/get.html')
    lista = get_oficinas_dado_una_palabra_clave(keyword,pagina)
    context= {'lista':lista,'pagina':pagina}
    return HttpResponse(template.render(context,request))

def create(request):
    if request.method == 'POST':
        user=None
        dic = request.POST.dict()
        print(dic)
        ubicacion = str(dic['calle'])+","+str(dic['carrera'])+","+str(dic['numero'])
        create_oficina(dic['foto'],"https://panoraven.com/es/embed/7H05TCQdC8",dic['nombre'],float(dic['precio']),dic['tipo_contrato'],ubicacion,dic['localidad'],dic['descripcion'],0,user,int(dic.get('parqueadero',0)),int(dic.get('transporte',0)),int(dic.get('wifi',0)),int(dic.get('aire',0)),int(dic.get('calefaccion',0)),int(dic.get('locker',0)),int(dic.get('vista',0)),int(dic.get('fotocopiadora',0)),int(dic.get('impresora',0)),int(dic.get('monitordual',0)),int(dic.get('monitorunico',0)),int(dic.get('proyector',0)),int(dic.get('scanner',0)),int(dic.get('cafe',0)),int(dic.get('agua',0)),int(dic.get('chillout',0)),int(dic.get('dog',0)),int(dic.get('eventos',0)))
    lista = {"Transporte":[["Parqueadero incluido","parqueadero"],["Ubicación cerca del transporte público","transporte"]],"Características":[["Wifi de alta velocidad","wifi"],["Aire acondicionado","aire"],["Calefacción","calefaccion"],["Lockers personales","locker"],["Vista al exterior","vista"]],"Equipamiento":[["Fotocopiadora","fotocopiadora"],["Impresora","impresora"],["Monitor dual","monitordual"], ["Monitor único","monitorunico"],["Proyector","proyector"],["Scanner","scanner"]],"Facilidades":[["Café  gratis","cafe"],["Agua para beber gratis","agua"],["Área de Chill-out","chillout"],["Zona Dog-friendly","dog"],["Eventos","eventos"]]}
    context = {'lista':lista,}
    return render(request, 'oficina/create.html', context)


