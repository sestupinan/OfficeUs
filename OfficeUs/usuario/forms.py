from django import forms
from .models import Usuario

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