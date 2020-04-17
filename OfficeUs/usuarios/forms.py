from django import forms
from .models import Usuario, Oficina

class OficinaForm(forms.ModelForm):
    class Meta:
        model = Oficina
        fields = [
            'foto',
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

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre',
            'correo',
            'contraseña',
            'direccion',
            'barrio',
            'foto',
        ]

        labels = {
            'nombre' : 'Nombre',
            'correo' : 'Correo',
            'contraseña' : 'Contraseña',
            'direccion' : 'Direccion',
            'barrio':'Barrio',
            'foto':'Foto',
        }