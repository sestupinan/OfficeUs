from django.db import models
from ..models import Oficina
from usuario.models import Usuario
#Get todas las oficinas
numero_elementos_por_pagina = 15

def get_oficinas(pagina):
	q='select * from ' +Oficina.objects.model._meta.db_table+ ' limit %s offset %s'
	return Oficina.objects.raw(q,[numero_elementos_por_pagina,pagina*numero_elementos_por_pagina])

def create_oficina(foto,foto360,nombre,precio,contrato,ubicacion,localidad,desc,calificacion,user,parqueadero,transporte,wifi,aire,calefaccion,locker,vista,fotocopiadora,impresora,monitordual,monitorunico,proyector,scanner,cafe,agua,chillout,dog,eventos):
    Oficina.objects.create(foto=foto,
    	foto360=foto360,
    	nombre=nombre,
    	precio=precio,
    	tipo_contrato=contrato,
    	ubicacion=ubicacion,
    	localidad=localidad,
    	descripcion=desc,
    	calificacion=calificacion,
    	duenio=Usuario.objects.create(correo="Adena@quis.com"),
    	parqueadero=parqueadero,
    	transporte=transporte,
    	wifi=wifi,
    	aire=aire,
    	calefaccion=calefaccion,
    	locker=locker,
    	vista=vista,
    	fotocopiadora=fotocopiadora,
    	impresora=impresora,
    	monitordual=monitordual,
    	monitorunico=monitorunico,
    	proyector=proyector,
    	scanner=scanner,
    	cafe=cafe,
    	agua=agua,
    	chillout=chillout,
    	dog=dog,
    	eventos=eventos);
    Oficina.save()
    return ('Oficina creada')

def get_oficina(ide):
	return Oficina.objects.get(id=ide)

def get_oficinas_dado_una_palabra_clave(palabra,pagina):
	q='select * from +Oficina.objects.model._meta.db_table+ as p where p.nombre = %s limit %s offset %s'
	return Oficina.objects.raw(q,[palabra,numero_elementos_por_pagina,pagina*numero_elementos_por_pagina])