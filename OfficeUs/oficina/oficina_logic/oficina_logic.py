from django.db import models
from ..models import Oficina
#Get todas las oficinas
numero_elementos_por_pagina = 15

def get_oficinas(pagina):
	q='select * from '+Oficina.objects.model._meta.db_table+' limit %s offset %s'
	return Oficina.objects.raw(q,[numero_elementos_por_pagina,pagina*numero_elementos_por_pagina])

def create_oficina(form):
    oficina = form.save()
    oficina.save()
    return ()

def get_oficina(ide):
	return Oficina.objects.get(id=ide)

def get_oficinas_dado_una_palabra_clave(palabra,pagina):
	q='select * from '+Oficina.objects.model._meta.db_table+' as p where p.nombre = %s limit %s offset %s'
	return Oficina.objects.raw(q,[palabra,numero_elementos_por_pagina,pagina*numero_elementos_por_pagina])