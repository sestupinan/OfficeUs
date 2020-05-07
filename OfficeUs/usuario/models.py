from django.db import models

class Usuario(models.Model):
	id = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=30)
	correo = models.CharField(max_length=50)
	contraseña = models.CharField(max_length=30)
	direccion = models.CharField(max_length=30)
	barrio = models.CharField(max_length=30)
	foto = models.CharField(max_length=100)
	def __str__(self):
		return '%s / %s' % (self.correo, self.contraseña)