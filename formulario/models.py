from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Formulario(models.Model):
    comentario = models.TextField(blank=True)
    materias = ArrayField(models.TextField)
    habilidadesBlandas = ArrayField(models.TextField)



class Materia(models.Model):
    nombre = models.charField(max_length=64)


class HabilidadBlanda(models.Model):
    nombre = models.charField(max_length=64)