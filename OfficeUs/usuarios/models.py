from django.db import models



class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    correo = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    barrio = models.CharField(max_length=30)
    foto = models.CharField(max_length=100)
    def __str__(self):
        return '%s-%s-%s' % (self.nombre, self.correo, self.barrio)


class Oficina(models.Model):
    foto = models.CharField(max_length=100)
    nombre = models.CharField(max_length=30)
    precio = models.FloatField(null=True, blank=True, default=None)
    tipo_contrato = models.CharField(max_length=20)
    ubicacion = models.CharField(max_length=40)
    localidad = models.CharField(max_length=20)

    #duenio = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return '%s-%s-%s' % (self.nombre, self.precio, self.tipo_contrato)

