from django.db import models
from usuario.models import Usuario

class Oficina(models.Model):
    foto = models.CharField(max_length=300)
    foto360 = models.CharField(max_length=1000)
    nombre = models.CharField(max_length=30)
    precio = models.FloatField(null=True, blank=True, default=None)
    tipo_contrato = models.CharField(max_length=20)
    ubicacion = models.CharField(max_length=40)
    localidad = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=500)
    duenio = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return '%s-%s-%s' % (self.nombre, self.precio, self.tipo_contrato)
