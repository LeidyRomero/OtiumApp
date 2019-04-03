from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Formulario(models.Model):
    comentario = models.TextField(blank=True)
    materias = ArrayField(models.TextField(blank=True))
    habilidadesBlandas = ArrayField(models.TextField(blank=True))



class Materia(models.Model):
    nombre = models.CharField(max_length=64)


class HabilidadBlanda(models.Model):
    nombre = models.CharField(max_length=64)