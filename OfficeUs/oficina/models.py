from django.db import models
from usuario.models import Usuario
from django.core.validators import MaxValueValidator, MinValueValidator

class Oficina(models.Model):
    id = models.IntegerField(primary_key=True)
    foto = models.CharField(max_length=300)
    foto360 = models.CharField(max_length=1000)
    nombre = models.CharField(max_length=30)
    precio = models.FloatField(null=True, blank=True, default=None)
    tipo_contrato = models.CharField(max_length=20)
    ubicacion = models.CharField(max_length=40)
    localidad = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=500)
    calificacion = models.FloatField(validators=[MaxValueValidator(5),MinValueValidator(0)])
    duenio = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    parqueadero=models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    transporte=models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    wifi = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    aire = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    calefaccion = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    locker = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    vista = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    fotocopiadora = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    impresora = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    monitordual = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    monitorunico = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    proyector = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    scanner = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    cafe = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    agua = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    chillout = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    dog = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    eventos = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    visitantes = models.IntegerField(null=True, blank=True, default=None)
    interesados = models.IntegerField(null=True, blank=True, default=None)
    porcentaje = models.FloatField(null=True, blank=True, default=None)
    def __str__(self):
        return '%s-%s-%s' % (self.nombre, self.precio, self.tipo_contrato)

class Historial(models.Model):
    id = models.IntegerField(primary_key=True)
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE)
    cantidad = models.FloatField(null=True, blank=True, default=None)
    tipo = models.CharField(max_length=20)
    fecha_hora = models.CharField(max_length=200)
    arrendatario = models.CharField(max_length=300)
    tipo_cliente = models.CharField(max_length=30)
    calificacion = models.FloatField(validators=[MaxValueValidator(5),MinValueValidator(0)])
    def __str__(self):
        return "{'calificacion':%s ,'cantidad':%s}" % (self.calificacion, self.cantidad)

class Comment(models.Model):
    post = models.ForeignKey(Oficina,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)