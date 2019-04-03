from django.db import models

# Create your models here.

class Empresa(models.Model):
	class Meta:
		unique_together = (('nombre','ubicacion'),)
	nombre = models.CharField(max_length = 255)
	ubicacion = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)

	def __str__(self):
		return self.nombre

class Oferta(models.Model):
	class Meta:
		unique_together = (('titulo','nombre'),)
	salario = models.IntegerField()
	titulo = models.CharField(max_length = 255)
	descripcion = models.TextField()
	ubicacion = models.ForeignKey(Empresa, on_delete = models.CASCADE, related_name = 'ubicacion_empresa')
	nombre = models.ForeignKey(Empresa, on_delete = models.CASCADE, related_name = 'nombre_empresa')
	jornada = models.CharField(max_length = 255)

	def __str__(self):
		return self.titulo

class Requerimiento(models.Model):
	class Meta:
		unique_together = (('oferta','requerimiento'),)
	oferta = models.ForeignKey(Oferta, on_delete = models.CASCADE)
	requerimiento = models.TextField()

	def __str__(self):
		return self.requerimiento

class Atributo(models.Model):
	class Meta:
		unique_together = (('oferta','nombre'),)
	oferta = models.ForeignKey(Oferta, on_delete = models.CASCADE)
	nombre = models.CharField(max_length = 64)

	def __str__(self):
		return self.nombre