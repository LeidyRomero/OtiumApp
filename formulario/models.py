from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Formulario(models.Model):
    comentario = models.TextField(blank=True)
    def __str__(self):
        return self.comentario



class Materia(models.Model):
    class Meta:
        unique_together =(('nombre','formulario'),)
    nombre = models.CharField(max_length=64)
    formulario = models.ForeignKey(Formulario,on_delete = models.CASCADE, related_name = 'materia_formulario', blank = True )

    def __str__(self):
        return self.nombre

class HabilidadBlanda(models.Model):
    class Meta:
        unique_together =(('nombre','formulario'),)
    nombre = models.CharField(max_length=64)
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE, related_name='habilidad_formulario', blank = True)

    def __str__(self):
        return self.nombre