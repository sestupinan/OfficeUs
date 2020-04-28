from django import forms
from .models import Oficina

class OficinaForm(forms.ModelForm):
    class Meta:
        model = Oficina
        fields = [
            'foto',
            'foto360',
            'nombre',
            'precio',
            'tipo_contrato',
            'ubicacion',
            'localidad',
            
        ]

        labels = {
            'foto' : 'Foto',
            'nombre' : 'Nombre',
            'precio' : 'Precio',
            'tipo_contrato' : 'Tipo Contrato',
            'ubicacion':'Ubicacion',
            'localidad':'Localidad',
        }
