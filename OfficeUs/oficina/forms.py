from django import forms
from .models import Oficina
from .models import Comment

class OficinaForm(forms.ModelForm):
    class Meta:
        model = Oficina
        fields = [
        'foto',
        'foto360',
        'nombre',
        'precio',
        'descripcion',
        'tipo_contrato',
        'ubicacion',
        'localidad',
        'calificacion',
        'parqueadero',
        'transporte',
        'wifi',
        'aire',
        'calefaccion',
        'locker',
        'vista',
        'fotocopiadora',
        'impresora',
        'monitordual',
        'monitorunico',
        'proyector',
        'scanner',
        'cafe',
        'agua',
        'chillout',
        'dog',
        'eventos',
        ]

        labels = {
        'foto' : 'Foto',
        'foto360':'Foto 360view',
        'nombre' : 'Nombre',
        'precio' : 'Precio',
        'descripcion':'Descripción',
        'tipo_contrato' : 'Tipo Contrato',
        'ubicacion':'Ubicación',
        'localidad':'Localidad',
        'calificacion':'Calificación',
        'parqueadero':'Parqueadero',
        'transporte':'transporte',
        'wifi':'wifi',
        'aire':'aire',
        'calefaccion':'calefaccion',
        'locker':'lockers',
        'vista':'vista',
        'fotocopiadora':'fotocopiadora',
        'impresora':'impresora',
        'monitordual':'monitordual',
        'monitorunico':'monitor',
        'proyector':'proyector',
        'scanner':'scanner',
        'cafe':'café',
        'agua':'agua',
        'chillout':'chillout',
        'dog':'dog',
        'eventos':'Eventos'
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        