from django.db import models

# Create your models here.
class Oferta(models.Model):
	class Meta:
		unique_together = (('titulo','empresa'),)
	salario = models.IntegerField()
	titulo = models.CharField(max_length = 255)
	descripcion = models.TextField()
	ubicacion = models.ForeignKey(Empresa, on_delete = models.CASCADE)
	empresa = models.ForeignKey(Empresa, on_delete = models.CASCADE)
	jornada = models.CharField(max_length = 255)

	def __str__(self):
		return self.titulo

#class Empresa(models.Model):
	#class Meta:
		#unique_together = (('nombre','ubicacion'),)
	#nombre = models.CharField(max_length = 255)
	#ubicacion = models.CharField(max_length = 255)
	#email = models.CharField(max_length = 255)

	#def __str__(self):
		#return self.nombre

#class Requerimiento(models.Model):
	#class Meta:
		#unique_together = (('oferta','requerimiento'),)
	#oferta = models.ForeignKey(Oferta, on_delete = models.CASCADE)
	#requerimiento = models.TextField()

	#def __str__(self):
		#return self.requerimiento